---
id: fond_famiglie
label: 集合族与任意并交
parent: fond_fondamenta
prerequisites: [fond_insiemi, fond_quantificatori]
summary: 给一批集合编上名字（指标）后，可对任意多个集合同时取交并：⋂ 由 ∀ 定义、⋃ 由 ∃ 定义，是 ∩ 由 ∧、∪ 由 ∨ 定义的推广。
status: learning
refs: Amann–Escher, Analysis I §I.2
---

## 问题从哪来

[[fond_insiemi|上一节]]定义了两个集合的交 A ∩ B。三个集合也不成问题，写 A ∩ B ∩ C。十个集合，先给它们起名字 A₁, A₂, …, A₁₀，再写

A₁ ∩ A₂ ∩ ⋯ ∩ A₁₀

那么**无穷多个**呢？比如对每个正整数 n 都给定一个集合 Aₙ，想取它们全体的交。写 "A₁ ∩ A₂ ∩ A₃ ∩ ⋯" 是写不完的，省略号也不构成严格定义。

**需要一个新记法——这就是本节的全部目的。** 没有新概念，只是把「有限多次运算」换成「一句话说清所有情形」。

## 先看一个能自己算的例子

取 Aₙ := {1, 2, …, n}，即

A₁ = {1}<br>
A₂ = {1, 2}<br>
A₃ = {1, 2, 3}<br>
A₄ = {1, 2, 3, 4}<br>
⋮

<svg viewBox="0 0 420 190" xmlns="http://www.w3.org/2000/svg">
<text x="30" y="34" font-size="13" fill="#555">A₁</text>
<rect x="55" y="20" width="42" height="22" rx="4" fill="#FF7F50" fill-opacity="0.3" stroke="#E0612F" stroke-width="1.2"/>
<text x="76" y="36" font-size="13" text-anchor="middle" fill="#333">1</text>
<text x="30" y="66" font-size="13" fill="#555">A₂</text>
<rect x="55" y="52" width="84" height="22" rx="4" fill="#FF7F50" fill-opacity="0.22" stroke="#E0612F" stroke-width="1.2"/>
<text x="76" y="68" font-size="13" text-anchor="middle" fill="#333">1</text>
<text x="118" y="68" font-size="13" text-anchor="middle" fill="#333">2</text>
<text x="30" y="98" font-size="13" fill="#555">A₃</text>
<rect x="55" y="84" width="126" height="22" rx="4" fill="#FF7F50" fill-opacity="0.16" stroke="#E0612F" stroke-width="1.2"/>
<text x="76" y="100" font-size="13" text-anchor="middle" fill="#333">1</text>
<text x="118" y="100" font-size="13" text-anchor="middle" fill="#333">2</text>
<text x="160" y="100" font-size="13" text-anchor="middle" fill="#333">3</text>
<text x="30" y="130" font-size="13" fill="#555">A₄</text>
<rect x="55" y="116" width="168" height="22" rx="4" fill="#FF7F50" fill-opacity="0.12" stroke="#E0612F" stroke-width="1.2"/>
<text x="76" y="132" font-size="13" text-anchor="middle" fill="#333">1</text>
<text x="118" y="132" font-size="13" text-anchor="middle" fill="#333">2</text>
<text x="160" y="132" font-size="13" text-anchor="middle" fill="#333">3</text>
<text x="202" y="132" font-size="13" text-anchor="middle" fill="#333">4</text>
<text x="240" y="132" font-size="13" fill="#999">⋯</text>
<line x1="55" y1="150" x2="97" y2="150" stroke="#5A5FE0" stroke-width="2.5"/>
<text x="105" y="155" font-size="12" fill="#5A5FE0">交 = {1}（只有 1 在每一个里）</text>
<line x1="55" y1="174" x2="290" y2="174" stroke="#00A070" stroke-width="2.5"/>
<text x="298" y="179" font-size="12" fill="#00A070">并 = 全体正整数</text>
</svg>

**并**：哪些数**至少**出现在某一个 Aₙ 里？数 k 出现在 A<sub>k</sub> 里（也在之后每一个里）。所以并是全体正整数。

