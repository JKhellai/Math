---
id: fond_funzioni
label: 函数
parent: fond_fondamenta
prerequisites: [fond_relazioni, fond_quantificatori]
summary: 函数是定义域中每个元素恰好对应到达域中一个元素的对应；作为集合论对象，它是三元组 (X, G, Y)，其中图像 G ⊆ X×Y 满足每个 x 恰有一个配对。
status: learning
refs: Amann–Escher, Analysis I §I.3
---

[[fond_relazioni|关系]]允许一个元素对应到多个元素，也允许它谁都不对应。数学中最常用的对应比这更严格：每个输入**恰好**给出一个输出。本节把这条限制精确化，并给出函数的纯集合论定义。

## 记号 ∃!

先补一个量词记号。定义

∃!x P(x)  :⟺  ∃x ( P(x) ∧ ∀y ( P(y) ⟹ y = x ) )

读作「恰好存在一个 x 使 P(x) 成立」。

右端是两件事的合取：

∃x P(x)<br>
（存在性）

∀y ( P(y) ⟹ y = x )<br>
（唯一性：凡满足 P 的都等于这个 x）

证明形如 ∃! 的命题时照例分两步：先造出一个，再证只此一个。

## 定义

**定义（函数）** 设 X, Y 是集合。从 X 到 Y 的一个**函数**(function)（同义词**映射**(map)）是一个对应 f，使

∀x ∈ X, ∃!y ∈ Y : y 与 x 对应

记作

f : X → Y，  x ↦ f(x)

由唯一性，与 x 对应的那个元素由 x 完全确定，记作 f(x)，称 f 在 x 处的**值**(value)。X 称 f 的**定义域**(domain)，记 dom(f)；Y 称 f 的**到达域**(codomain)。

**注** 箭头 → 连接两个集合，↦ 描述单个元素的去向，二者不可混用。

<svg viewBox="0 0 440 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="fa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#555"/>
    </marker>
    <marker id="far" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#B33"/>
    </marker>
  </defs>
  <text x="70" y="18" font-size="12" text-anchor="middle" fill="#333">是函数</text>
  <ellipse cx="40" cy="95" rx="22" ry="52" fill="none" stroke="#888" stroke-width="1.2"/>
  <ellipse cx="120" cy="95" rx="22" ry="52" fill="none" stroke="#888" stroke-width="1.2"/>
  <circle cx="40" cy="60" r="3" fill="#333"/><circle cx="40" cy="95" r="3" fill="#333"/><circle cx="40" cy="130" r="3" fill="#333"/>
  <circle cx="120" cy="70" r="3" fill="#333"/><circle cx="120" cy="120" r="3" fill="#333"/>
  <line x1="47" y1="60" x2="111" y2="69" stroke="#555" stroke-width="1.1" marker-end="url(#fa)"/>
  <line x1="47" y1="95" x2="111" y2="73" stroke="#555" stroke-width="1.1" marker-end="url(#fa)"/>
  <line x1="47" y1="130" x2="111" y2="122" stroke="#555" stroke-width="1.1" marker-end="url(#fa)"/>
  <text x="80" y="178" font-size="10" text-anchor="middle" fill="#777">每点恰一支箭</text>
  <line x1="163" y1="20" x2="163" y2="175" stroke="#e0e0e0" stroke-width="1"/>
  <text x="225" y="18" font-size="12" text-anchor="middle" fill="#B33">不是：某点两支箭</text>
  <ellipse cx="195" cy="95" rx="22" ry="52" fill="none" stroke="#888" stroke-width="1.2"/>
  <ellipse cx="275" cy="95" rx="22" ry="52" fill="none" stroke="#888" stroke-width="1.2"/>
  <circle cx="195" cy="60" r="3" fill="#B33"/><circle cx="195" cy="95" r="3" fill="#333"/><circle cx="195" cy="130" r="3" fill="#333"/>
  <circle cx="275" cy="70" r="3" fill="#333"/><circle cx="275" cy="120" r="3" fill="#333"/>
  <line x1="202" y1="59" x2="266" y2="68" stroke="#B33" stroke-width="1.1" marker-end="url(#far)"/>
  <line x1="202" y1="63" x2="266" y2="117" stroke="#B33" stroke-width="1.1" marker-end="url(#far)"/>
  <line x1="202" y1="95" x2="266" y2="74" stroke="#555" stroke-width="1.1" marker-end="url(#fa)"/>
  <line x1="202" y1="130" x2="266" y2="122" stroke="#555" stroke-width="1.1" marker-end="url(#fa)"/>
  <text x="235" y="178" font-size="10" text-anchor="middle" fill="#B33">唯一性失败</text>
  <line x1="318" y1="20" x2="318" y2="175" stroke="#e0e0e0" stroke-width="1"/>
  <text x="380" y="18" font-size="12" text-anchor="middle" fill="#B33">不是：某点无箭</text>
  <ellipse cx="350" cy="95" rx="22" ry="52" fill="none" stroke="#888" stroke-width="1.2"/>
  <ellipse cx="415" cy="95" rx="20" ry="52" fill="none" stroke="#888" stroke-width="1.2"/>
  <circle cx="350" cy="60" r="3" fill="#333"/><circle cx="350" cy="95" r="3" fill="#B33"/><circle cx="350" cy="130" r="3" fill="#333"/>
  <circle cx="415" cy="70" r="3" fill="#333"/><circle cx="415" cy="120" r="3" fill="#333"/>
  <line x1="357" y1="60" x2="407" y2="69" stroke="#555" stroke-width="1.1" marker-end="url(#fa)"/>
  <line x1="357" y1="130" x2="407" y2="121" stroke="#555" stroke-width="1.1" marker-end="url(#fa)"/>
  <text x="382" y="178" font-size="10" text-anchor="middle" fill="#B33">存在性失败</text>
