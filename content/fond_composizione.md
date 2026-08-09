---
id: fond_composizione
label: 复合与逆函数
parent: fond_fondamenta
prerequisites: [fond_funzioni, fond_iniettive_suriettive]
summary: 复合 g∘f 把 f 的输出作为 g 的输入；复合满足结合律，以恒等函数为单位。f 存在逆函数当且仅当 f 是双射，此时逆唯一，且 (g∘f)⁻¹ = f⁻¹∘g⁻¹。
status: learning
refs: Amann–Escher, Analysis I §I.3
---

[[fond_iniettive_suriettive|上一节]]定义了单射、满射与双射，但没有回答一个问题：什么样的函数存在「反过来」的函数，把 f 的输出送回原来的输入。要精确陈述这个问题，需要先有把两个函数依次作用的运算。本节先定义这个运算，再用它刻画可逆性。

## 复合

**定义（复合）** 设 f : X → Y，g : Y → V。定义

g ∘ f : X → V，  x ↦ g(f(x))，

称为 f 与 g 的**复合**(composition)，读作「f 之后接 g」。

定义要求 f 的到达域与 g 的定义域是同一个集合 Y，否则 g(f(x)) 无意义。

g ∘ f 是函数：

∀x ∈ X : f(x) ∈ Y 唯一确定 ⟹ g(f(x)) ∈ V 唯一确定<br>
（第一步因 f 是函数，第二步因 g 是函数；于是每个 x 恰好对应 V 中一个元素，符合[[fond_funzioni|函数]]的定义）

**注** 记号 g ∘ f 中 g 写在左边，先作用的却是 f。这个顺序来自 g(f(x)) 的写法。

<svg viewBox="0 0 400 175" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="mk" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#555"/>
    </marker>
    <marker id="mkb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#5A5FE0"/>
    </marker>
  </defs>
  <ellipse cx="60" cy="60" rx="32" ry="40" fill="none" stroke="#888" stroke-width="1.3"/>
  <ellipse cx="200" cy="60" rx="32" ry="40" fill="none" stroke="#888" stroke-width="1.3"/>
  <ellipse cx="340" cy="60" rx="32" ry="40" fill="none" stroke="#888" stroke-width="1.3"/>
  <text x="60" y="16" font-size="14" text-anchor="middle" fill="#333">X</text>
  <text x="200" y="16" font-size="14" text-anchor="middle" fill="#333">Y</text>
  <text x="340" y="16" font-size="14" text-anchor="middle" fill="#333">V</text>
  <circle cx="60" cy="60" r="3" fill="#333"/>
  <circle cx="200" cy="60" r="3" fill="#333"/>
  <circle cx="340" cy="60" r="3" fill="#333"/>
  <text x="46" y="80" font-size="11" fill="#555">x</text>
  <text x="186" y="80" font-size="11" fill="#555">f(x)</text>
  <text x="322" y="80" font-size="11" fill="#555">g(f(x))</text>
  <line x1="95" y1="60" x2="163" y2="60" stroke="#555" stroke-width="1.3" marker-end="url(#mk)"/>
  <line x1="235" y1="60" x2="303" y2="60" stroke="#555" stroke-width="1.3" marker-end="url(#mk)"/>
  <text x="129" y="52" font-size="12" fill="#555">f</text>
  <text x="269" y="52" font-size="12" fill="#555">g</text>
  <polyline points="60,104 60,140 340,140 340,104" fill="none" stroke="#5A5FE0" stroke-width="1.3" marker-end="url(#mkb)"/>
  <text x="200" y="158" font-size="12" text-anchor="middle" fill="#5A5FE0">g ∘ f</text>
</svg>

## 结合律

**命题（A–E 命题 3.3）** 设 f : X → Y，g : Y → U，h : U → V。则 (h ∘ g) ∘ f 与 h ∘ (g ∘ f) 都有定义，且

(h ∘ g) ∘ f = h ∘ (g ∘ f)。

**证明** 先验两边有定义、且定义域到达域相同：

g ∘ f : X → U，h : U → V ⟹ h ∘ (g ∘ f) : X → V<br>
h ∘ g : Y → V，f : X → Y ⟹ (h ∘ g) ∘ f : X → V<br>
（两次都是复合的衔接条件成立）

再逐点验值。由[[fond_funzioni|函数相等]]的定义，这一步不能省：