**交**：哪些数出现在**每一个** Aₙ 里？A₁ 只含 1，所以交至多是 {1}；而 1 确实在每个 Aₙ 里。所以交是 {1}。（2 不行——它不在 A₁ 里。）

这两句话就是下面定义要形式化的东西。

## 指标集

上例中 A₁, A₂, A₃, … 的下标 1, 2, 3, … 是给这些集合起的**名字**。把全部名字收集成一个集合，就是**指标集**。

**定义（集合族）** 设 A 是**非空**集合，且对每个 α ∈ A 给定一个集合 A<sub>α</sub>。则

{ A<sub>α</sub> ; α ∈ A }

称一个**集合族**(family of sets)，A 称它的**指标集**(index set)。

集合族就是**一批集合，外加给它们起的名字**。名字不必是数：可以用任意集合的元素当指标，例如「对每个实数 r 给定一个集合 A<sub>r</sub>」，此时指标集是 ℝ。

三点说明：

不要求 α ≠ β 时 A<sub>α</sub> ≠ A<sub>β</sub><br>
（两个不同的名字可以指向同一个集合）

不要求每个 A<sub>α</sub> 非空<br>
（成员可以是 ∅）

集合族本身**永不为空**<br>
（指标集 A 被要求非空，故至少有一个成员。这个要求后面证明里要用到）

## 定义：任意交与任意并

回到两个集合的情形：

x ∈ A ∩ B  意思是  「x ∈ A **并且** x ∈ B」

三个集合：「x 属于 A₁、A₂、A₃ **每一个**」

任意多个：「x 属于**每一个** A<sub>α</sub>」——用量词写就是 **∀α, x ∈ A<sub>α</sub>**

并完全平行：

x ∈ A ∪ B  意思是  「x ∈ A **或者** x ∈ B」

任意多个：「**至少有一个** A<sub>α</sub> 含 x」——用量词写就是 **∃α, x ∈ A<sub>α</sub>**

于是定义（设 { A<sub>α</sub> ; α ∈ A } 是集合 X 的子集族）：

⋂<sub>α</sub> A<sub>α</sub> := { x ∈ X : ∀α ∈ A, x ∈ A<sub>α</sub> }

⋃<sub>α</sub> A<sub>α</sub> := { x ∈ X : ∃α ∈ A, x ∈ A<sub>α</sub> }

两者都是 X 的子集。

**对应关系一览：**

| 两个集合 | 任意多个集合 |
|---|---|
| ∧（并且） | ∀（对所有） |
| ∩ | ⋂ |
| ∨（或者） | ∃（存在） |
| ∪ | ⋃ |

∀ 是 ∧ 的推广，∃ 是 ∨ 的推广。所以 ⋂、⋃ 不是新东西，只是把「并且／或者」换成了「所有／存在」。

用这个定义复核开头的例子：

x ∈ ⋂<sub>n</sub> Aₙ ⟺ ∀n, x ∈ Aₙ

取 x = 2：2 ∉ A₁，故「∀n」不成立，2 不在交里。取 x = 1：1 ∈ Aₙ 对每个 n 成立，故 1 在交里。与手算一致。

**记号** ⋂<sub>α</sub> A<sub>α</sub> 也写作 ⋂<sub>α∈A</sub> A<sub>α</sub>。若把族本身记作 𝒜，还可写 ⋂<sub>A∈𝒜</sub> A 或简记 ⋂𝒜。并同理。

**有限族** 指标集取 {0, 1, …, n} 时写

⋃<sub>j=0</sub><sup>n</sup> A<sub>j</sub>  或  A₀ ∪ ⋯ ∪ Aₙ

与上一节的有限并交一致——**有限情形是本节的特例，不是另一套东西**。

## 无穷带来的新现象

有限个集合做不出来、无穷个才会出现的情况，值得单看。以下取 X = ℝ（ℝ 此处按熟悉的方式借用，严格构造留待后面），指标 n 取遍 n ≥ 1 的正整数。

**(a) Aₙ := [0, 1/n]，则 ⋂<sub>n</sub> Aₙ = {0}。**