</svg>

## 图像与纯集合论定义

上面的「对应」一词并未化归到集合语言。补上这一步。

**定义（图像）** 设 f : X → Y。称

graph(f) := { (x, y) ∈ X × Y : y = f(x) } = { (x, f(x)) : x ∈ X }

为 f 的**图像**(graph)。由[[fond_relazioni|笛卡尔积]]的定义，graph(f) ⊆ X × Y。

反过来，一个子集 G ⊆ X × Y 何时是某函数的图像？

**命题（A–E 注 3.1）** 设 G ⊆ X × Y 满足

∀x ∈ X, ∃!y ∈ Y : (x, y) ∈ G

则由「令 f(x) := 那个唯一的 y」定义的 f : X → Y 是函数，且 graph(f) = G。

**证明** 对每个 x ∈ X，条件给出唯一的 y 使 (x,y) ∈ G，故 f(x) 有定义且唯一确定，f 是函数。

(x, y) ∈ graph(f)<br>
 ⟺ y = f(x)<br>
 ⟺ (x, y) ∈ G<br>
（第 2 步用 f 的定义：f(x) 就是使 (x,·) ∈ G 的那个唯一元素）∎

于是可以把「对应」这个未加定义的词彻底消去：

**定义（函数，集合论形式）** 从 X 到 Y 的函数是一个三元组 (X, G, Y)，其中 G ⊆ X × Y 满足 ∀x ∈ X, ∃!y ∈ Y : (x,y) ∈ G。

**注** 定义取三元组而非只取 G，是因为到达域 Y 不能由 G 恢复：同一个 G 配上不同的 Y，得到不同的函数。下一节讲满射时，这个区别是本质的。

