---
id: fond_iniettive_suriettive
label: 单射、满射与双射
parent: fond_fondamenta
prerequisites: [fond_funzioni]
summary: 满射指 im(f) = Y，单射指 f(x) = f(y) ⟹ x = y，双射指两者兼备。满射性依赖于到达域，因此依赖于函数三元组中的 Y。
status: learning
refs: Amann–Escher, Analysis I §I.3
---

[[fond_funzioni|函数]]的定义只要求「每个输入恰好一个输出」。它并未禁止两件事：不同的输入取到同一个值，以及到达域中有元素**不被**取到（即 im(f) ⊊ Y）。分别排除这两种情形，得到两个基本概念。

## 定义

设 f : X → Y 是函数。

**满射**(surjective)：im(f) = Y

**单射**(injective)：∀x, y ∈ X : f(x) = f(y) ⟹ x = y

**双射**(bijective)：f 既是单射又是满射

也称 f 为一个**满射**(surjection)、**单射**(injection)、**双射**(bijection)。英文文献中常用 **onto** 表示满射、**one-to-one** 表示单射。

## 等价的写法

两个定义各有一个常用的等价形式，实际证明时按方便选用。

**单射的逆否形式**

∀x, y ∈ X : x ≠ y ⟹ f(x) ≠ f(y)

它与定义中的形式互为[[fond_proposizioni|逆否]]，故等价。定义中的形式（由函数值相等推出自变量相等）在证明中通常更好用，因为等式比不等式便于计算。

**满射的存在形式**

∀y ∈ Y, ∃x ∈ X : f(x) = y

这只是把 im(f) = Y 展开：im(f) ⊆ Y 恒成立，故 im(f) = Y 等价于 Y ⊆ im(f)，而后者正是上式。

**注（满射依赖于到达域）** 单射性只牵涉 f 在 X 上的取值规则；满射性还牵涉 Y 是什么。改变到达域会改变满射性：

f : ℝ → ℝ，x ↦ x²  不是满射（负数不被取到）<br>
g : ℝ → [0, ∞)，x ↦ x²  是满射<br>
（ℝ 此处按熟悉的方式借用，严格构造留待后面）

两者取值规则相同、定义域相同，但到达域不同，因而[[fond_funzioni|是两个不同的函数]]。这就是把函数定义成三元组 (X, G, Y)、而不只是图像 G 的原因——**若丢掉 Y，「是否满射」这个问题就无从提起**。

## 图示

以下三条曲线的定义域是横轴上的区间、到达域是纵轴上的区间。判读方法：看**水平线**与曲线的交点个数。

<svg viewBox="0 0 420 175" xmlns="http://www.w3.org/2000/svg">
<rect x="15" y="15" width="100" height="100" fill="none" stroke="#bbb" stroke-width="1"/>
<polyline points="15.0,115.0 20.0,103.9 25.0,92.6 30.0,82.0 35.0,73.1 40.0,66.4 45.0,62.1 50.0,60.2 55.0,60.5 60.0,62.3 65.0,65.0 70.0,67.7 75.0,69.5 80.0,69.8 85.0,67.9 90.0,63.6 95.0,56.9 100.0,48.0 105.0,37.4 110.0,26.1 115.0,15.0" fill="none" stroke="#E0612F" stroke-width="2"/>
<line x1="15" y1="66" x2="115" y2="66" stroke="#5A5FE0" stroke-width="1" stroke-dasharray="3,2"/>
<circle cx="40" cy="66" r="2.8" fill="#5A5FE0"/><circle cx="70" cy="66" r="2.8" fill="#5A5FE0"/><circle cx="88" cy="66" r="2.8" fill="#5A5FE0"/>
<text x="65" y="135" font-size="11" text-anchor="middle" fill="#333">满射，非单射</text>
<text x="65" y="152" font-size="9.5" text-anchor="middle" fill="#777">每条水平线至少交一次</text>
<text x="65" y="166" font-size="9.5" text-anchor="middle" fill="#5A5FE0">但有的交多次</text>
<rect x="160" y="15" width="100" height="100" fill="none" stroke="#bbb" stroke-width="1"/>
<polyline points="160.0,87.0 170.0,82.6 180.0,78.2 190.0,73.8 200.0,69.4 210.0,65.0 220.0,60.6 230.0,56.2 240.0,51.8 250.0,47.4 260.0,43.0" fill="none" stroke="#E0612F" stroke-width="2"/>
<line x1="160" y1="28" x2="260" y2="28" stroke="#B33" stroke-width="1" stroke-dasharray="3,2"/>
<text x="210" y="135" font-size="11" text-anchor="middle" fill="#333">单射，非满射</text>
<text x="210" y="152" font-size="9.5" text-anchor="middle" fill="#777">每条水平线至多交一次</text>
<text x="210" y="166" font-size="9.5" text-anchor="middle" fill="#B33">但有的一次也不交</text>
<rect x="305" y="15" width="100" height="100" fill="none" stroke="#bbb" stroke-width="1"/>
<polyline points="305.0,115.0 315.0,111.0 325.0,104.5 335.0,96.5 345.0,87.3 355.0,77.1 365.0,66.1 375.0,54.3 385.0,41.8 395.0,28.7 405.0,15.0" fill="none" stroke="#00A070" stroke-width="2"/>
<line x1="305" y1="66" x2="405" y2="66" stroke="#00A070" stroke-width="1" stroke-dasharray="3,2"/>
<circle cx="365" cy="66" r="2.8" fill="#00A070"/>
<text x="355" y="135" font-size="11" text-anchor="middle" fill="#333">双射</text>
<text x="355" y="152" font-size="9.5" text-anchor="middle" fill="#777">每条水平线恰交一次</text>
</svg>

