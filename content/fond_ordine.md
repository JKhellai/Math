---
id: fond_ordine
label: 序关系
parent: fond_fondamenta
prerequisites: [fond_relazioni, fond_insiemi]
summary: 自反、传递、反对称的关系称偏序；再加上任两元素可比即全序。由偏序定义上界、最大元与上确界（上界中的最小者），最大元存在则等于上确界，反之不然。
status: learning
refs: Amann–Escher, Analysis I §I.4
---

[[fond_equivalenza|等价关系]]把「同类」这个概念精确化。关系的另一大类刻画「谁在谁前面」——[[fond_relazioni|自反、传递]]仍然要求，但对称换成一条相反的要求。此后 ℕ、ℚ、ℝ 上的大小关系都是本节定义的实例。

## 偏序与全序

**定义（偏序）** X 上的关系 ≤ 称**偏序**(partial order)，若它自反、传递，且**反对称**(anti-symmetric)：

(x ≤ y) ∧ (y ≤ x) ⟹ x = y

此时称 (X, ≤) 为**偏序集**(partially ordered set)。上下文清楚时把 (X, ≤) 简记为 X。

**定义（全序）** 偏序 ≤ 若还满足

∀ x, y ∈ X : (x ≤ y) ∨ (y ≤ x)

则称**全序**(total order)，(X, ≤) 称**全序集**。

差别在最后这条：全序要求**任意两个元素都可比**，偏序不要求。

**注（对称与反对称）** 二者不是互相否定的关系。对称说「x ∼ y 就一定 y ∼ x」；反对称说「若两个方向都成立，则两元素相等」。[[fond_relazioni|对角线]] Δ<sub>X</sub>（相等关系）同时满足两者。

**记号（A–E 注 4.3(a)）** 由 ≤ 派生出三个记号：

x ≥ y :⟺ y ≤ x<br>
x < y :⟺ (x ≤ y) ∧ (x ≠ y)<br>
x > y :⟺ y < x

**注（A–E 注 4.3(b)）** X 全序时，对任一对 x, y ∈ X，下列三者**恰有一个**成立：

x < y，  x = y，  x > y

X 只是偏序而非全序时，至少存在两个元素 x, y **不可比**(incomparable)——x ≤ y 与 y ≤ x 都不成立。

## 例

**(a)** 设 (X, ≤) 是偏序集，Y ⊆ X。则 ≤ 到 Y 上的[[fond_relazioni|限制]]仍是偏序。

**(b)（标准例子）** (P(X), ⊆) 是偏序集，⊆ 称 P(X) 上的**包含序**(inclusion order)。

验证三条：

A ⊆ A（自反）<br>
A ⊆ B ∧ B ⊆ C ⟹ A ⊆ C（传递，即[[fond_dimostrazioni|包含的传递性]]）<br>
A ⊆ B ∧ B ⊆ A ⟹ A = B（反对称，即[[fond_insiemi|外延原则的推论]]）

**它一般不是全序。** 取 X := {a, b}（a ≠ b），则 {a} 与 {b} 不可比：两者互不包含。

<svg viewBox="0 0 420 210" xmlns="http://www.w3.org/2000/svg">
<line x1="110" y1="160" x2="60" y2="118" stroke="#888" stroke-width="1.2"/>
<line x1="110" y1="160" x2="160" y2="118" stroke="#888" stroke-width="1.2"/>
<line x1="60" y1="100" x2="110" y2="60" stroke="#888" stroke-width="1.2"/>
<line x1="160" y1="100" x2="110" y2="60" stroke="#888" stroke-width="1.2"/>
<text x="110" y="176" font-size="13" text-anchor="middle" fill="#333">∅</text>
<text x="60" y="112" font-size="13" text-anchor="middle" fill="#E0612F">{a}</text>
<text x="160" y="112" font-size="13" text-anchor="middle" fill="#E0612F">{b}</text>
<text x="110" y="52" font-size="13" text-anchor="middle" fill="#333">{a,b}</text>
<line x1="82" y1="107" x2="138" y2="107" stroke="#B33" stroke-width="1.4" stroke-dasharray="4,3"/>
<text x="110" y="132" font-size="10" text-anchor="middle" fill="#B33">不可比</text>
<text x="235" y="70" font-size="11" fill="#555">连线自下而上表示 ⊆</text>
<text x="235" y="92" font-size="11" fill="#555">∅ ⊆ {a} ⊆ {a,b}</text>
<text x="235" y="118" font-size="11" fill="#B33">但 {a} 与 {b} 互不包含</text>
<text x="235" y="138" font-size="11" fill="#B33">⟹ (P(X), ⊆) 非全序</text>
</svg>