<svg viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect x="40" y="30" width="130" height="110" fill="none" stroke="#888" stroke-width="1.2"/>
  <text x="105" y="22" font-size="12" text-anchor="middle" fill="#00A070">G 是函数图像</text>
  <text x="30" y="150" font-size="10" fill="#999">X</text>
  <text x="30" y="36" font-size="10" fill="#999">Y</text>
  <polyline points="40.0,123.5 45.0,115.3 50.0,107.9 55.0,102.2 60.0,98.5 65.0,97.0 70.0,97.5 75.0,99.3 80.0,101.7 85.0,103.8 90.0,104.7 95.0,103.9 100.0,100.9 105.0,95.7 110.0,88.7 115.0,80.7 120.0,72.3 125.0,64.6 130.0,58.4 135.0,54.0 140.0,51.9 145.0,51.9 150.0,53.4 155.0,55.7 160.0,58.0 165.0,59.3 170.0,59.1" fill="none" stroke="#00A070" stroke-width="1.8"/>
  <line x1="115" y1="30" x2="115" y2="140" stroke="#5A5FE0" stroke-width="1" stroke-dasharray="3,3"/>
  <circle cx="115" cy="80.7" r="3.5" fill="#5A5FE0"/>
  <text x="105" y="163" font-size="10" text-anchor="middle" fill="#5A5FE0">每条竖线恰交一次</text>
  <rect x="230" y="30" width="130" height="110" fill="none" stroke="#888" stroke-width="1.2"/>
  <text x="295" y="22" font-size="12" text-anchor="middle" fill="#B33">H 不是</text>
  <polyline points="337.0,85.0 336.6,90.5 335.6,95.9 333.8,101.1 331.4,106.0 328.3,110.6 324.7,114.7 320.6,118.3 316.0,121.4 311.1,123.8 305.9,125.6 300.5,126.6 295.0,127.0 289.5,126.6 284.1,125.6 278.9,123.8 274.0,121.4 269.4,118.3 265.3,114.7 261.7,110.6 258.6,106.0 256.2,101.1 254.4,95.9 253.4,90.5 253.0,85.0 253.4,79.5 254.4,74.1 256.2,68.9 258.6,64.0 261.7,59.4 265.3,55.3 269.4,51.7 274.0,48.6 278.9,46.2 284.1,44.4 289.5,43.4 295.0,43.0 300.5,43.4 305.9,44.4 311.1,46.2 316.0,48.6 320.6,51.7 324.7,55.3 328.3,59.4 331.4,64.0 333.8,68.9 335.6,74.1 336.6,79.5 337.0,85.0" fill="none" stroke="#B33" stroke-width="1.8"/>
  <line x1="295" y1="30" x2="295" y2="140" stroke="#5A5FE0" stroke-width="1" stroke-dasharray="3,3"/>
  <circle cx="295" cy="43" r="3.5" fill="#5A5FE0"/>
  <circle cx="295" cy="127" r="3.5" fill="#5A5FE0"/>
  <line x1="243" y1="30" x2="243" y2="140" stroke="#999" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="295" y="163" font-size="10" text-anchor="middle" fill="#B33">有竖线交两次</text>
  <text x="243" y="176" font-size="10" text-anchor="middle" fill="#999">有竖线不交</text>
</svg>

## 函数相等

**定义** 设 f : X → Y，g : U → V。则

f = g  :⟺  X = U  ∧  Y = V  ∧  ∀x ∈ X : f(x) = g(x)

定义域、到达域、逐点取值，三者全同才算相等。

**注** 到达域参与判定，不是多余的讲究。取 f : ℝ → ℝ，x ↦ x² 与 g : ℝ → [0, ∞)，x ↦ x²（ℝ 此处按熟悉的方式借用，严格构造留待后面）。二者定义域相同、逐点取值相同，但到达域不同，因而**是两个不同的函数**。下一节会看到 g 满射而 f 不满射。

## 像

**定义（像）** 设 f : X → Y。称

im(f) := { y ∈ Y : ∃x ∈ X, y = f(x) } ⊆ Y

为 f 的**像**(image)。

im(f) 是到达域中真正被取到的部分。一般 im(f) ⊊ Y。上面 f : ℝ → ℝ，x ↦ x² 的像是 [0, ∞)，真含于到达域 ℝ。

## 例

以下 X, Y 为集合。

**(a) 恒等函数** id<sub>X</sub> : X → X，x ↦ x。上下文清楚时写 id。

**(b) 含入** 设 X ⊆ Y。称 i : X → Y，x ↦ x 为 X 到 Y 的**含入**(inclusion)。注意

i = id<sub>X</sub> ⟺ X = Y

（二者取值规则相同，差别只在到达域：i 的到达域是 Y，id<sub>X</sub> 的是 X）

**(c) 常函数** 设 X, Y 非空，b ∈ Y。则 X → Y，x ↦ b 是**常函数**(constant function)。

**(d) 限制** 设 f : X → Y，A ⊆ X。称 f|<sub>A</sub> : A → Y，x ↦ f(x) 为 f 到 A 上的**限制**(restriction)。有

f|<sub>A</sub> = f ⟺ A = X

**(e) 延拓** 设 A ⊆ X，g : A → Y。任何满足 f|<sub>A</sub> = g 的 f : X → Y 称 g 的**延拓**(extension)，记 f ⊇ g。例如由 (b)，id<sub>Y</sub> ⊇ i。

