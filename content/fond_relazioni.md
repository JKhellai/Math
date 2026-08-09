---
id: fond_relazioni
label: 有序对与关系
parent: fond_fondamenta
prerequisites: [fond_insiemi, fond_dimostrazioni]
summary: 有序对 (a,b) 由「对应位置相等」这一特征性质刻画，笛卡尔积 X×Y 收集全部有序对；X 上的关系定义为 X×X 的子集，可有自反、对称、传递等性质。
status: learning
refs: Amann–Escher, Analysis I §I.2; Amann–Escher, Analysis I §I.4
---

[[fond_insiemi|集合]]由成员决定，与次序无关：{a, b} = {b, a}。但数学中经常需要**带次序**的配对——平面上的点 (1, 2) 与 (2, 1) 不同。本节先造出这种对象，再用它把「关系」化归为集合。

## 有序对

**定义（有序对）** 由两个对象 a、b 可以形成一个新对象 (a, b)，称**有序对**(ordered pair)。两个有序对的相等定义为

(a, b) = (a′, b′)  :⟺  (a = a′) ∧ (b = b′)

称 a 为 (a, b) 的**第一分量**、b 为**第二分量**。对 x = (a, b) 定义

pr₁(x) := a，  pr₂(x) := b

称 prⱼ(x) 为 x 的第 j 个**投影**(projection)，j ∈ {1, 2}。

上述定义只规定了「有序对是什么样的」——即它的相等如何判定——没有说它由什么造成。这就够用了：此后一切关于有序对的推理都只依据这条相等条件。

**注（有序对可以用集合造出来）** 若要求把有序对也化归为集合，可以定义

(a, b) := { {a}, {a, b} }

并验证它满足上面的相等条件。验证需要分情形讨论，此处不展开。这个构造的唯一作用是**说明有序对并非新的原始对象**，而是集合论内部可造的；一旦确认这一点，就可以把具体构造忘掉，只用相等条件。

## 笛卡尔积

**定义** 设 X, Y 是集合。一切有序对 (x, y)（x ∈ X，y ∈ Y）构成的集合称 X 与 Y 的**笛卡尔积**(Cartesian product)，记 X × Y。

**例（A–E 例 2.5）** X := {a, b}，Y := {∗, ◇, △}，则

X × Y = { (a,∗), (b,∗), (a,◇), (b,◇), (a,△), (b,△) }

共 2 × 3 = 6 个元素。

<svg viewBox="0 0 420 200" xmlns="http://www.w3.org/2000/svg">
<rect x="55" y="36" width="140" height="144" fill="#979AFF" fill-opacity="0.10" stroke="#5A5FE0" stroke-width="1.2"/>
<text x="125" y="26" font-size="12" text-anchor="middle" fill="#5A5FE0">X × Y</text>
<line x1="55" y1="180" x2="210" y2="180" stroke="#888" stroke-width="1.2"/>
<line x1="55" y1="180" x2="55" y2="30" stroke="#888" stroke-width="1.2"/>
<text x="215" y="184" font-size="12" fill="#555">X</text>
<text x="50" y="26" font-size="12" fill="#555">Y</text>
<text x="90" y="195" font-size="12" text-anchor="middle" fill="#333">a</text>
<text x="160" y="195" font-size="12" text-anchor="middle" fill="#333">b</text>
<text x="44" y="154" font-size="12" text-anchor="end" fill="#333">∗</text>
<text x="44" y="112" font-size="12" text-anchor="end" fill="#333">◇</text>
<text x="44" y="70" font-size="12" text-anchor="end" fill="#333">△</text>
<circle cx="90" cy="150" r="4" fill="#333"/><circle cx="160" cy="150" r="4" fill="#333"/>
<circle cx="90" cy="108" r="4" fill="#333"/><circle cx="160" cy="108" r="4" fill="#333"/>
<circle cx="90" cy="66" r="4" fill="#333"/><circle cx="160" cy="66" r="4" fill="#333"/>
<text x="240" y="80" font-size="11" fill="#555">每个格点是一个有序对</text>
<text x="240" y="100" font-size="11" fill="#555">例如左下角是 (a, ∗)</text>
<text x="240" y="126" font-size="11" fill="#777">共 2 × 3 = 6 个</text>
</svg>

**注（A–E 注 2.5(b)）** 上图把 X、Y 画成两条线、X × Y 画成矩形。这类图只用于辅助直觉，**不能用来证明定理**——它可以提示哪些命题也许可证，但证明必须靠推导。

## 命题 2.6

**命题（A–E 命题 2.6）** 设 X, Y 是集合。

(i) X × Y = ∅ ⟺ (X = ∅) ∨ (Y = ∅)

(ii) 一般地 X × Y ≠ Y × X