**判读规则**（针对到达域中的每条水平线 y = 常数）：

至少交一次 ⟺ 满射（每个 y 都被取到）<br>
至多交一次 ⟺ 单射（不同的 x 不会给出同一个 y）<br>
恰好交一次 ⟺ 双射

注意与[[fond_funzioni|竖线判读]]的区别：竖线判断的是「这条曲线是不是函数的图像」，横线判断的是「这个函数是单射还是满射」。

## 例：投影

**例（A–E 例 3.4(b)）** 设 X₁, …, X<sub>n</sub> 非空。则对每个 k，[[fond_relazioni|投影]]

pr<sub>k</sub> : X₁ × ⋯ × X<sub>n</sub> → X<sub>k</sub>，  (x₁, …, x<sub>n</sub>) ↦ x<sub>k</sub>

是**满射**，但一般**不是单射**。

**满射的验证**：任给 a ∈ X<sub>k</sub>，因各 X<sub>j</sub> 非空，可从每个 X<sub>j</sub>（j ≠ k）任取一个元素 c<sub>j</sub>，构造

x := (c₁, …, c<sub>k−1</sub>, a, c<sub>k+1</sub>, …, c<sub>n</sub>)<br>
⟹ pr<sub>k</sub>(x) = a

故 X<sub>k</sub> 的每个元素都被取到。（**这里用到了各 X<sub>j</sub> 非空**——若某个 X<sub>j</sub> = ∅，则整个积为空，投影没有可用的原像。）

**非单射的反例**：取 n = 2，X₁ = X₂ = {0, 1}，k = 1。则

pr₁(0, 0) = 0 = pr₁(0, 1)，而 (0,0) ≠ (0,1)

两个不同的输入给出同一个值，故 pr₁ 不是单射。∎

## 否定形式

要证某个函数**不**是单射或**不**是满射，用下列形式（由[[fond_quantificatori|量词否定]]得到）：

**非单射**：∃x, y ∈ X : (f(x) = f(y)) ∧ (x ≠ y)

即举出两个不同的输入取到相同的值。

**非满射**：∃y ∈ Y, ∀x ∈ X : f(x) ≠ y

即举出到达域中一个不被取到的元素。

两者都是**举反例**：找出一个具体的对象即可，不必对所有情形论证。

## 练习

(a) 判断下列函数是单射、满射、双射，还是都不是。（ℝ 与 ℕ 按熟悉的方式借用。）

① f : ℝ → ℝ，f(x) = x³<br>
② f : ℝ → ℝ，f(x) = x² + 1<br>
③ f : ℕ → ℕ，f(n) = n + 1<br>
④ f : ℝ → (0, ∞)，f(x) = x²

(b) 设 X := {1, 2, 3}，Y := {a, b}。证明不存在从 X 到 Y 的单射，也不存在从 Y 到 X 的满射。（提示：先想清楚需要举出什么。）

(c) 设 f : X → Y 与 g : Y → V。证明：若 g ∘ f 是单射，则 f 是单射。（并举例说明此时 g 不必是单射。）

## 参考解答

**(a)**

① **双射**。单射：x³ = y³ ⟹ x = y（实数的三次方保序，暂且承认）。满射：任给 y ∈ ℝ，取 x := y^{1/3}。

② **都不是**。非单射：f(1) = 2 = f(−1) 而 1 ≠ −1。非满射：取 y := 0，则对一切 x 有 x² + 1 ≥ 1 > 0，故 0 不被取到。

③ **单射，非满射**。单射：n + 1 = m + 1 ⟹ n = m。非满射：取 y := 0，则 n + 1 = 0 对任何 n ∈ ℕ 都不成立（n + 1 ≥ 1）。

④ **满射，非单射**。满射：任给 y > 0，取 x := √y，则 x² = y（注意到达域已排除 0，故不必担心 0）。非单射：f(1) = 1 = f(−1)。

（②与④对照：取值规则相同，只是到达域从 ℝ 换成 (0,∞)，满射性就变了——再次印证满射依赖到达域。）∎

**(b)** **不存在 X → Y 的单射**：设 f : X → Y 任意。X 有 3 个元素，Y 只有 2 个。三个值 f(1), f(2), f(3) 都落在两元素集合 Y 中，故其中必有两个相等（否则 Y 至少要有 3 个不同元素）。设 f(i) = f(j) 且 i ≠ j，则 f 不单射。

**不存在 Y → X 的满射**：设 g : Y → X 任意。像 im(g) = { g(a), g(b) } 至多含 2 个元素，而 X 有 3 个元素，故 im(g) ≠ X，即 g 不满射。∎

（这两条的一般形式——有限集之间单射要求 |X| ≤ |Y|、满射要求 |X| ≥ |Y|——将在讨论[[fond_cardinalita|基数]]时精确化。）

**(c)** 设 g ∘ f 单射。要证 f 单射：

f(x) = f(x′)<br>
⟹ g(f(x)) = g(f(x′))（两边作用 g）<br>
⟹ (g ∘ f)(x) = (g ∘ f)(x′)（复合的定义）<br>
⟹ x = x′（g ∘ f 单射）

故 f 单射。∎

**g 不必单射的例子**：取 X := {1}，Y := {1, 2}，V := {1}，f(1) := 1，g(1) := g(2) := 1。则 g ∘ f : X → V 把 1 送到 1，定义域只有一个元素，平凡地是单射；但 g(1) = g(2) 而 1 ≠ 2，g 不单射。∎

## 前瞻

双射的意义在于它可以「反过来」：每个 y 恰好来自一个 x，于是能定义一个从 Y 回到 X 的函数。要精确陈述这件事，需要先有把两个函数依次作用的运算。见 [[fond_composizione|复合与逆函数]]。