**注** 记号 f ⊇ g 与集合包含同形，这是有理由的：按集合论定义，函数就是它的图像，而 f 延拓 g 恰好意味着 graph(g) ⊆ graph(f)。

**(f) 诱导函数** 设 f : X → Y，im(f) ⊆ U ⊆ Y ⊆ V。则可定义 f₁ : X → U 与 f₂ : X → V，取值皆为 f₁(x) = f₂(x) = f(x)。三者取值规则相同、到达域不同，因而是三个不同的函数；通常仍用同一个符号 f，按需要视其到达域为 U、Y 或 V。

**(g) 特征函数** 设 X ≠ ∅，A ⊆ X。称

χ<sub>A</sub> : X → {0, 1}，  χ<sub>A</sub>(x) := 1（x ∈ A）， χ<sub>A</sub>(x) := 0（x ∈ Aᶜ）

为 A 的**特征函数**(characteristic function)。它把子集 A 编码成一个函数。

**(h) 投影** 设 X₁, …, Xₙ 非空。则

pr<sub>k</sub> : X₁ × ⋯ × Xₙ → X<sub>k</sub>，  (x₁, …, xₙ) ↦ x<sub>k</sub>，  k = 1, …, n

是函数，称第 k 个**投影**(projection)。

**注（空集的情形）** 定义未排除 X = ∅ 或 Y = ∅。

X = ∅ ⟹ 从 X 到 Y 恰有一个函数<br>
（条件 ∀x ∈ ∅ : … 空洞成立，且此时 G = ∅ 是唯一选择；称**空函数**）

Y = ∅ ∧ X ≠ ∅ ⟹ 不存在从 X 到 Y 的函数<br>
（取 x ∈ X，需有 y ∈ ∅ 与之对应，不可能）

## 练习

(a) 设 X := {1, 2, 3}，Y := {a, b}。写出从 X 到 Y 的全部函数共有几个，并说明理由。

(b) 设 f : X → Y，A ⊆ B ⊆ X。证明 f|<sub>A</sub> = (f|<sub>B</sub>)|<sub>A</sub>。

(c) 设 A, B ⊆ X。证明特征函数满足 χ<sub>A∩B</sub>(x) = χ<sub>A</sub>(x) · χ<sub>B</sub>(x) 对一切 x ∈ X 成立。

## 参考解答

**(a)** 共 **8** 个。

每个函数由它在 1, 2, 3 处的取值完全确定；每处独立地有 2 种选择（a 或 b）。

|Y|^|X| = 2³ = 8

（这也解释了函数集记号 Yˣ：从 X 到 Y 的函数个数是 |Y|^|X|。）

**(b)** 三者都是 A → Y 的函数，定义域到达域相同，只需逐点验值。

∀x ∈ A : f|<sub>A</sub>(x) = f(x)<br>
（限制的定义）

∀x ∈ A : (f|<sub>B</sub>)|<sub>A</sub>(x) = f|<sub>B</sub>(x) = f(x)<br>
（第 1 步因 A ⊆ B，第 2 步用限制的定义）

两者逐点相等，由[[fond_funzioni|函数相等]]得 f|<sub>A</sub> = (f|<sub>B</sub>)|<sub>A</sub>。∎

**(c)** 分情形。

x ∈ A ∩ B ⟹ χ<sub>A∩B</sub>(x) = 1，且 χ<sub>A</sub>(x) = χ<sub>B</sub>(x) = 1 ⟹ 乘积 = 1

x ∉ A ∩ B ⟹ χ<sub>A∩B</sub>(x) = 0，且 x ∉ A 或 x ∉ B ⟹ χ<sub>A</sub>(x) = 0 或 χ<sub>B</sub>(x) = 0 ⟹ 乘积 = 0<br>
（第 2 步用[[fond_insiemi|交]]的定义与[[fond_proposizioni|De Morgan]]）

两种情形下等式都成立。∎

## 前瞻

函数的定义只要求「每个输入恰好一个输出」，并未禁止两件事：不同输入取到同一个值，以及到达域中有元素不被取到（即 im(f) ⊊ Y）。分别排除这两种情形，得到单射与满射。见 [[fond_iniettive_suriettive|单射、满射与双射]]。