<svg viewBox="0 0 440 205" xmlns="http://www.w3.org/2000/svg">
<line x1="35" y1="175" x2="405" y2="175" stroke="#888" stroke-width="1.2"/>
<path d="M 405 175 L 397 171 L 397 179 z" fill="#888"/>
<line x1="60" y1="30" x2="60" y2="182" stroke="#E0612F" stroke-width="1" stroke-dasharray="4,3"/>
<text x="60" y="196" font-size="11" text-anchor="middle" fill="#E0612F">0</text>
<text x="360" y="196" font-size="11" text-anchor="middle" fill="#888">1</text>
<line x1="60" y1="40" x2="360" y2="40" stroke="#5A5FE0" stroke-width="3"/>
<circle cx="60" cy="40" r="3.5" fill="#5A5FE0"/><circle cx="360" cy="40" r="3.5" fill="#5A5FE0"/>
<text x="372" y="44" font-size="11" fill="#5A5FE0">[0,1]</text>
<line x1="60" y1="66" x2="210" y2="66" stroke="#5A5FE0" stroke-width="3"/>
<circle cx="60" cy="66" r="3.5" fill="#5A5FE0"/><circle cx="210" cy="66" r="3.5" fill="#5A5FE0"/>
<text x="222" y="70" font-size="11" fill="#5A5FE0">[0,1/2]</text>
<line x1="60" y1="92" x2="160" y2="92" stroke="#5A5FE0" stroke-width="3"/>
<circle cx="60" cy="92" r="3.5" fill="#5A5FE0"/><circle cx="160" cy="92" r="3.5" fill="#5A5FE0"/>
<text x="172" y="96" font-size="11" fill="#5A5FE0">[0,1/3]</text>
<line x1="60" y1="118" x2="135" y2="118" stroke="#5A5FE0" stroke-width="3"/>
<circle cx="60" cy="118" r="3.5" fill="#5A5FE0"/><circle cx="135" cy="118" r="3.5" fill="#5A5FE0"/>
<text x="147" y="122" font-size="11" fill="#5A5FE0">[0,1/4]</text>
<line x1="60" y1="144" x2="120" y2="144" stroke="#5A5FE0" stroke-width="3"/>
<circle cx="60" cy="144" r="3.5" fill="#5A5FE0"/><circle cx="120" cy="144" r="3.5" fill="#5A5FE0"/>
<text x="132" y="148" font-size="11" fill="#5A5FE0">[0,1/5]</text>
<text x="150" y="163" font-size="11" fill="#999">⋮</text>
<circle cx="60" cy="175" r="4.5" fill="#E0612F"/>
<text x="78" y="167" font-size="11" fill="#E0612F">⋂ = {0}</text>
</svg>

0 属于每个 [0, 1/n]，故 0 在交里。<br>
任何 x > 0：总能取到 n 使 1/n < x，于是 x ∉ [0, 1/n]，故 x 不在交里。<br>
（此处用到阿基米德性质，暂且承认，严格证明留待 [[num_archimede|后面]]）

**(b) Bₙ := (0, 1/n)（开区间），则 ⋂<sub>n</sub> Bₙ = ∅。**

论证与 (a) 相同，差别只在 0 这一点：开区间不含左端点，故 0 ∉ Bₙ 对每个 n 都成立，连 0 也被排除，交为空。

这里出现了有限情形不会有的现象。称一族集合**嵌套**(nested)，若它们依次互相包含：

B₁ ⊇ B₂ ⊇ B₃ ⊇ ⋯

本例的 Bₙ 正是嵌套的（1/n 递减，区间一个比一个小），且每个 Bₙ 都非空。两种情形对比：

**有限多个**嵌套非空集合，交必非空——因为 B₁ ∩ ⋯ ∩ Bₙ 就等于其中最小的那个 Bₙ，而它非空。

**无穷多个**嵌套非空集合，交可以是空集——本例就是。

差别的根源：有限族里必有一个最小的成员，无穷族里可能没有。本例中每个 Bₙ 后面还有更小的 Bₙ₊₁，收缩没有尽头，最终什么也不剩。

