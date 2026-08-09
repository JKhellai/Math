---
id: fond_insiemi
label: 集合
parent: fond_fondamenta
prerequisites: [fond_proposizioni, fond_quantificatori]
summary: 集合由其元素决定（外延原则）；交、并、补是逻辑联结词 ∧、∨、¬ 抬到属于关系上的产物，故集合恒等式全部归结为逻辑等价。幂集 P(X) 收集 X 的一切子集。
status: learning
refs: Amann–Escher, Analysis I §I.2
---

[[fond_quantificatori|量词]]中的 ∀x、∃x 总要取遍某个范围，之前只含糊称之为「论域」。本节把这个范围本身作为对象来处理，即**集合**。此后每个数学对象都将被装在某个集合中来谈。

## 集合与属于

**集合**(set)是把若干对象看作一个整体，这些对象称它的**元素**(element)。最基本的关系是**属于**(membership)，记 x ∈ A，其否定记 x ∉ A。

∈ 不再往下定义，与逻辑联结词一样是这一层的原始概念。

写出具体集合有两种方式：

- **列举**：A := {0, 1, 2}。<br>
- **描述**：从**已有**集合 A 中挑出满足谓词 P 的元素，记 { x ∈ A : P(x) }，例如 { x ∈ ℝ : x > 3 }。

**注** 描述式必须从一个已有集合中切取。无限制地写 { x : P(x) }（对一切满足 P 的对象一网打尽）会导致矛盾（罗素悖论），严格的处理留待后面。

## 外延原则

**定义（外延原则）** 

A = B  :⟺  ∀x ( x ∈ A ⟺ x ∈ B )

集合由其成员完全决定：与元素的排列次序、书写重复次数、描述方式均无关。故 {0,1,2} = {2,1,0} = {0,0,1,2}。

## 子集

**定义（子集）** 

A ⊆ B  :⟺  ∀x ( x ∈ A ⟹ x ∈ B )

**命题** A = B ⟺ ( A ⊆ B ∧ B ⊆ A )。

**证明** 

A = B<br>
 ⟺ ∀x ( x ∈ A ⟺ x ∈ B )<br>
 ⟺ ∀x ( (x ∈ A ⟹ x ∈ B) ∧ (x ∈ B ⟹ x ∈ A) )<br>
 ⟺ ∀x (x ∈ A ⟹ x ∈ B) ∧ ∀x (x ∈ B ⟹ x ∈ A)<br>
 ⟺ A ⊆ B ∧ B ⊆ A<br>
（第 2 步用[[fond_proposizioni|p ⟺ q 等价于 (p⟹q) ∧ (q⟹p)]]；第 3 步用 ∀ 对 ∧ 可分配）∎

证集合相等的标准做法由此确定：**分别证两个方向的包含**。

## 交、并、差、补

设 A, B 是集合 X 的子集。定义

x ∈ A ∪ B  :⟺  x ∈ A ∨ x ∈ B  （**并** union）

x ∈ A ∩ B  :⟺  x ∈ A ∧ x ∈ B  （**交** intersection）

x ∈ A ∖ B  :⟺  x ∈ A ∧ x ∉ B  （**差**，B 在 A 中的**相对补**）

当全集 X 由上下文确定时，记

Aᶜ := X ∖ A  （A 的**补集** complement）

三种运算就是[[fond_proposizioni|联结词]] ∨、∧、¬ 抬到 ∈ 上的产物。由此得

A ∖ B = A ∩ Bᶜ<br>
（两边的成员条件都是 x ∈ A ∧ x ∉ B）

**定义（不相交）** A ∩ B = ∅ 时称 A 与 B **不相交**(disjoint)。

<svg viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg">
  <rect x="20" y="20" width="360" height="170" fill="none" stroke="#999" stroke-width="1.2"/>
  <text x="32" y="38" font-size="13" fill="#555">X</text>
  <circle cx="160" cy="105" r="70" fill="#FF7F50" fill-opacity="0.22" stroke="#E0612F" stroke-width="1.5"/>
  <circle cx="240" cy="105" r="70" fill="#979AFF" fill-opacity="0.22" stroke="#5A5FE0" stroke-width="1.5"/>
  <text x="112" y="110" font-size="18" text-anchor="middle" fill="#333">A</text>
  <text x="288" y="110" font-size="18" text-anchor="middle" fill="#333">B</text>
  <text x="200" y="110" font-size="12" text-anchor="middle" fill="#333">A∩B</text>
  <text x="130" y="176" font-size="11" text-anchor="middle" fill="#E0612F">A∖B</text>
  <text x="55" y="170" font-size="11" fill="#555">(A∪B)ᶜ</text>
</svg>

## 交与并的代数律

**命题（A–E 命题 2.4）** 设 X, Y, Z 是某集合的子集。则

(i) X ∪ Y = Y ∪ X，  X ∩ Y = Y ∩ X  （交换律）