∀x ∈ X : ((h ∘ g) ∘ f)(x) = (h ∘ g)(f(x)) = h(g(f(x)))<br>
∀x ∈ X : (h ∘ (g ∘ f))(x) = h((g ∘ f)(x)) = h(g(f(x)))<br>
（两行各步都只用复合的定义；末端相同）∎

<svg viewBox="0 0 440 175" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="m2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#555"/>
    </marker>
    <marker id="m2o" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#E0612F"/>
    </marker>
    <marker id="m2b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#5A5FE0"/>
    </marker>
  </defs>
  <text x="45" y="92" font-size="14" text-anchor="middle" fill="#333">X</text>
  <text x="165" y="92" font-size="14" text-anchor="middle" fill="#333">Y</text>
  <text x="285" y="92" font-size="14" text-anchor="middle" fill="#333">U</text>
  <text x="405" y="92" font-size="14" text-anchor="middle" fill="#333">V</text>
  <line x1="58" y1="87" x2="152" y2="87" stroke="#555" stroke-width="1.2" marker-end="url(#m2)"/>
  <line x1="178" y1="87" x2="272" y2="87" stroke="#555" stroke-width="1.2" marker-end="url(#m2)"/>
  <line x1="298" y1="87" x2="392" y2="87" stroke="#555" stroke-width="1.2" marker-end="url(#m2)"/>
  <text x="105" y="80" font-size="12" text-anchor="middle" fill="#555">f</text>
  <text x="225" y="80" font-size="12" text-anchor="middle" fill="#555">g</text>
  <text x="345" y="80" font-size="12" text-anchor="middle" fill="#555">h</text>
  <polyline points="45,72 45,42 285,42 285,72" fill="none" stroke="#E0612F" stroke-width="1.2" marker-end="url(#m2o)"/>
  <text x="165" y="34" font-size="12" text-anchor="middle" fill="#E0612F">g ∘ f</text>
  <polyline points="165,102 165,132 405,132 405,102" fill="none" stroke="#5A5FE0" stroke-width="1.2" marker-end="url(#m2b)"/>
  <text x="285" y="148" font-size="12" text-anchor="middle" fill="#5A5FE0">h ∘ g</text>
  <text x="220" y="20" font-size="11" text-anchor="middle" fill="#777">先合橙色再接 h ： h ∘ (g ∘ f)</text>
  <text x="220" y="168" font-size="11" text-anchor="middle" fill="#777">先 f 再接蓝色 ： (h ∘ g) ∘ f</text>
</svg>

因此复合三个函数时可省略括号，写作 h ∘ g ∘ f；多于三个的复合同理。

**注（复合不交换）** 即使 g ∘ f 与 f ∘ g 都有定义，二者一般不等。取 X = Y = V = ℝ（ℝ 此处按熟悉的方式借用，严格构造留待后面），f(x) := x + 1，g(x) := x²：

(g ∘ f)(x) = (x + 1)² = x² + 2x + 1，  (f ∘ g)(x) = x² + 1<br>
x = 1 ⟹ (g ∘ f)(1) = 4 ≠ 2 = (f ∘ g)(1) ⟹ g ∘ f ≠ f ∘ g<br>
（一个反例即足以否定相等，因函数相等要求逐点相等）

## 交换图

复合关系常用图表示。约定把 f : X → Y 画成 X --f--> Y。

**定义（交换图）** 一个由集合与箭头组成的图称**交换**(commutative)，若图中任取两个集合，沿箭头方向从一个到另一个的**任意两条路径**，其复合相等。