**(c) Cₙ := [1/n, 1]，则 ⋃<sub>n</sub> Cₙ = (0, 1]。**

每个 x ∈ (0,1] 落在某个 Cₙ 里（取 n 使 1/n ≤ x）；而 0 不属于任何 Cₙ。

这里同样有一个有限情形没有的现象：每个 Cₙ 都**含它的两个端点**，有限个这样的区间求并，结果仍含两端点；但无穷并 (0,1] 在左端缺了 0。原因还是没有最小的 1/n——左端点一个比一个小，却始终大于 0，于是 0 永远进不来。

(b)(c) 这类现象在后面的拓扑里会正式登场。例如练习 (b) 的 ⋂<sub>n</sub> (−1/n, 1/n) = {0}：每个 (−1/n, 1/n) 都是开区间，交却是单点集，不再是开区间。这正是「开集对任意并封闭，却只对**有限**交封闭」的来由。

## 德摩根律

先看最直观也最常用的一条。它其实就是[[fond_quantificatori|量词否定规则]]换了身记号。

**命题** 设 { A<sub>α</sub> ; α ∈ A } 是 X 的子集族。则

( ⋂<sub>α</sub> A<sub>α</sub> )<sup>c</sup> = ⋃<sub>α</sub> A<sub>α</sub><sup>c</sup>    ( ⋃<sub>α</sub> A<sub>α</sub> )<sup>c</sup> = ⋂<sub>α</sub> A<sub>α</sub><sup>c</sup>

用日常语言读第一式：「**不是**每个 A<sub>α</sub> 都含 x」等价于「**存在某个** A<sub>α</sub> 不含 x」。

**证明**

x ∈ ( ⋂<sub>α</sub> A<sub>α</sub> )<sup>c</sup><br>
⟺ x ∉ ⋂<sub>α</sub> A<sub>α</sub><br>
⟺ ¬ ( ∀α : x ∈ A<sub>α</sub> )<br>
⟺ ∃α : x ∉ A<sub>α</sub><br>
⟺ ∃α : x ∈ A<sub>α</sub><sup>c</sup><br>
⟺ x ∈ ⋃<sub>α</sub> A<sub>α</sub><sup>c</sup><br>
（第 3 步用 ¬∀ ⟺ ∃¬，其余各步只用定义）

第二式同法，用 ¬∃ ⟺ ∀¬。∎

## 分配律（一个集合与一族集合）

实际使用中最频繁的是下面这条：一个固定集合 B 与一族集合作交并。

**命题** 设 { A<sub>α</sub> ; α ∈ A } 是 X 的子集族，B ⊆ X。则

B ∩ ( ⋃<sub>α</sub> A<sub>α</sub> ) = ⋃<sub>α</sub> ( B ∩ A<sub>α</sub> )

B ∪ ( ⋂<sub>α</sub> A<sub>α</sub> ) = ⋂<sub>α</sub> ( B ∪ A<sub>α</sub> )

**证明**（第一式）

x ∈ B ∩ ( ⋃<sub>α</sub> A<sub>α</sub> )<br>
⟺ x ∈ B ∧ ( ∃α : x ∈ A<sub>α</sub> )<br>
⟺ ∃α : ( x ∈ B ∧ x ∈ A<sub>α</sub> )<br>
⟺ ∃α : x ∈ B ∩ A<sub>α</sub><br>
⟺ x ∈ ⋃<sub>α</sub> ( B ∩ A<sub>α</sub> )<br>
（第 3 步把 x ∈ B 移进 ∃ 的辖域：这一步合法是因为条件 x ∈ B **不含被量化的变元 α**）

第二式同法。∎

**注** 「与量词变元无关的条件可以自由进出量词辖域」是常用的一步，但前提必须核对：条件里不能出现 α。

## 一般形式（A–E 命题 2.7）

最后是两族集合同时参与的一般版本。先读懂它说什么，再看证明。

**命题（A–E 命题 2.7）** 设 { A<sub>α</sub> ; α ∈ A } 与 { B<sub>β</sub> ; β ∈ B } 是 X 的子集族，(α, β) 取遍 A × B。则

**(i)（结合律）**