原书给出了 (i) 的完整证明，用意是示范证明如何构造与书写。它恰好把[[fond_dimostrazioni|证明方法]]那节的两种路径各用了一次。

**证明 (i)** 要证的是双条件，故分两个方向。

**⟹（用反证法）** 设 X × Y = ∅，并反设 (X = ∅) ∨ (Y = ∅) 为假。由[[fond_proposizioni|德摩根律]]，

¬( (X = ∅) ∨ (Y = ∅) ) = (X ≠ ∅) ∧ (Y ≠ ∅)

于是存在 x ∈ X 与 y ∈ Y，从而 (x, y) ∈ X × Y，与 X × Y = ∅ 矛盾。

**⟸（用逆否证明）** 要证 (X = ∅) ∨ (Y = ∅) ⟹ X × Y = ∅，改证其逆否

X × Y ≠ ∅ ⟹ ¬( (X = ∅) ∨ (Y = ∅) )

设 X × Y ≠ ∅，则存在 (x, y) ∈ X × Y，其中 x ∈ X、y ∈ Y。故 X ≠ ∅ 且 Y ≠ ∅，即

(X ≠ ∅) ∧ (Y ≠ ∅) = ¬( (X = ∅) ∨ (Y = ∅) ) ∎

**(ii) 的反例** 取 X := {a}，Y := {b}，a ≠ b。则

X × Y = { (a, b) }，  Y × X = { (b, a) }

而 (a, b) ≠ (b, a)（第一分量 a ≠ b），故两个积不相等。∎

**注** 笛卡尔积**不交换**。这与集合的并、交形成对照：∪ 与 ∩ 都[[fond_insiemi|可交换]]，× 不可。原因在于它的元素是**有序**对。

## 多重积

三个集合的积定义为

X × Y × Z := (X × Y) × Z

n 个集合同理，按递归定义：

X₁ × ⋯ × Xₙ := (X₁ × ⋯ × X<sub>n−1</sub>) × Xₙ

对 x ∈ X₁ × ⋯ × Xₙ，把 (⋯((x₁, x₂), x₃), …, xₙ) 简写为

(x₁, …, xₙ)

称 xⱼ 为 x 的第 j 个**分量**，也记 prⱼ(x)。X₁ × ⋯ × Xₙ 也写作

∏<sub>j=1</sub><sup>n</sup> Xⱼ

若所有因子相同（Xⱼ = X 对一切 j），则记 **X<sup>n</sup>**。例如 ℝ² 是平面上一切有序对，ℝ³ 是空间中一切三元组。

## 关系

有了笛卡尔积，就可以给「关系」一个精确的集合论含义。

**定义（关系）** X 上的一个（二元）**关系**(relation)是 X × X 的一个子集 R ⊆ X × X。对 (x, y) ∈ R，通常写作

x R y  或  x ∼<sub>R</sub> y

读作「x 与 y 有关系 R」。

这个定义把「关系」彻底化归为集合：**一个关系就是「哪些配对成立」这份名单**。比如在 X = {1,2,3} 上，关系「小于」就是子集

{ (1,2), (1,3), (2,3) } ⊆ X × X

<svg viewBox="0 0 420 200" xmlns="http://www.w3.org/2000/svg">
<line x1="60" y1="170" x2="200" y2="170" stroke="#888" stroke-width="1.2"/>
<line x1="60" y1="170" x2="60" y2="35" stroke="#888" stroke-width="1.2"/>
<text x="205" y="174" font-size="11" fill="#555">X</text>
<text x="55" y="30" font-size="11" fill="#555">X</text>
<text x="90" y="188" font-size="11" text-anchor="middle" fill="#333">1</text>
<text x="130" y="188" font-size="11" text-anchor="middle" fill="#333">2</text>
<text x="170" y="188" font-size="11" text-anchor="middle" fill="#333">3</text>
<text x="50" y="144" font-size="11" text-anchor="end" fill="#333">1</text>
<text x="50" y="104" font-size="11" text-anchor="end" fill="#333">2</text>
<text x="50" y="64" font-size="11" text-anchor="end" fill="#333">3</text>
<circle cx="90" cy="140" r="4" fill="#ccc"/><circle cx="130" cy="140" r="4" fill="#ccc"/><circle cx="170" cy="140" r="4" fill="#ccc"/>
<circle cx="90" cy="100" r="4" fill="#ccc"/><circle cx="130" cy="100" r="4" fill="#ccc"/><circle cx="170" cy="100" r="4" fill="#ccc"/>
<circle cx="90" cy="60" r="4" fill="#ccc"/><circle cx="130" cy="60" r="4" fill="#ccc"/><circle cx="170" cy="60" r="4" fill="#ccc"/>
<circle cx="90" cy="100" r="5.5" fill="#E0612F"/>
<circle cx="90" cy="60" r="5.5" fill="#E0612F"/>
<circle cx="130" cy="60" r="5.5" fill="#E0612F"/>
<line x1="72" y1="158" x2="182" y2="48" stroke="#5A5FE0" stroke-width="1" stroke-dasharray="4,3"/>
<text x="186" y="46" font-size="10" fill="#5A5FE0">对角线 Δ<tspan font-size="8">X</tspan></text>
<text x="240" y="70" font-size="11" fill="#E0612F">橙点 = 关系「小于」</text>
<text x="240" y="90" font-size="11" fill="#E0612F">(1,2), (1,3), (2,3)</text>
<text x="240" y="116" font-size="11" fill="#5A5FE0">虚线上的格点是 (x,x)</text>
<text x="240" y="134" font-size="11" fill="#777">「小于」不含对角线 ⟹ 非自反</text>
</svg>