<svg viewBox="0 0 440 175" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="m3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#555"/>
    </marker>
  </defs>
  <text x="50" y="45" font-size="14" text-anchor="middle" fill="#333">X</text>
  <text x="170" y="45" font-size="14" text-anchor="middle" fill="#333">Y</text>
  <text x="110" y="140" font-size="14" text-anchor="middle" fill="#333">V</text>
  <line x1="63" y1="40" x2="157" y2="40" stroke="#555" stroke-width="1.2" marker-end="url(#m3)"/>
  <text x="110" y="32" font-size="12" text-anchor="middle" fill="#555">f</text>
  <line x1="166" y1="56" x2="123" y2="124" stroke="#555" stroke-width="1.2" marker-end="url(#m3)"/>
  <text x="156" y="100" font-size="12" fill="#555">g</text>
  <line x1="54" y1="56" x2="97" y2="124" stroke="#555" stroke-width="1.2" marker-end="url(#m3)"/>
  <text x="52" y="100" font-size="12" fill="#555">h</text>
  <text x="110" y="165" font-size="12" text-anchor="middle" fill="#E0612F">交换 ⟺ h = g ∘ f</text>
  <line x1="230" y1="20" x2="230" y2="155" stroke="#e0e0e0" stroke-width="1"/>
  <text x="290" y="45" font-size="14" text-anchor="middle" fill="#333">X</text>
  <text x="400" y="45" font-size="14" text-anchor="middle" fill="#333">Y</text>
  <text x="290" y="130" font-size="14" text-anchor="middle" fill="#333">U</text>
  <text x="400" y="130" font-size="14" text-anchor="middle" fill="#333">V</text>
  <line x1="303" y1="40" x2="387" y2="40" stroke="#555" stroke-width="1.2" marker-end="url(#m3)"/>
  <text x="345" y="32" font-size="12" text-anchor="middle" fill="#555">f</text>
  <line x1="290" y1="53" x2="290" y2="112" stroke="#555" stroke-width="1.2" marker-end="url(#m3)"/>
  <text x="272" y="88" font-size="12" fill="#555">φ</text>
  <line x1="400" y1="53" x2="400" y2="112" stroke="#555" stroke-width="1.2" marker-end="url(#m3)"/>
  <text x="406" y="88" font-size="12" fill="#555">g</text>
  <line x1="303" y1="125" x2="387" y2="125" stroke="#555" stroke-width="1.2" marker-end="url(#m3)"/>
  <text x="345" y="147" font-size="12" text-anchor="middle" fill="#555">ψ</text>
  <text x="345" y="165" font-size="12" text-anchor="middle" fill="#E0612F">交换 ⟺ g ∘ f = ψ ∘ φ</text>
</svg>

左图从 X 到 V 有两条路径：直接走 h，或先 f 后 g。二者相等即 h = g ∘ f。右图从 X 到 V 也有两条：先 f 后 g，或先 φ 后 ψ。二者相等即 g ∘ f = ψ ∘ φ。

上一段结合律的图，正是这个约定的一个实例：从 X 到 V 的两条路径 h ∘ (g ∘ f) 与 (h ∘ g) ∘ f 相等，图交换。**结合律使得「沿箭头走过去」这件事与括号无关，交换图才有意义**——否则同一条路径按不同分段方式复合会得到不同的函数，图无法表达任何东西。

## 恒等函数

**定义（恒等函数）** 对集合 X，定义 id<sub>X</sub> : X → X，x ↦ x，称 X 上的**恒等函数**(identity function)。

**命题** ∀f : X → Y : f ∘ id<sub>X</sub> = f  ∧  id<sub>Y</sub> ∘ f = f。

**证明** 三者定义域皆为 X、到达域皆为 Y。

∀x ∈ X : (f ∘ id<sub>X</sub>)(x) = f(id<sub>X</sub>(x)) = f(x)<br>
∀x ∈ X : (id<sub>Y</sub> ∘ f)(x) = id<sub>Y</sub>(f(x)) = f(x)<br>
（各步只用复合与 id 的定义）∎

## 可逆当且仅当双射

**命题（A–E 命题 3.5）** 设 f : X → Y。则

f 双射 ⟺ ∃g : Y → X，g ∘ f = id<sub>X</sub> ∧ f ∘ g = id<sub>Y</sub>，

且此时 g 由 f 唯一确定。

**证明**

**(i) ⟹.** 设 f 双射。

f 满射 ⟹ ∀y ∈ Y, ∃x ∈ X : f(x) = y<br>
（存在性）

f 单射 ∧ f(x) = f(x′) = y ⟹ x = x′<br>
（唯一性）

⟹ ∀y ∈ Y, ∃!x ∈ X : f(x) = y

（合起来正是[[fond_funzioni|「恰好一个」]]。于是可定义 g : Y → X，把 y 送到这个唯一的 x。）