(ii) X ∪ (Y ∪ Z) = (X ∪ Y) ∪ Z，  X ∩ (Y ∩ Z) = (X ∩ Y) ∩ Z  （结合律）

(iii) X ∪ (Y ∩ Z) = (X ∪ Y) ∩ (X ∪ Z)，  X ∩ (Y ∪ Z) = (X ∩ Y) ∪ (X ∩ Z)  （分配律）

(iv) X ⊆ Y  ⟺  X ∪ Y = Y  ⟺  X ∩ Y = X

**证明** (i)(ii)(iii) 都由外延原则化归为对应的逻辑等价。以 (iii) 的第二式为例：

x ∈ X ∩ (Y ∪ Z)<br>
⟺ x ∈ X ∧ (x ∈ Y ∨ x ∈ Z)<br>
⟺ (x ∈ X ∧ x ∈ Y) ∨ (x ∈ X ∧ x ∈ Z)<br>
⟺ x ∈ (X ∩ Y) ∪ (X ∩ Z)<br>
（第 2 步用 ∧ 对 ∨ 的[[fond_proposizioni|分配律]]，可由真值表验证；其余各步只用定义）

对一切 x 成立，故两集合相等。其余各式同法。

(iv) 按 X ⊆ Y ⟹ X ∪ Y = Y ⟹ X ∩ Y = X ⟹ X ⊆ Y 的顺序证一圈。

**X ⊆ Y ⟹ X ∪ Y = Y：**

x ∈ X ∪ Y ⟹ x ∈ X ∨ x ∈ Y ⟹ x ∈ Y<br>
（若 x ∈ X，由 X ⊆ Y 得 x ∈ Y；两种情形都落在 Y 中，故 X ∪ Y ⊆ Y）

Y ⊆ X ∪ Y<br>
（并的定义直接给出）

两向包含得 X ∪ Y = Y。

**X ∪ Y = Y ⟹ X ∩ Y = X：**

X ⊆ X ∪ Y = Y ⟹ X ⊆ Y

x ∈ X ∩ Y ⟹ x ∈ X<br>
（交的定义，得 X ∩ Y ⊆ X）

x ∈ X ⟹ x ∈ X ∧ x ∈ Y ⟹ x ∈ X ∩ Y<br>
（第 1 步用刚得到的 X ⊆ Y，得 X ⊆ X ∩ Y）

**X ∩ Y = X ⟹ X ⊆ Y：**

x ∈ X = X ∩ Y ⟹ x ∈ Y ∎

## 空集

**定义** 不含任何元素的集合称**空集**(empty set)，记 ∅。

**命题** ∀A : ∅ ⊆ A。

**证明** 

∅ ⊆ A ⟺ ∀x ( x ∈ ∅ ⟹ x ∈ A )

x ∈ ∅ 恒假 ⟹ 蕴含式恒真<br>
（前件为假时[[fond_proposizioni|蕴含]]自动成立）∎

## 幂集

**定义（幂集）** 设 X 是集合。X 的一切子集构成的集合称 X 的**幂集**(power set)，记 P(X)，有时也记 2ˣ。

Y ∈ P(X)  ⟺  Y ⊆ X

由定义直接得到几条事实：

∅ ∈ P(X)  ∧  X ∈ P(X)<br>
（∅ 与 X 都是 X 的子集）

x ∈ X ⟺ {x} ∈ P(X)

P(X) ≠ ∅<br>
（至少含 ∅ 一个元素，即使 X = ∅）

**注** 幂集的元素本身是集合。区分 x ∈ X 与 {x} ⊆ X：前者说 x 是元素，后者说单元素集是子集；对应地 {x} ∈ P(X) 而一般 x ∉ P(X)。

**例** 

P(∅) = { ∅ }<br>
（∅ 唯一的子集是 ∅ 自己。注意 P(∅) 含一个元素，不是空集）

P({∅}) = { ∅, {∅} }

P({a, b}) = { ∅, {a}, {b}, {a, b} }

**例（P({a,b,c})）** 按元素个数分层排列，共 8 个子集：