**约定（A–E）** 除非另有说明，P(X)（以及它的任何子集）总视为带包含序的偏序集。

**(c)** 设 X 是集合，(Y, ≤) 是偏序集。则

f ≤ g  :⟺  ∀x ∈ X : f(x) ≤ g(x)

在函数集 [[fond_immagine_preimmagine|Funct(X, Y)]] 上定义一个偏序（逐点比较）。即使 Y 是全序的，Funct(X, Y) 一般也**不是**全序——两个函数可以在某些点上一大一小、在另一些点上反过来，从而不可比。

## 上界、最大元

设 (X, ≤) 是偏序集，A 是 X 的非空子集。

**定义** 元素 s ∈ X 称 A 的**上界**(upper bound)，若

∀a ∈ A : a ≤ s

类似地，s 称 A 的**下界**(lower bound)，若 ∀a ∈ A : a ≥ s。

A 有上界时称**上有界**，有下界时称**下有界**，两者兼备时称**有界**(bounded)。

**定义** 元素 m 称 A 的**最大元**(maximum)，记 max(A)，若

m ∈ A  且  m 是 A 的上界

**最小元** min(A) 同理定义。

**注** A 至多有一个最大元、至多有一个最小元。（设 m、m′ 都是最大元，则二者都在 A 中且都是上界，故 m ≤ m′ 与 m′ ≤ m 同时成立，由**反对称**得 m = m′。这是反对称性的直接用处。）

关键在于 **m ∈ A** 这个要求：上界只须站在 A 的上方，最大元还必须**属于** A。

## 上确界与下确界

上界通常有很多个。其中最小的那个有特殊地位。

**定义** 设 A 上有界。若 A 的全体上界构成的集合有**最小元**，则称这个元素为 A 的**上确界**(supremum)，记

sup(A) := min{ s ∈ X ; s 是 A 的上界 }

对下有界的 A 类似地定义**下确界**(infimum)：

inf(A) := max{ s ∈ X ; s 是 A 的下界 }

A 只有两个元素 A = {a, b} 时，常记 a ∨ b := sup(A)，a ∧ b := inf(A)。

<svg viewBox="0 0 420 210" xmlns="http://www.w3.org/2000/svg">
<rect x="45" y="30" width="150" height="52" rx="6" fill="#979AFF" fill-opacity="0.16" stroke="#5A5FE0" stroke-width="1.2"/>
<text x="120" y="52" font-size="12" text-anchor="middle" fill="#5A5FE0">A 的全体上界</text>
<circle cx="120" cy="70" r="5" fill="#E0612F"/>
<text x="132" y="74" font-size="11" fill="#E0612F">sup(A) = 上界中最小的</text>
<rect x="45" y="120" width="150" height="62" rx="6" fill="#FF7F50" fill-opacity="0.14" stroke="#E0612F" stroke-width="1.2"/>
<text x="120" y="140" font-size="12" text-anchor="middle" fill="#E0612F">A</text>
<circle cx="80" cy="160" r="4" fill="#333"/><circle cx="110" cy="168" r="4" fill="#333"/><circle cx="145" cy="158" r="4" fill="#333"/>
<line x1="120" y1="118" x2="120" y2="88" stroke="#999" stroke-width="1" stroke-dasharray="3,3"/>
<text x="240" y="60" font-size="11" fill="#555">sup 未必属于 A</text>
<text x="240" y="82" font-size="11" fill="#555">若 sup(A) ∈ A，则它就是 max(A)</text>
<text x="240" y="112" font-size="11" fill="#555">max 必须落在 A 内部</text>
<text x="240" y="134" font-size="11" fill="#777">故 max 存在 ⟹ sup 存在且相等</text>
<text x="240" y="154" font-size="11" fill="#777">反之不成立</text>
</svg>

**注（A–E 注 4.5）**

**(a)** 上有界的集合**未必有上确界**。上界集合可能没有最小元。这一点极其要紧——ℝ 之所以区别于 ℚ，正在于它保证了上确界的存在。

**(b)** sup(A) 与 inf(A) 存在时，一般**不属于** A。

**(c)** 若 sup(A) 存在且 sup(A) ∈ A，则 sup(A) = max(A)；inf 同理。

**(d)** 若 max(A) 存在，则 sup(A) = max(A)；若 min(A) 存在，则 inf(A) = min(A)。

(c)(d) 合起来说：**max 与 sup 的差别只在「是否落在 A 内」**。max 存在时二者一致；max 不存在时 sup 仍可能存在。