( ⋂<sub>α</sub> A<sub>α</sub> ) ∩ ( ⋂<sub>β</sub> B<sub>β</sub> ) = ⋂<sub>(α,β)</sub> ( A<sub>α</sub> ∩ B<sub>β</sub> )

( ⋃<sub>α</sub> A<sub>α</sub> ) ∪ ( ⋃<sub>β</sub> B<sub>β</sub> ) = ⋃<sub>(α,β)</sub> ( A<sub>α</sub> ∪ B<sub>β</sub> )

**(ii)（分配律）**

( ⋂<sub>α</sub> A<sub>α</sub> ) ∪ ( ⋂<sub>β</sub> B<sub>β</sub> ) = ⋂<sub>(α,β)</sub> ( A<sub>α</sub> ∪ B<sub>β</sub> )

( ⋃<sub>α</sub> A<sub>α</sub> ) ∩ ( ⋃<sub>β</sub> B<sub>β</sub> ) = ⋃<sub>(α,β)</sub> ( A<sub>α</sub> ∩ B<sub>β</sub> )

**(i) 第一式怎么读**：左边是「先把所有 A 交起来、再把所有 B 交起来、最后两者取交」；右边是「把每一对 A<sub>α</sub> ∩ B<sub>β</sub> 都取出来、再全部交起来」。两边都表达同一件事——x 同时属于所有的 A 和所有的 B。

**证明 (i) 第一式**

**⊆：**

x ∈ ( ⋂<sub>α</sub> A<sub>α</sub> ) ∩ ( ⋂<sub>β</sub> B<sub>β</sub> )<br>
⟹ ( ∀α : x ∈ A<sub>α</sub> ) ∧ ( ∀β : x ∈ B<sub>β</sub> )<br>
⟹ ∀(α,β) : x ∈ A<sub>α</sub> ∧ x ∈ B<sub>β</sub><br>
⟹ ∀(α,β) : x ∈ A<sub>α</sub> ∩ B<sub>β</sub><br>
⟹ x ∈ ⋂<sub>(α,β)</sub> ( A<sub>α</sub> ∩ B<sub>β</sub> )

**⊇：** 设 x ∈ ⋂<sub>(α,β)</sub> ( A<sub>α</sub> ∩ B<sub>β</sub> )，即 ∀(α,β) : x ∈ A<sub>α</sub> ∧ x ∈ B<sub>β</sub>。

固定任一 β₀ ∈ B，让 α 跑遍 A ⟹ ∀α : x ∈ A<sub>α</sub> ⟹ x ∈ ⋂<sub>α</sub> A<sub>α</sub><br>
固定任一 α₀ ∈ A，让 β 跑遍 B ⟹ ∀β : x ∈ B<sub>β</sub> ⟹ x ∈ ⋂<sub>β</sub> B<sub>β</sub>

故 x 属于两者之交。∎

**注** ⊇ 这一步要「固定某个 β₀ ∈ B」，**这里用到了指标集非空**。若 B 允许为空，A × B 也为空，右端成了空指标上的交，等式会失效。这就是定义中要求指标集非空的原因。

**证明 (ii) 第一式**

**⊆：** 设 x ∈ ( ⋂<sub>α</sub> A<sub>α</sub> ) ∪ ( ⋂<sub>β</sub> B<sub>β</sub> )，分两种情形。

若 ∀α : x ∈ A<sub>α</sub>，则任给 (α,β) 有 x ∈ A<sub>α</sub> ⊆ A<sub>α</sub> ∪ B<sub>β</sub><br>
若 ∀β : x ∈ B<sub>β</sub>，则任给 (α,β) 有 x ∈ B<sub>β</sub> ⊆ A<sub>α</sub> ∪ B<sub>β</sub>

两种情形都得 ∀(α,β) : x ∈ A<sub>α</sub> ∪ B<sub>β</sub>。

**⊇：** 这个方向必须用反证。设 x ∈ ⋂<sub>(α,β)</sub> ( A<sub>α</sub> ∪ B<sub>β</sub> )，反设 x 不属于左端，则