<svg viewBox="0 0 380 185" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="m4" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#555"/>
    </marker>
    <marker id="m4g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#E0612F"/>
    </marker>
  </defs>
  <ellipse cx="80" cy="90" rx="38" ry="62" fill="none" stroke="#888" stroke-width="1.3"/>
  <ellipse cx="290" cy="90" rx="38" ry="62" fill="none" stroke="#888" stroke-width="1.3"/>
  <text x="80" y="18" font-size="14" text-anchor="middle" fill="#333">X</text>
  <text x="290" y="18" font-size="14" text-anchor="middle" fill="#333">Y</text>
  <circle cx="80" cy="50" r="3.5" fill="#333"/><circle cx="80" cy="90" r="3.5" fill="#333"/><circle cx="80" cy="130" r="3.5" fill="#333"/>
  <circle cx="290" cy="50" r="3.5" fill="#333"/><circle cx="290" cy="90" r="3.5" fill="#333"/><circle cx="290" cy="130" r="3.5" fill="#333"/>
  <line x1="90" y1="47" x2="276" y2="47" stroke="#555" stroke-width="1.1" marker-end="url(#m4)"/>
  <line x1="90" y1="127" x2="276" y2="127" stroke="#555" stroke-width="1.1" marker-end="url(#m4)"/>
  <line x1="90" y1="84" x2="276" y2="84" stroke="#555" stroke-width="1.1" marker-end="url(#m4)"/>
  <text x="183" y="78" font-size="12" text-anchor="middle" fill="#555">f</text>
  <line x1="280" y1="97" x2="94" y2="97" stroke="#E0612F" stroke-width="1.1" stroke-dasharray="4,3" marker-end="url(#m4g)"/>
  <text x="183" y="112" font-size="12" text-anchor="middle" fill="#E0612F">g</text>
  <text x="190" y="175" font-size="10" text-anchor="middle" fill="#777">双射把 X 与 Y 逐点配对；把每个 y 送回与它配对的那个 x，即得 g</text>
</svg>

验证两个等式：

∀y ∈ Y : (f ∘ g)(y) = f(g(y)) = y ⟹ f ∘ g = id<sub>Y</sub><br>
（g(y) 按定义就是满足 f(·) = y 的那个元素）

∀x ∈ X : (g ∘ f)(x) = g(f(x)) = x ⟹ g ∘ f = id<sub>X</sub><br>
（记 y := f(x)；x 满足 f(x) = y，而这样的元素唯一，故 g(y) = x）

**(ii) ⟸.** 设 g 满足两个等式。

f 满射：∀y ∈ Y : f(g(y)) = y ⟹ 取 x := g(y) 得 f(x) = y<br>
（用 f ∘ g = id<sub>Y</sub>）

f 单射：f(x) = f(x′)<br>
 ⟹ g(f(x)) = g(f(x′))<br>
 ⟹ (g ∘ f)(x) = (g ∘ f)(x′)<br>
 ⟹ id<sub>X</sub>(x) = id<sub>X</sub>(x′)<br>
 ⟹ x = x′<br>
（第 1 步两边作用 g；第 2 步复合的定义；第 3 步用 g ∘ f = id<sub>X</sub>）

**(iii) 唯一性.** 设 h : Y → X 也满足 h ∘ f = id<sub>X</sub> ∧ f ∘ h = id<sub>Y</sub>。

g = g ∘ id<sub>Y</sub> = g ∘ (f ∘ h) = (g ∘ f) ∘ h = id<sub>X</sub> ∘ h = h<br>
（依次用：id 的单位性；f ∘ h = id<sub>Y</sub>；结合律；g ∘ f = id<sub>X</sub>；id 的单位性）∎

## 逆函数

**定义（逆函数）** 设 f : X → Y 双射。由上一命题，满足

f ∘ f⁻¹ = id<sub>Y</sub>  ∧  f⁻¹ ∘ f = id<sub>X</sub>

的函数 f⁻¹ : Y → X 存在且唯一，称 f 的**逆函数**(inverse function)。

上式对 f 与 f⁻¹ 对称，故 f⁻¹ 也满足命题 3.5 的条件：

f⁻¹ 双射 ∧ (f⁻¹)⁻¹ = f<br>
（把命题 3.5 中的 f 换成 f⁻¹、g 换成 f 即得）

**注（记号 f⁻¹ 的两种含义）** 对**任意**函数 f : X → Y（不要求双射）与 C ⊆ Y，记号

f⁻¹(C) := { x ∈ X : f(x) ∈ C }