<svg viewBox="0 0 380 300" xmlns="http://www.w3.org/2000/svg">
  <line x1="190" y1="240" x2="80" y2="185" stroke="#aaa" stroke-width="1"/>
  <line x1="190" y1="240" x2="190" y2="185" stroke="#aaa" stroke-width="1"/>
  <line x1="190" y1="240" x2="300" y2="185" stroke="#aaa" stroke-width="1"/>
  <line x1="80" y1="170" x2="80" y2="115" stroke="#aaa" stroke-width="1"/>
  <line x1="80" y1="170" x2="190" y2="115" stroke="#aaa" stroke-width="1"/>
  <line x1="190" y1="170" x2="80" y2="115" stroke="#aaa" stroke-width="1"/>
  <line x1="190" y1="170" x2="300" y2="115" stroke="#aaa" stroke-width="1"/>
  <line x1="300" y1="170" x2="190" y2="115" stroke="#aaa" stroke-width="1"/>
  <line x1="300" y1="170" x2="300" y2="115" stroke="#aaa" stroke-width="1"/>
  <line x1="80" y1="100" x2="190" y2="50" stroke="#aaa" stroke-width="1"/>
  <line x1="190" y1="100" x2="190" y2="50" stroke="#aaa" stroke-width="1"/>
  <line x1="300" y1="100" x2="190" y2="50" stroke="#aaa" stroke-width="1"/>
  <text x="190" y="252" font-size="13" text-anchor="middle" fill="#333">∅</text>
  <text x="80" y="182" font-size="13" text-anchor="middle" fill="#333">{a}</text>
  <text x="190" y="182" font-size="13" text-anchor="middle" fill="#333">{b}</text>
  <text x="300" y="182" font-size="13" text-anchor="middle" fill="#333">{c}</text>
  <text x="80" y="112" font-size="13" text-anchor="middle" fill="#333">{a,b}</text>
  <text x="190" y="112" font-size="13" text-anchor="middle" fill="#333">{a,c}</text>
  <text x="300" y="112" font-size="13" text-anchor="middle" fill="#333">{b,c}</text>
  <text x="190" y="46" font-size="13" text-anchor="middle" fill="#333">{a,b,c}</text>
  <text x="352" y="252" font-size="10" fill="#999">0 元</text>
  <text x="352" y="182" font-size="10" fill="#999">1 元</text>
  <text x="352" y="112" font-size="10" fill="#999">2 元</text>
  <text x="352" y="46" font-size="10" fill="#999">3 元</text>
  <text x="30" y="285" font-size="11" fill="#777">连线表示 ⊆（下含于上）；共 2³ = 8 个子集</text>
</svg>

一般地，X 含 n 个元素时 P(X) 含 2ⁿ 个元素（每个元素独立地选择「取或不取」）。这也是记号 2ˣ 的来由。严格证明需要[[fond_cardinalita|计数]]，留待后面。

## 关于「集合」一词

**注（A–E 注 2.8）** 本节没有定义什么是「集合」。「集合」与「元素」是数学的**原始概念**(undefined concept)，不加定义，只规定使用规则。这些规则即**公理**——本节及后续各节中未给出证明的关于集合的陈述，可视为公理。例如「一个集合的幂集仍是集合」就是这样一条公理。

集合与元素「是什么」不重要，重要的是处理它们的规则。公理化集合论的完整讨论不在本书范围内。

## 练习

(a) 证明包含的传递性：X ⊆ Y ∧ Y ⊆ Z ⟹ X ⊆ Z。

(b) 验证命题 2.4(iii) 的第一式：X ∪ (Y ∩ Z) = (X ∪ Y) ∩ (X ∪ Z)。

(c) 写出 P({1, 2}) 的全部元素，并判断下列各式真假：<br>
 ① {1} ∈ P({1,2})　② {1} ⊆ P({1,2})　③ ∅ ∈ P({1,2})　④ ∅ ⊆ P({1,2})

## 参考解答

**(a)** 

x ∈ X ⟹ x ∈ Y ⟹ x ∈ Z<br>
（第 1 步用 X ⊆ Y，第 2 步用 Y ⊆ Z）

对一切 x 成立，故 X ⊆ Z。∎

**(b)** 

x ∈ X ∪ (Y ∩ Z)<br>
 ⟺ x ∈ X ∨ (x ∈ Y ∧ x ∈ Z)<br>
 ⟺ (x ∈ X ∨ x ∈ Y) ∧ (x ∈ X ∨ x ∈ Z)<br>
 ⟺ x ∈ (X ∪ Y) ∩ (X ∪ Z)<br>
（第 2 步用 ∨ 对 ∧ 的分配律）

对一切 x 成立，故两集合相等。∎

**(c)** P({1,2}) = { ∅, {1}, {2}, {1,2} }，共 2² = 4 个元素。

① **真**。{1} 是 {1,2} 的子集，故作为元素属于幂集。

② **假**。{1} ⊆ P({1,2}) 要求 {1} 的每个元素都属于 P({1,2})，即要求 1 ∈ P({1,2})。但 P({1,2}) 的元素都是集合，1 不是其中之一。（把 ② 改成 {{1}} ⊆ P({1,2}) 则为真。）

③ **真**。∅ ⊆ {1,2}，故 ∅ ∈ P({1,2})。

④ **真**。∅ 是任何集合的子集。

①②对照说明：**∈ 与 ⊆ 不可混用**；幂集的元素是集合，这一层区别在此最容易出错。∎

## 前瞻

上面的交与并都只对两个集合定义。若要对任意多个集合同时取交、取并（例如无穷多个），需要用一个**指标集**来标记它们，得到集合族的概念，交与并的代数律也随之推广。见 [[fond_famiglie|集合族与任意并交]]。