**例（A–E 例 4.6(a)）** 设 𝒜 是 P(X) 的非空子集（带包含序）。则

sup(𝒜) = ⋃𝒜，  inf(𝒜) = ⋂𝒜

即在包含序下，[[fond_famiglie|任意并]]就是上确界、[[fond_famiglie|任意交]]就是下确界。（并集包含每个成员，故是上界；任何包含所有成员的集合必包含它们的并，故并是最小的上界。交同理。）

## 单调函数与有界函数

**定义** 设 (X, ≤) 与 (Y, ≤) 是偏序集，f : X → Y。称 f

**递增**(increasing)，若 x ≤ y ⟹ f(x) ≤ f(y)；<br>
**递减**(decreasing)，若 x ≤ y ⟹ f(x) ≥ f(y)；<br>
**严格递增**，若 x < y ⟹ f(x) < f(y)；严格递减同理。

递增或递减统称**单调**(monotone)。

**定义** 设 X 是集合，(Y, ≤) 是偏序集。函数 f : X → Y 称**有界**（上有界、下有界），若它的[[fond_funzioni|像]] im(f) 在 Y 中有界（上有界、下有界）。

**例（A–E 例 4.7(a)）** 设 f : X → Y。则[[fond_immagine_preimmagine|命题 3.8]] 的 (i) 与 (i′) 恰好是说：诱导的集值函数

f : P(X) → P(Y)  与  f<sup>−1</sup> : P(Y) → P(X)

在包含序下都是**递增**的（A ⊆ B ⟹ f(A) ⊆ f(B)，B ⊆ B′ ⟹ f<sup>−1</sup>(B) ⊆ f<sup>−1</sup>(B′)）。

## 练习

(a) 在整数集上考虑整除关系：m ≼ n :⟺ m 整除 n（限于正整数，借用整数的算术）。验证它是偏序，并说明它不是全序。

(b) 设 X := {a, b, c}，在 P(X) 上取包含序，A := { {a}, {b} }。求 A 的全部上界、sup(A)，并说明 max(A) 是否存在。

(c) 证明注 4.5(d)：若 max(A) 存在，则 sup(A) 存在且 sup(A) = max(A)。

## 参考解答

**(a)** 记 m ≼ n 为「m 整除 n」，限于正整数。

自反：m 整除 m（m = m·1）✓<br>
传递：m 整除 n ∧ n 整除 l ⟹ n = mk ∧ l = nk′ ⟹ l = m(kk′) ⟹ m 整除 l ✓<br>
反对称：m 整除 n ∧ n 整除 m ⟹ n = mk ∧ m = nk′ ⟹ m = mkk′ ⟹ kk′ = 1 ⟹ k = k′ = 1（正整数）⟹ m = n ✓

故是偏序。**不是全序**：2 与 3 不可比——2 不整除 3，3 也不整除 2。∎

**(b)** 上界是包含 {a} 与 {b} 两者的集合，即包含 {a, b} 的集合：

上界全体 = { {a,b}, {a,b,c} }

其中最小的是 {a, b}，故 **sup(A) = {a, b}**（与例 4.6(a) 一致：sup 是 ⋃A = {a} ∪ {b} = {a,b}）。

**max(A) 不存在**：最大元必须属于 A = { {a}, {b} }，但 {a} 不是上界（不含 {b}），{b} 也不是上界。A 中没有元素是上界，故无最大元。∎

这正是注 4.5 说的情形：**sup 存在而 max 不存在**，因为 sup(A) = {a,b} ∉ A。

**(c)** 记 m := max(A)，S := { s ∈ X ; s 是 A 的上界 }。要证 S 有最小元且等于 m。

**m ∈ S**：由最大元的定义，m 是 A 的上界。

**m 是 S 的下界**：任取 s ∈ S。因 m ∈ A（最大元属于 A）且 s 是 A 的上界，故 m ≤ s。

两条合起来：m ∈ S 且 m ≤ s 对一切 s ∈ S，即 m = min(S) = sup(A)。∎

**注** 证明用到了 m ∈ A 这个条件（第二步）。这正是 max 与 sup 的分界：max 落在 A 内，才能作为 A 的成员被任何上界压住。

## 前瞻

偏序、上界、上确界的定义已就位，但注 4.5(a) 留下一个问题：上有界的集合未必有上确界。哪些序集能保证上确界总存在？这个性质称完备性，是 ℝ 区别于 ℚ 的关键，也是整个分析的基石。届时会看到 ℚ 上有界却无上确界的具体例子，见 [[num_estremo_superiore|上确界与完备性]]。