表示 C 的**原像**(preimage)。特别地记 f⁻¹(y) := f⁻¹({y})，称 f 在 y 处的**纤维**(fiber)，它就是方程 f(x) = y 的解集，可能为空。原像的自变量是子集或点、取值是**子集**；逆函数的自变量是点、取值是**点**。f 双射时二者相容：{ f⁻¹(y) } = f⁻¹({y})。原像的系统性质留待下一节。

**命题（A–E 命题 3.6）** f : X → Y 双射 ∧ g : Y → V 双射 ⟹ g ∘ f 双射，且

(g ∘ f)⁻¹ = f⁻¹ ∘ g⁻¹。

**证明** f⁻¹ ∘ g⁻¹ : V → X。由命题 3.5，只需验两个复合皆为恒等：

(f⁻¹ ∘ g⁻¹) ∘ (g ∘ f) = f⁻¹ ∘ (g⁻¹ ∘ g) ∘ f = f⁻¹ ∘ id<sub>Y</sub> ∘ f = f⁻¹ ∘ f = id<sub>X</sub><br>
(g ∘ f) ∘ (f⁻¹ ∘ g⁻¹) = g ∘ (f ∘ f⁻¹) ∘ g⁻¹ = g ∘ id<sub>Y</sub> ∘ g⁻¹ = g ∘ g⁻¹ = id<sub>V</sub><br>
（两链第 1 步均用结合律重新分组，其后用逆的定义与 id 的单位性）

由命题 3.5，g ∘ f 双射且其逆为 f⁻¹ ∘ g⁻¹。∎

<svg viewBox="0 0 440 195" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="m5" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#555"/>
    </marker>
    <marker id="m5o" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#E0612F"/>
    </marker>
  </defs>
  <ellipse cx="70" cy="80" rx="30" ry="42" fill="none" stroke="#888" stroke-width="1.3"/>
  <ellipse cx="220" cy="80" rx="30" ry="42" fill="none" stroke="#888" stroke-width="1.3"/>
  <ellipse cx="370" cy="80" rx="30" ry="42" fill="none" stroke="#888" stroke-width="1.3"/>
  <text x="70" y="26" font-size="14" text-anchor="middle" fill="#333">X</text>
  <text x="220" y="26" font-size="14" text-anchor="middle" fill="#333">Y</text>
  <text x="370" y="26" font-size="14" text-anchor="middle" fill="#333">V</text>
  <line x1="103" y1="66" x2="185" y2="66" stroke="#555" stroke-width="1.2" marker-end="url(#m5)"/>
  <line x1="253" y1="66" x2="335" y2="66" stroke="#555" stroke-width="1.2" marker-end="url(#m5)"/>
  <text x="144" y="58" font-size="12" text-anchor="middle" fill="#555">f</text>
  <text x="294" y="58" font-size="12" text-anchor="middle" fill="#555">g</text>
  <line x1="337" y1="96" x2="255" y2="96" stroke="#E0612F" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#m5o)"/>
  <line x1="187" y1="96" x2="105" y2="96" stroke="#E0612F" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#m5o)"/>
  <text x="296" y="112" font-size="12" text-anchor="middle" fill="#E0612F">g⁻¹</text>
  <text x="146" y="112" font-size="12" text-anchor="middle" fill="#E0612F">f⁻¹</text>
  <text x="220" y="160" font-size="11" text-anchor="middle" fill="#777">去程 X→V 先 f 后 g；回程 V→X 只能先 g⁻¹ 后 f⁻¹</text>
  <text x="220" y="180" font-size="11" text-anchor="middle" fill="#E0612F">故 (g ∘ f)⁻¹ = f⁻¹ ∘ g⁻¹，右端次序颠倒</text>
</svg>

## 例

f : ℝ → ℝ，f(x) := 2x + 1。

f 单射：2x + 1 = 2x′ + 1 ⟹ 2x = 2x′ ⟹ x = x′<br>
f 满射：∀y ∈ ℝ，取 x := (y − 1)/2 ⟹ f(x) = 2·(y−1)/2 + 1 = y<br>
⟹ f 双射，f⁻¹(y) = (y − 1)/2

验证：<br>
f⁻¹(f(x)) = ((2x + 1) − 1)/2 = x<br>
f(f⁻¹(y)) = 2·(y − 1)/2 + 1 = y