¬( ∀α : x ∈ A<sub>α</sub> ) ∧ ¬( ∀β : x ∈ B<sub>β</sub> )<br>
⟹ ( ∃α₀ : x ∉ A<sub>α₀</sub> ) ∧ ( ∃β₀ : x ∉ B<sub>β₀</sub> )<br>
（用 ¬∀ ⟺ ∃¬）

取这一对 (α₀, β₀)：x ∉ A<sub>α₀</sub> 且 x ∉ B<sub>β₀</sub>，故 x ∉ A<sub>α₀</sub> ∪ B<sub>β₀</sub>。但假设说 x 属于**每一对**指标处的并，矛盾。∎

**注** 这里为什么必须反证：由「每一对 (α,β) 处 x 落在 A<sub>α</sub> 或 B<sub>β</sub> 之中」无法逐对地选出统一的一侧。反证法把两侧各自的失败点 α₀ 与 β₀ **配成一对**，矛盾才浮现。这个「取一对反例指标」的手法处理双指标问题时常用。

## 练习

(a) 取 Aₙ := {n, n+1, n+2, …}（n ≥ 1 的正整数）。求 ⋂<sub>n</sub> Aₙ 与 ⋃<sub>n</sub> Aₙ。

(b) 取 Aₙ := (−1/n, 1/n)。求 ⋂<sub>n</sub> Aₙ。

(c) 证明命题 2.7(i) 的第二式：( ⋃<sub>α</sub> A<sub>α</sub> ) ∪ ( ⋃<sub>β</sub> B<sub>β</sub> ) = ⋃<sub>(α,β)</sub> ( A<sub>α</sub> ∪ B<sub>β</sub> )。

## 参考解答

**(a)** A₁ = {1,2,3,…}，A₂ = {2,3,4,…}，A₃ = {3,4,5,…}，…

**并** = A₁ = 全体正整数。因为 A₁ 已经最大，且每个 Aₙ ⊆ A₁。

**交** = ∅。设 k 是正整数，则 k ∉ A<sub>k+1</sub>（A<sub>k+1</sub> 从 k+1 起），故 k 不在交里。任何正整数都被排除，交为空。∎

**(b)** ⋂<sub>n</sub> Aₙ = {0}。

0 ∈ (−1/n, 1/n) 对每个 n 成立，故 0 在交里。<br>
若 x ≠ 0，取 n 使 1/n < |x|，则 x ∉ (−1/n, 1/n)，故 x 不在交里。<br>
（阿基米德性质，暂且承认）∎

**(c)** 

**⊆：** 设 x ∈ ( ⋃<sub>α</sub> A<sub>α</sub> ) ∪ ( ⋃<sub>β</sub> B<sub>β</sub> )，分两种情形。

若 ∃α₀ : x ∈ A<sub>α₀</sub>，任取 β₀ ∈ B（B 非空），则 x ∈ A<sub>α₀</sub> ∪ B<sub>β₀</sub>，故 x 属于右端的并。<br>
若 ∃β₀ : x ∈ B<sub>β₀</sub>，任取 α₀ ∈ A，同理。

**⊇：** 设 x ∈ ⋃<sub>(α,β)</sub> ( A<sub>α</sub> ∪ B<sub>β</sub> )，即 ∃(α₀,β₀) : x ∈ A<sub>α₀</sub> ∪ B<sub>β₀</sub>。

则 x ∈ A<sub>α₀</sub> 或 x ∈ B<sub>β₀</sub>；前者给出 x ∈ ⋃<sub>α</sub> A<sub>α</sub>，后者给出 x ∈ ⋃<sub>β</sub> B<sub>β</sub>。两种情形都落在左端。∎

**注** ⊆ 方向也用到了指标集非空（需要「任取 β₀ ∈ B」才能凑出一对指标）。

## 前瞻

任意并交是此后处处要用的记法：[[fond_immagine_preimmagine|像与原像]]对集合运算的行为、以及后面拓扑中「开集对任意并封闭、只对有限交封闭」的表述，都建立在本节之上。A–E §I.2 的内容至此完整。下一步转向[[fond_relazioni|有序对与关系]]，为把「对应」化归为集合作准备。