## 关系的三种性质

设 R 是 X 上的关系。

**自反**(reflexive)：∀x ∈ X : x R x

即 R 包含**对角线**

Δ<sub>X</sub> := { (x, x) ; x ∈ X }

**传递**(transitive)：(x R y) ∧ (y R z) ⟹ x R z

**对称**(symmetric)：x R y ⟹ y R x

**例** 上图中的「小于」关系：传递（1<2 且 2<3 则 1<3），但**不自反**（1 < 1 不成立，图中对角线上无橙点），也**不对称**（1<2 但 2<1 不成立）。

而 X 上的「相等」关系恰好就是对角线 Δ<sub>X</sub> 本身，它自反、对称、传递三条全有。

## 关系的限制

**定义** 设 Y 是 X 的非空子集，R 是 X 上的关系。则

R<sub>Y</sub> := (Y × Y) ∩ R

是 Y 上的一个关系，称 R 到 Y 上的**限制**(restriction)。

显然

x R<sub>Y</sub> y  ⟺  x, y ∈ Y  ∧  x R y

上下文清楚时通常仍写 R 而不写 R<sub>Y</sub>。

## 练习

(a) 设 X := {1, 2}，Y := {1, 2, 3}。写出 X × Y 与 Y × X 的全部元素，并指出二者为何不相等。

(b) 设 X := {1,2,3}，考虑关系 R := { (1,1), (2,2), (3,3), (1,2), (2,1) }。判断它是否自反、对称、传递，逐条说明。

(c) 证明：若关系 R 既对称又传递，且 R 自反，则对任意 x, y ∈ X，

x R y ⟺ ( ∀z ∈ X : ( z R x ⟺ z R y ) )

## 参考解答

**(a)** 

X × Y = { (1,1), (1,2), (1,3), (2,1), (2,2), (2,3) }，共 6 个元素。<br>
Y × X = { (1,1), (1,2), (2,1), (2,2), (3,1), (3,2) }，共 6 个元素。

二者不相等：(1,3) ∈ X × Y，但 (1,3) ∉ Y × X（第二分量须属于 X = {1,2}，而 3 ∉ X）。∎

**(b)** **自反**：需 (1,1), (2,2), (3,3) 全在 R 中——都在，故自反（R 含对角线）。

**对称**：R 中的非对角元素是 (1,2) 与 (2,1)，二者互为反转、都在 R 中；对角元素反转后仍是自身。故对称。

**传递**：需逐一检查所有可拼接的配对。(1,2) 与 (2,1) 拼得 (1,1) ∈ R ✓；(2,1) 与 (1,2) 拼得 (2,2) ∈ R ✓；(1,2) 与 (2,2) 拼得 (1,2) ∈ R ✓；(1,1) 与 (1,2) 拼得 (1,2) ∈ R ✓；其余涉及 3 的只有 (3,3)，与自身拼得 (3,3) ∈ R ✓。故传递。

三条都满足。∎

**(c)** 分两个方向。

**⟹** 设 x R y。任取 z ∈ X，要证 z R x ⟺ z R y。

z R x ⟹ z R y：<br>
z R x ∧ x R y ⟹ z R y（传递）

z R y ⟹ z R x：<br>
x R y ⟹ y R x（对称）<br>
z R y ∧ y R x ⟹ z R x（传递）

**⟸** 设 ∀z : ( z R x ⟺ z R y )。取 z := x。由**自反**有 x R x，故左端成立，于是右端 x R y 成立。∎

**注** ⟸ 方向用到了自反性——这正是题目要求 R 自反的原因。若 R 不自反，取 z := x 这一步就走不通。三条性质（自反、对称、传递）合起来的关系将在下一节专门讨论。∎

## 前瞻

同时具备自反、对称、传递三条性质的关系有特殊的重要性：它把 X 分割成若干互不相交的「同类」块。这类关系称等价关系，由它得到的分块称等价类，而「把每一类当作一个新对象」正是后面构造 ℤ、ℚ 时反复使用的手法。见 [[fond_equivalenza|等价关系与商集]]。