<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
  <line x1="30" y1="198.6" x2="285" y2="198.6" stroke="#bbb" stroke-width="1"/>
  <line x1="101.4" y1="15" x2="101.4" y2="275" stroke="#bbb" stroke-width="1"/>
  <text x="288" y="202" font-size="10" fill="#999">x</text>
  <text x="106" y="18" font-size="10" fill="#999">y</text>
  <line x1="30" y1="270" x2="280" y2="20" stroke="#999" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="246" y="40" font-size="10" fill="#999">y = x</text>
  <line x1="65.7" y1="234.3" x2="172.9" y2="20" stroke="#E0612F" stroke-width="2"/>
  <text x="177" y="28" font-size="11" fill="#E0612F">f</text>
  <line x1="65.7" y1="234.3" x2="280" y2="127.1" stroke="#5A5FE0" stroke-width="2"/>
  <text x="256" y="118" font-size="11" fill="#5A5FE0">f⁻¹</text>
  <circle cx="101.4" cy="162.9" r="3.5" fill="#E0612F"/>
  <text x="66" y="158" font-size="10" fill="#E0612F">(0,1)</text>
  <circle cx="137.1" cy="198.6" r="3.5" fill="#5A5FE0"/>
  <text x="142" y="215" font-size="10" fill="#5A5FE0">(1,0)</text>
  <line x1="101.4" y1="162.9" x2="137.1" y2="198.6" stroke="#777" stroke-width="0.8" stroke-dasharray="3,2"/>
</svg>

两图像关于直线 y = x 对称。理由：由[[fond_funzioni|函数即其图像]]，

(a, b) ∈ f ⟺ b = f(a) ⟺ a = f⁻¹(b) ⟺ (b, a) ∈ f⁻¹<br>
（中间一步用逆函数的定义）

而 (a, b) ↦ (b, a) 就是平面上关于 y = x 的反射。（此处用到 ℝ 与平面坐标，均为借用。）

## 练习

(a) 设 f : X → Y，g : Y → X，g ∘ f = id<sub>X</sub>（**只**假设这一个等式）。证明 f 单射、g 满射；再举一例说明此时 f 不必满射。

(b) 证明：f : X → Y 单射 ∧ g : Y → V 单射 ⟹ g ∘ f 单射。

(c) 求 f : ℝ → ℝ，f(x) = 3x − 4 的逆函数，并验证两个恒等式。

## 参考解答

**(a)** f 单射：

f(x) = f(x′) ⟹ g(f(x)) = g(f(x′)) ⟹ id<sub>X</sub>(x) = id<sub>X</sub>(x′) ⟹ x = x′<br>
（第 1 步两边作用 g；第 2 步用 g ∘ f = id<sub>X</sub>）

g 满射：

∀x ∈ X，取 y := f(x) ∈ Y ⟹ g(y) = g(f(x)) = id<sub>X</sub>(x) = x<br>
（X 的每个元素都在 g 的像中）

f 不必满射的例子：X := {0}，Y := {0, 1}，f(0) := 0，g(0) := g(1) := 0。

(g ∘ f)(0) = g(0) = 0 = id<sub>X</sub>(0) ⟹ g ∘ f = id<sub>X</sub><br>
f(X) = {0} ∌ 1 ⟹ f 不满射 ∎

对照命题 3.5：**只有一个等式时只能得到「f 单射、g 满射」，两个等式同时成立才给出双射。** 这也说明命题 3.5 里那两个等式缺一不可。

**(b)** (g ∘ f)(x) = (g ∘ f)(x′)<br>
 ⟹ g(f(x)) = g(f(x′))<br>
 ⟹ f(x) = f(x′)<br>
 ⟹ x = x′<br>
（第 2 步用 g 单射；第 3 步用 f 单射）∎

**(c)** y = 3x − 4 ⟹ x = (y + 4)/3 ⟹ f⁻¹(y) = (y + 4)/3

f⁻¹(f(x)) = ((3x − 4) + 4)/3 = 3x/3 = x<br>
f(f⁻¹(y)) = 3·(y + 4)/3 − 4 = (y + 4) − 4 = y ∎

## 前瞻

上面那条注里出现的原像 f⁻¹(C)，对任意函数都有定义，且与像 f(A) 一样，可以看作 P(Y) → P(X) 与 P(X) → P(Y) 上的函数。它们在并、交、补之下的行为并不对称——原像与三种运算都可交换，像却只对并可交换。这是下一节的内容。
