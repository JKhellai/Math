#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — 数学知识体系 · 构建管线
============================================================================
把 content/**/*.md（带 YAML frontmatter 的数学概念节点，唯一真相来源）构建成
一张可下钻的 3D 知识图：

  content/**/*.md  →  build.py  →  graph.json  +  graph.html（自包含查看器）

严格遵循《构建系统规格》：
  · §2 五条设计约束：唯一真相来源 / 自底向上声明 / 能推导就不存 / 无消费者的字段不引入 / 无根之木
  · §5 解析 → 归属树 → 依赖网 → 容器叶判定 → 深度 → 布局数据 → 颜色 → 双链/正文 → 输出
  · §6 OKLab 颜色推导
  · §7 graph.json 输出结构

依赖：仅标准库（无 PyYAML / markdown —— frontmatter 自解析，正文交查看器的 marked 渲染）。
用法：`py -3 build.py`（Windows 可双击 build.bat）。
"""

import sys, os, re, json, glob, math, datetime

# 让 Windows 控制台也能打印中文
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT     = os.path.dirname(os.path.abspath(__file__))
CONTENT  = os.path.join(ROOT, "content")
TEMPLATE = os.path.join(ROOT, "viewer_template.html")
# 公开版（默认，可发布到 GitHub Pages）：剔除私人 status；入口为 index.html
# 私人版（--private，本地学习用，已被 .gitignore）：保留 status / 进度层
OUT_JSON_PUBLIC  = os.path.join(ROOT, "graph.json")
OUT_HTML_PUBLIC  = os.path.join(ROOT, "index.html")
OUT_JSON_PRIVATE = os.path.join(ROOT, "graph.private.json")
OUT_HTML_PRIVATE = os.path.join(ROOT, "index.private.html")

NEUTRAL_HEX = "#A9A9A9"  # Fondamenta 中性色（§6：不参与混合）

# ───────────────────────────────────────────────────────────────────────────
# §6  OKLab 颜色转换（按规格给定的精确实现）
# ───────────────────────────────────────────────────────────────────────────
def srgb_to_lin(c):
    c /= 255
    return ((c + 0.055) / 1.055) ** 2.4 if c > 0.04045 else c / 12.92

def lin_to_srgb(c):
    c = 1.055 * (c ** (1 / 2.4)) - 0.055 if c > 0.0031308 else 12.92 * c
    return max(0, min(255, round(c * 255)))

def rgb_to_oklab(r, g, b):
    r, g, b = srgb_to_lin(r), srgb_to_lin(g), srgb_to_lin(b)
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = l ** (1 / 3), m ** (1 / 3), s ** (1 / 3)
    return (0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
            1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
            0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_)

def oklab_to_rgb(L, a, b):
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    return (lin_to_srgb( 4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s),
            lin_to_srgb(-1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s),
            lin_to_srgb(-0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s))

def hex_to_rgb(h):
    h = h.strip().lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return "#" + "".join(f"{int(c):02X}" for c in rgb)

def mix_oklab(weighted):
    """weighted = [(hex, weight), ...] → 在 OKLab 空间按权重加权平均，转回 sRGB hex。"""
    tot = sum(w for _, w in weighted) or 1.0
    L = a = b = 0.0
    for hx, w in weighted:
        ol, oa, ob = rgb_to_oklab(*hex_to_rgb(hx))
        f = w / tot
        L += ol * f; a += oa * f; b += ob * f
    return rgb_to_hex(oklab_to_rgb(L, a, b))

# ───────────────────────────────────────────────────────────────────────────
# 极简 frontmatter (YAML 子集) 解析 —— 仅覆盖本契约用到的形态，无第三方依赖
#   · key: scalar           (字符串 / null / 带引号字符串)
#   · key: [a, b, c]        (行内列表)
#   · key:                  (块状列表)
#       - a
#       - b
# ───────────────────────────────────────────────────────────────────────────
def _scalar(v):
    v = v.strip()
    if v == "" :          return None
    if v in ("null", "~", "None"): return None
    if (len(v) >= 2) and ((v[0] == v[-1] == '"') or (v[0] == v[-1] == "'")):
        return v[1:-1]
    return v

def _inline_list(v):
    inner = v.strip()[1:-1].strip()
    if not inner:
        return []
    return [_scalar(x) for x in inner.split(",") if x.strip() != ""]

def parse_frontmatter(text):
    """返回 (frontmatter dict, body str)。无 frontmatter 时 fm={}。"""
    if not text.startswith("---"):
        return {}, text
    # 找到第二个 '---' 分隔线
    lines = text.splitlines()
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, text
    fm_lines = lines[1:end]
    body = "\n".join(lines[end + 1:])
    fm = {}
    i = 0
    while i < len(fm_lines):
        raw = fm_lines[i]
        if raw.strip() == "" or raw.lstrip().startswith("#"):
            i += 1; continue
        if ":" not in raw:
            i += 1; continue
        key, _, val = raw.partition(":")
        key = key.strip()
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            fm[key] = _inline_list(val)
        elif val == "":
            # 可能是块状列表
            items = []
            j = i + 1
            while j < len(fm_lines) and fm_lines[j].lstrip().startswith("- "):
                items.append(_scalar(fm_lines[j].lstrip()[2:]))
                j += 1
            if items:
                fm[key] = items
                i = j; continue
            fm[key] = None
        else:
            fm[key] = _scalar(val)
        i += 1
    return fm, body

# ───────────────────────────────────────────────────────────────────────────
# 双链 [[id]] / [[id|显示文字]] 解析
#   · 目标存在 → <a class="wl" data-id="..">文字</a> + 计入 popupLinks
#   · 目标不存在（前向引用）→ 优雅降级为普通文字（§5.8a），目标建好后自动恢复
# ───────────────────────────────────────────────────────────────────────────
WIKILINK = re.compile(r"\[\[\s*([^\[\]|]+?)\s*(?:\|\s*([^\[\]]+?)\s*)?\]\]")

def transform_links(body, label_of):
    popup, seen = [], set()
    def repl(m):
        tid  = m.group(1).strip()
        disp = (m.group(2) or "").strip()
        if tid in label_of:                       # 目标存在 → 真链接
            text = disp or label_of[tid] or tid
            if tid not in seen:
                seen.add(tid); popup.append({"id": tid, "text": text})
            return f'<a class="wl" data-id="{tid}">{text}</a>'
        # 悬空 → 普通文字（不报错、不建桩）
        return disp or tid
    return WIKILINK.sub(repl, body), popup

# ───────────────────────────────────────────────────────────────────────────
# 主构建流程
# ───────────────────────────────────────────────────────────────────────────
def build(public=True):
    files = sorted(glob.glob(os.path.join(CONTENT, "**", "*.md"), recursive=True))
    if not files:
        print(f"⚠  在 {CONTENT} 下没找到任何 .md 节点。");

    raw_nodes = []      # 解析后的原始节点（含 body 未转链接）
    by_id = {}
    for path in files:
        with open(path, "r", encoding="utf-8") as f:
            fm, body = parse_frontmatter(f.read())
        nid = fm.get("id") or os.path.splitext(os.path.basename(path))[0]
        if "id" not in fm:
            print(f"⚠  {os.path.relpath(path, ROOT)} 缺少 id，按文件名取 '{nid}'")
        node = {
            "id":            nid,
            "label":         fm.get("label") or nid,
            "parent":        fm.get("parent"),                 # None = 顶层主干
            "prerequisites": fm.get("prerequisites") or [],
            "summary":       fm.get("summary") or "",
            "status":        fm.get("status"),                 # 可选
            "refs":          fm.get("refs"),                   # 可选
            "color_raw":     fm.get("color"),                  # 仅顶层主干手填
            "order":         fm.get("order"),                  # 可选排序提示
            "aliases":       fm.get("aliases") or [],          # 可选，供搜索
            "_body":         body,
            "_path":         os.path.relpath(path, ROOT),
        }
        if nid in by_id:
            print(f"⚠  id 重复：'{nid}'（{node['_path']}）覆盖了先前定义")
        by_id[nid] = node
        raw_nodes.append(node)

    ids = set(by_id)
    label_of = {nid: n["label"] for nid, n in by_id.items()}

    # ── §5.2 归属树：parent 链（指向不存在的 parent → 视作顶层，不报错）──────────
    def parent_of(n):
        p = n["parent"]
        return p if (p in by_id) else None

    children = {nid: [] for nid in by_id}
    for n in raw_nodes:
        p = parent_of(n)
        if p:
            children[p].append(n["id"])

    # ── §5.4 容器/叶判定（推导）──────────────────────────────────────────────
    container_ids = {nid for nid, kids in children.items() if kids}

    # ── 顶层主干识别（parent==null）；并据依赖结构区分 地基 / 学科主干 ──────────
    #   §2：三学科主干各自 prerequisites:[fond_fondamenta]，建立在地基之上。
    #   ⇒ 被其它顶层主干依赖的顶层主干 = 地基（中性，不参与混合）；其余 = 学科主干。
    top_ids = [n["id"] for n in raw_nodes if parent_of(n) is None]
    top_set = set(top_ids)
    depended_top = set()
    for n in raw_nodes:
        if n["id"] in top_set:
            for pr in n["prerequisites"]:
                if pr in top_set:
                    depended_top.add(pr)
    foundation_ids = set(depended_top)                       # 地基主干
    discipline_ids = [t for t in top_ids if t not in foundation_ids]

    # ── §5.5 深度：顺 parent 链 ───────────────────────────────────────────────
    def depth_of(nid, _guard=None):
        _guard = _guard or set()
        if nid in _guard:        # 防环
            return 0
        p = parent_of(by_id[nid])
        if not p:
            return 0
        return 1 + depth_of(p, _guard | {nid})

    # ── §5.3 依赖网：prerequisites → 有向边 root→dependent（悬空端点跳过）──────
    edges, dangling_pre = [], []
    fwd = {nid: [] for nid in by_id}   # root → dependents
    bwd = {nid: [] for nid in by_id}   # dependent → roots
    for n in raw_nodes:
        for pr in n["prerequisites"]:
            if pr in by_id:
                edges.append({"from": pr, "to": n["id"], "type": "prerequisite"})
                fwd[pr].append(n["id"])
                bwd[n["id"]].append(pr)
            else:
                dangling_pre.append({"node": n["id"], "missing": pr})

    # 顶层主干（parent 链）—— 供颜色回退与色相布局
    def top_trunk_of(nid, _guard=None):
        _guard = _guard or set()
        if nid in _guard:
            return nid
        p = parent_of(by_id[nid])
        return nid if not p else top_trunk_of(p, _guard | {nid})

    # ── §6 颜色推导 ──────────────────────────────────────────────────────────
    discipline_color = {t: (by_id[t]["color_raw"] or NEUTRAL_HEX) for t in discipline_ids}

    def prereq_closure(nid):
        seen, stack = set(), list(bwd[nid])
        while stack:
            c = stack.pop()
            if c in seen:
                continue
            seen.add(c)
            stack.extend(bwd[c])
        return seen

    def derive_color(n):
        nid = n["id"]
        # 顶层主干：用手填 color（缺省退中性）
        if nid in top_set:
            return n["color_raw"] or NEUTRAL_HEX
        # 收集 prereq 祖先触及的学科主干（每个祖先顺 parent 链上溯顶层主干；排除地基）
        weights = {}
        for anc in prereq_closure(nid):
            t = top_trunk_of(anc)
            if t in discipline_color:
                weights[t] = weights.get(t, 0) + 1
        if not weights:
            # 不触及任何学科主干（只到地基/无前置）→ 回退自身归属主干基色
            home = top_trunk_of(nid)
            if home in discipline_color:
                return discipline_color[home]
            return NEUTRAL_HEX                      # 家在地基 → 中性
        if len(weights) == 1:
            return discipline_color[next(iter(weights))]
        return mix_oklab([(discipline_color[t], w) for t, w in weights.items()])

    # ── §6（查看器）承重程度：有多少节点最终（传递）依赖它 ─────────────────────
    def transitive_dependents(nid):
        seen, stack = set(), list(fwd[nid])
        while stack:
            c = stack.pop()
            if c in seen:
                continue
            seen.add(c)
            stack.extend(fwd[c])
        return len(seen)

    # ── §2 层内半径数据：同父兄弟内、仅计兄弟间前置的最长依赖链长（确定性环序）──
    ring_memo = {}
    def sibling_ring(nid, _guard=None):
        if nid in ring_memo:
            return ring_memo[nid]
        _guard = _guard or set()
        if nid in _guard:
            return 0
        p = parent_of(by_id[nid])
        sibs = set(children[p]) if p else top_set
        best = 0
        for r in bwd[nid]:
            if r in sibs:
                best = max(best, 1 + sibling_ring(r, _guard | {nid}))
        ring_memo[nid] = best
        return best

    # ── §5.8 正文：双链解析（其余 markdown 留给查看器的 marked 渲染）───────────
    nodes_out = []
    for n in raw_nodes:
        nid = n["id"]
        body, popup = transform_links(n["_body"], label_of)
        role = ("foundation" if nid in foundation_ids
                else "discipline" if nid in discipline_ids else None)
        out = {
            "id":          nid,
            "label":       n["label"],
            "parent":      parent_of(n),                 # 规范化：悬空 parent → None
            "summary":     n["summary"],
            "depth":       depth_of(nid),
            "isContainer": nid in container_ids,
            "isTop":       nid in top_set,
            "role":        role,                         # foundation|discipline|None
            "color":       derive_color(n),
            "ring":        sibling_ring(nid),            # 同父内径向环序
            "bearing":     transitive_dependents(nid),   # 承重（传递依赖者数）
            "popupLinks":  popup,
            "body":        body,
        }
        # 可选字段：有才写（§2.4 无消费者不强塞，但这些都有查看器消费）
        # status = 私人进度，仅私人版保留；公开版剔除（§3：不参与公开着色，亦不外泄进度）
        if (not public) and n["status"]:  out["status"]  = n["status"]
        if n["refs"]:    out["refs"]    = n["refs"]
        if n["order"] is not None: out["order"] = n["order"]
        if n["aliases"]: out["aliases"] = n["aliases"]
        nodes_out.append(out)

    graph = {
        "nodes": nodes_out,
        "edges": edges,
        "meta": {
            # 不写实时时间戳：保证"内容不变则输出不变"，避免每次构建都产生无谓的 git 改动
            "counts": {"nodes": len(nodes_out), "edges": len(edges),
                       "dangling_prerequisites": len(dangling_pre)},
            "palette": {"neutral": NEUTRAL_HEX, "disciplines": discipline_color},
            "topIds": top_ids,
            "foundationIds": sorted(foundation_ids),
            "disciplineIds": discipline_ids,
            "danglingPrerequisites": dangling_pre,
        },
    }
    return graph, dangling_pre

# ───────────────────────────────────────────────────────────────────────────
def embed_html(graph, out_html):
    if not os.path.exists(TEMPLATE):
        print(f"⚠  找不到查看器模板 {TEMPLATE}，跳过 HTML 生成。")
        return False
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        tpl = f.read()
    payload = json.dumps(graph, ensure_ascii=False, separators=(",", ":"))
    payload = payload.replace("</", "<\\/")     # 防止 body 内出现 </script> 提前闭合
    if "/*__GRAPH_DATA__*/" not in tpl:
        print("⚠  模板缺少 /*__GRAPH_DATA__*/ 占位符，无法内嵌数据。")
        return False
    html = tpl.replace("/*__GRAPH_DATA__*/", payload)
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(html)
    return True

def main():
    public = "--private" not in sys.argv
    out_json = OUT_JSON_PUBLIC if public else OUT_JSON_PRIVATE
    out_html = OUT_HTML_PUBLIC if public else OUT_HTML_PRIVATE
    mode = "公开版（剔除 status）" if public else "私人版（保留 status / 进度层）"
    print(f"· 构建数学知识图 … [{mode}]")
    graph, dangling = build(public=public)
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=2)
    c = graph["meta"]["counts"]
    print(f"  {os.path.basename(out_json)}  ✓  {c['nodes']} 节点 · {c['edges']} 边")
    if dangling:
        print(f"  前向引用（悬空 prerequisites，已优雅跳过 {len(dangling)} 条）：")
        for d in dangling:
            print(f"     · {d['node']} → 缺失 {d['missing']}")
    if embed_html(graph, out_html):
        print(f"  {os.path.basename(out_html)}  ✓  自包含查看器已生成")
    print(f"· 完成。双击 {os.path.basename(out_html)} 即可查看（无需服务器）。")
    if public:
        print("  提示：本地想看私人进度层，运行  py -3 build.py --private  （产物已被 .gitignore）")

if __name__ == "__main__":
    main()
