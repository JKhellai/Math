---
id: num_n
label: Peano 公理与自然数
parent: num_costruzioni
prerequisites: [fond_funzioni, fond_iniettive_suriettive, fond_insiemi]
summary: 自然数由三元组 (ℕ, 0, ν) 刻画，ν : ℕ → ℕ∖{0} 是后继函数，只需两条公理：(N0) ν 单射，(N1) 含 0 且对 ν 封闭的子集必是 ℕ 全体。(N1) 即归纳原理。
status: learning
refs: Amann–Escher, Analysis I §I.5
---

此前各节谈到 ℝ、ℕ 时都标明「按熟悉的方式借用」。从本节起偿还这笔账：先用公理刻画自然数，随后逐级构造 ℤ、ℚ、ℝ、ℂ。

自然数的核心特征只有一条：**每个自然数后面都紧跟着下一个**。Peano 的公理系统把这句话形式化。

## 需要哪些数据

刻画自然数需要三样东西：

一个集合 **ℕ**<br>
一个特定元素 **0 ∈ ℕ**<br>
一个函数 **ν : ℕ → ℕ<sup>×</sup>**，其中 ℕ<sup>×</sup> := ℕ ∖ {0}

ν(n) 称 n 的**后继**(successor)，ν 称**后继函数**(successor function)。

**注意 ν 的到达域是 ℕ<sup>×</sup> 而不是 ℕ。** 这不是笔误：ℕ<sup>×</sup> 已经把 0 排除在外，所以「ν(n) = 0 永不发生」已经写进了函数的[[fond_funzioni|到达域]]里，不必再单列一条公理。许多教材把「0 不是任何数的后继」写成独立的公理，A–E 用到达域来承担这件事，效果相同。

<svg viewBox="0 0 420 130" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="na" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#5A5FE0"/>
</marker>
</defs>
<circle cx="55" cy="70" r="15" fill="#FF7F50" fill-opacity="0.3" stroke="#E0612F" stroke-width="1.5"/>
<text x="55" y="75" font-size="13" text-anchor="middle" fill="#333">0</text>
<circle cx="125" cy="70" r="15" fill="none" stroke="#5A5FE0" stroke-width="1.3"/>
<text x="125" y="75" font-size="13" text-anchor="middle" fill="#333">1</text>
<circle cx="195" cy="70" r="15" fill="none" stroke="#5A5FE0" stroke-width="1.3"/>
<text x="195" y="75" font-size="13" text-anchor="middle" fill="#333">2</text>
<circle cx="265" cy="70" r="15" fill="none" stroke="#5A5FE0" stroke-width="1.3"/>
<text x="265" y="75" font-size="13" text-anchor="middle" fill="#333">3</text>
<circle cx="335" cy="70" r="15" fill="none" stroke="#5A5FE0" stroke-width="1.3"/>
<text x="335" y="75" font-size="13" text-anchor="middle" fill="#333">4</text>
<text x="375" y="75" font-size="14" fill="#999">⋯</text>
<line x1="70" y1="70" x2="110" y2="70" stroke="#5A5FE0" stroke-width="1.4" marker-end="url(#na)"/>
<line x1="140" y1="70" x2="180" y2="70" stroke="#5A5FE0" stroke-width="1.4" marker-end="url(#na)"/>
<line x1="210" y1="70" x2="250" y2="70" stroke="#5A5FE0" stroke-width="1.4" marker-end="url(#na)"/>
<line x1="280" y1="70" x2="320" y2="70" stroke="#5A5FE0" stroke-width="1.4" marker-end="url(#na)"/>
<text x="90" y="60" font-size="11" text-anchor="middle" fill="#5A5FE0">ν</text>
<text x="55" y="105" font-size="10" text-anchor="middle" fill="#E0612F">无箭头射入</text>
<text x="55" y="30" font-size="10" text-anchor="middle" fill="#E0612F">起点</text>
</svg>

## 两条公理

**(N0)** ν 是[[fond_iniettive_suriettive|单射]]。

**(N1)** 若 ℕ 的子集 N 满足<br>
 　0 ∈ N，且<br>
 　∀n ∈ N : ν(n) ∈ N，<br>
 则 N = ℕ。

满足这两条的三元组 (ℕ, 0, ν) 就称一个自然数系统。

**(N0) 在说什么**：不同的数有不同的后继。若 ν(m) = ν(n)，则 m = n。

**(N1) 在说什么**：ℕ 里没有多余的元素。任何「含 0 且一走到底都不漏」的子集，必然就是 ℕ 全体——换言之，**从 0 出发反复取后继，能走遍 ℕ 的每一个元素**。

## 两条公理各自拦截什么

只有把两条都写上，(ℕ, 0, ν) 才真的是自然数。下面各给一个具体的反例，说明去掉任何一条会漏进什么。

**反例 A：满足 (N1) 而不满足 (N0)。** 取

ℕ<sub>A</sub> := {0, 1, 2, 3}，  ν(0) = 1，ν(1) = 2，ν(2) = 3，ν(3) = 1

<svg viewBox="0 0 420 190" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="nb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#B33"/>
</marker>
</defs>
<circle cx="50" cy="95" r="15" fill="#FF7F50" fill-opacity="0.3" stroke="#E0612F" stroke-width="1.5"/>
<text x="50" y="100" font-size="13" text-anchor="middle" fill="#333">0</text>
<circle cx="138" cy="95" r="15" fill="none" stroke="#B33" stroke-width="1.3"/>
<text x="138" y="100" font-size="13" text-anchor="middle" fill="#333">1</text>
<circle cx="216" cy="50" r="15" fill="none" stroke="#B33" stroke-width="1.3"/>
<text x="216" y="55" font-size="13" text-anchor="middle" fill="#333">2</text>
<circle cx="216" cy="140" r="15" fill="none" stroke="#B33" stroke-width="1.3"/>
<text x="216" y="145" font-size="13" text-anchor="middle" fill="#333">3</text>
<line x1="65" y1="95" x2="123" y2="95" stroke="#B33" stroke-width="1.4" marker-end="url(#nb)"/>
<line x1="150" y1="87" x2="204" y2="60" stroke="#B33" stroke-width="1.4" marker-end="url(#nb)"/>
<line x1="216" y1="65" x2="216" y2="125" stroke="#B33" stroke-width="1.4" marker-end="url(#nb)"/>
<line x1="204" y1="132" x2="150" y2="105" stroke="#B33" stroke-width="1.4" marker-end="url(#nb)"/>
<text x="250" y="70" font-size="11" fill="#B33">ν(0) = 1 = ν(3)</text>
<text x="250" y="92" font-size="11" fill="#B33">两个不同的数后继相同</text>
<text x="250" y="114" font-size="11" fill="#B33">⟹ ν 非单射，(N0) 失败</text>
<text x="250" y="140" font-size="11" fill="#777">但 (N1) 仍然成立</text>
</svg>

验证 (N1) 成立：设 N ⊆ ℕ<sub>A</sub>，0 ∈ N，且对 ν 封闭。

0 ∈ N ⟹ ν(0) = 1 ∈ N ⟹ ν(1) = 2 ∈ N ⟹ ν(2) = 3 ∈ N<br>
⟹ N = {0,1,2,3} = ℕ<sub>A</sub>

验证 (N0) 失败：ν(0) = 1 = ν(3)，而 0 ≠ 3，故 ν 非单射。

这个模型只有四个元素、绕成一个圈，显然不是自然数。**(N0) 的作用正是禁止这种绕回来的结构**：若 ν 单射，则一旦某个数的后继回到已出现过的数，就会出现两个不同的数共用一个后继。

**反例 B：满足 (N0) 而不满足 (N1)。** 在通常的 0, 1, 2, 3, … 之外，另添两个元素 a、b，规定

ν(a) = b，  ν(b) = a

<svg viewBox="0 0 420 175" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="nc" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#5A5FE0"/>
</marker>
<marker id="nd" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#B33"/>
</marker>
</defs>
<circle cx="50" cy="50" r="14" fill="#FF7F50" fill-opacity="0.3" stroke="#E0612F" stroke-width="1.4"/>
<text x="50" y="55" font-size="12" text-anchor="middle" fill="#333">0</text>
<circle cx="115" cy="50" r="14" fill="none" stroke="#5A5FE0" stroke-width="1.2"/>
<text x="115" y="55" font-size="12" text-anchor="middle" fill="#333">1</text>
<circle cx="180" cy="50" r="14" fill="none" stroke="#5A5FE0" stroke-width="1.2"/>
<text x="180" y="55" font-size="12" text-anchor="middle" fill="#333">2</text>
<circle cx="245" cy="50" r="14" fill="none" stroke="#5A5FE0" stroke-width="1.2"/>
<text x="245" y="55" font-size="12" text-anchor="middle" fill="#333">3</text>
<text x="285" y="55" font-size="13" fill="#999">⋯</text>
<line x1="64" y1="50" x2="101" y2="50" stroke="#5A5FE0" stroke-width="1.3" marker-end="url(#nc)"/>
<line x1="129" y1="50" x2="166" y2="50" stroke="#5A5FE0" stroke-width="1.3" marker-end="url(#nc)"/>
<line x1="194" y1="50" x2="231" y2="50" stroke="#5A5FE0" stroke-width="1.3" marker-end="url(#nc)"/>
<text x="150" y="30" font-size="10" text-anchor="middle" fill="#5A5FE0">从 0 出发能走到的部分</text>
<circle cx="115" cy="130" r="14" fill="none" stroke="#B33" stroke-width="1.4"/>
<text x="115" y="135" font-size="12" text-anchor="middle" fill="#333">a</text>
<circle cx="205" cy="130" r="14" fill="none" stroke="#B33" stroke-width="1.4"/>
<text x="205" y="135" font-size="12" text-anchor="middle" fill="#333">b</text>
<path d="M 128 123 A 40 40 0 0 1 192 123" fill="none" stroke="#B33" stroke-width="1.3" marker-end="url(#nd)"/>
<path d="M 192 137 A 40 40 0 0 1 128 137" fill="none" stroke="#B33" stroke-width="1.3" marker-end="url(#nd)"/>
<text x="250" y="125" font-size="11" fill="#B33">a、b 自成一个二元环</text>
<text x="250" y="147" font-size="11" fill="#B33">从 0 永远走不到 ⟹ (N1) 失败</text>
</svg>

验证 (N0) 成立：ν 在 0,1,2,3,… 上单射；ν(a) = b、ν(b) = a 也互不相同，且 a、b 不是链上任何元素的后继。整体仍是单射。

验证 (N1) 失败：取 N := {0, 1, 2, 3, …}（只含链的部分）。则 0 ∈ N，且 N 对 ν 封闭（链上每个元素的后继仍在链上）。但 N ≠ ℕ<sub>B</sub>，因为 a、b 不在 N 中。

这个模型里多出了一段「从 0 走不到」的部分。**(N1) 的作用正是禁止这种多余的部分**：它要求 ℕ 恰好由「从 0 出发反复取后继」所得到的元素组成，一个不多。

**两条公理各司其职**：(N0) 禁止绕回，(N1) 禁止多余。

## 0 是唯一不是后继的元素

**命题（A–E 注 5.1(a)）** ν : ℕ → ℕ<sup>×</sup> 是[[fond_iniettive_suriettive|满射]]，从而（连同 (N0)）是双射。

换言之：**除 0 之外，每个自然数都恰好是某一个自然数的后继**。

**证明** 令

N := im(ν) ∪ {0}

即「一切后继」连同 0。要证 N = ℕ，用 (N1)，需验两件事。

**0 ∈ N**：由 N 的定义，0 被直接放了进去。

**N 对 ν 封闭**：任取 n ∈ N，则 ν(n) 是某个元素的后继（即 n 的后继），故

ν(n) ∈ im(ν) ⊆ N

（这里不需要 n ∈ N 这个条件的任何特殊性质——对**任何** n ∈ ℕ 都有 ν(n) ∈ im(ν)。）

由 (N1) 得 N = ℕ，即

im(ν) ∪ {0} = ℕ

两边去掉 0。因 ν 的到达域是 ℕ<sup>×</sup> = ℕ ∖ {0}，故 0 ∉ im(ν)，于是

im(ν) = ℕ ∖ {0} = ℕ<sup>×</sup>

这正是 ν : ℕ → ℕ<sup>×</sup> 满射。再由 (N0) 单射，ν 是双射。∎

## 记号

**（A–E 注 5.1(b)）** 通常把

0，ν(0)，ν(ν(0))，ν(ν(ν(0)))，…

依次记作 0, 1, 2, 3, …。即 1 := ν(0)，2 := ν(1)，3 := ν(2)，依此类推。

**（A–E 注 5.1(c)）** 有些教材让自然数从 1 而非 0 开始。这只是约定的差别，没有数学上的实质区别。本书从 0 开始。

## 归纳原理

公理 (N1) 是关于**子集**的陈述。实际证明时用的是它关于**命题**的等价形式。

**命题（归纳原理，基本形式）** 设对每个 n ∈ ℕ 给定一个[[fond_proposizioni|命题]] A(n)。若

(i) A(0) 为真，<br>
(ii) 对每个 n ∈ ℕ，由 A(n) 为真可以推出 A(ν(n)) 为真，

则 A(n) 对一切 n ∈ ℕ 为真。

**证明** 令

N := { n ∈ ℕ ; A(n) 为真 }

由 (i)，0 ∈ N。由 (ii)，n ∈ N ⟹ ν(n) ∈ N。故 N 满足 (N1) 的两个条件，得 N = ℕ，即 A(n) 对一切 n 为真。∎

条件 (i) 称**归纳基础**(base case)，条件 (ii) 称**归纳步骤**(induction step)，(ii) 中假设 A(n) 为真这一步称**归纳假设**(induction hypothesis)。

**注** 归纳原理不是新公理，它就是 (N1) 换了个说法：把「子集 N」换成「使 A 为真的那些 n」。两者互相翻译。

**例** 证明：∀n ∈ ℕ : ν(n) ≠ n（没有自然数是自己的后继）。

**归纳基础**：ν(0) ∈ ℕ<sup>×</sup> = ℕ ∖ {0}，故 ν(0) ≠ 0。

**归纳步骤**：设 ν(n) ≠ n。要证 ν(ν(n)) ≠ ν(n)。用[[fond_proposizioni|逆否]]：

ν(ν(n)) = ν(n) ⟹ ν(n) = n（由 (N0) 单射）

而这与归纳假设 ν(n) ≠ n 矛盾。故 ν(ν(n)) ≠ ν(n)。

由归纳原理，结论对一切 n 成立。∎

**注（另外两种形式留待后面）** 实际使用中常需要两种加强版：

**从 n₀ 起的归纳**——只对 n ≥ n₀ 断言 A(n)；<br>
**强归纳**——归纳步骤中可以假设 A(k) 对一切 n₀ ≤ k ≤ n 都为真。

这两种形式的陈述都用到了 **+** 与 **≤**，而加法与序还没有定义。它们将在[[num_aritmetica|自然数的算术]]之后给出。本节只用得上上面的基本形式。

## 注：ℕ 存在吗？唯一吗？

上面的公理刻画了「自然数是什么样的」，但没有回答两个问题：**这样的 (ℕ, 0, ν) 存在吗？如果存在，有几个？** A–E 对此作了讨论，这里概述。

**存在性。** 称集合 M 为一个**无穷系统**(infinite system)，若存在单射 f : M → M 使 f(M) ⊊ M（像真含于 M 自身）。Dedekind 证明：**任何无穷系统中都含有一个自然数模型 (ℕ, 0, ν)**。于是 ℕ 的存在性归结为无穷系统的存在性。

Dedekind 本人的存在性证明隐含使用了 Frege 于 1893 年提出的**概括公理**：对每个关于集合的性质 E，集合

M<sub>E</sub> := { x ; x 是集合且满足 E }

存在。1901 年 Russell 指出这条公理导致矛盾。取 E 为「x 是集合且 x ∉ x」，得

M := { x ; (x 是集合) ∧ (x ∉ x) }

于是 M ∈ M ⟺ M ∉ M。这正是[[fond_insiemi|集合那节提到的、描述式必须从已有集合中切取]]的原因。

现代的处理是区分**类**(class)与**集合**(set)：集合是特别「小」的类。概括公理改述为「M<sub>E</sub> 是一个**类**」，于是上面的 M 是类而不是集合，矛盾消失。此外还需一条单独的公理，保证我们一直在用的

{ x ; (x ∈ X) ∧ E(x) } = { x ∈ X ; E(x) }

是集合。

要在公理集合论内证明 ℕ 存在，需要**无穷公理**：存在一个**归纳集**。这里归纳集指含 ∅、且对每个 z 都含 z ∪ {z} 的集合 N。取

ℕ := ⋂ { m ; m 是归纳集 }，  ν(z) := z ∪ {z}，  0 := ∅

可证 ℕ 本身是归纳集，且 (ℕ, 0, ν) 满足 Peano 公理。这就给出了一个模型。

**唯一性。** 设 (ℕ′, 0′, ν′) 是另一个模型。可以证明存在双射 φ : ℕ → ℕ′ 使

φ(0) = 0′  且  φ ∘ ν = ν′ ∘ φ

即 φ 是从 (ℕ, 0, ν) 到 (ℕ′, 0′, ν′) 的**同构**。所以**自然数在同构意义下唯一**——因此可以名正言顺地说「**那个**自然数系统」。

（以上讨论属于公理集合论，本节不展开证明。）

## 练习

(a) 用归纳原理证明：∀n ∈ ℕ<sup>×</sup>，存在唯一的 m ∈ ℕ 使 ν(m) = n。（提示：存在性即注 5.1(a) 的满射，唯一性用 (N0)。这道题请把两部分分别写清。）

(b) 考虑三元组 ℕ<sub>C</sub> := {0}，ν(0) := 0。检查它是否满足 (N0) 与 (N1)，并说明它为什么不能作为自然数模型。

(c) 设 (ℕ, 0, ν) 满足两条公理。证明：对任何 n ∈ ℕ，集合

S<sub>n</sub> := { n, ν(n), ν(ν(n)), … }

对 ν 封闭。再说明为什么由此**不能**推出 S<sub>n</sub> = ℕ。

## 参考解答

**(a) 存在性**：即 ν : ℕ → ℕ<sup>×</sup> 满射，已在注 5.1(a) 中证明——任给 n ∈ ℕ<sup>×</sup> = im(ν)，存在 m 使 ν(m) = n。

**唯一性**：设 ν(m) = n = ν(m′)。由 **(N0)** ν 单射，得 m = m′。

两部分合起来：∀n ∈ ℕ<sup>×</sup>, ∃!m ∈ ℕ : ν(m) = n。∎

**(b)** ℕ<sub>C</sub> = {0}，ν(0) = 0。

首先，**这个 ν 根本不合法**：按定义 ν 的到达域必须是 ℕ<sub>C</sub><sup>×</sup> = ℕ<sub>C</sub> ∖ {0} = ∅。而 ν(0) = 0 ∉ ∅，故 ν 不是从 ℕ<sub>C</sub> 到 ℕ<sub>C</sub><sup>×</sup> 的函数。

若强行考察：ν 作为 {0} → {0} 的函数是单射，(N0) 形式上成立；(N1) 也成立（唯一含 0 的子集就是 {0} 自身）。但它不是自然数模型，因为它违反了「0 不是任何数的后继」——而这一条正是由**到达域 ℕ<sup>×</sup>** 承担的。

这说明到达域的限制不是可有可无的形式细节：**它承担着一条实质的公理**。∎

**(c)** **S<sub>n</sub> 对 ν 封闭**：S<sub>n</sub> 中的元素形如 n 或 ν 作用若干次于 n 的结果。任取这样一个元素 x，则 ν(x) 也是 ν 作用若干次于 n 的结果，故 ν(x) ∈ S<sub>n</sub>。

**不能推出 S<sub>n</sub> = ℕ**：(N1) 要求的两个条件是「含 **0**」与「对 ν 封闭」。S<sub>n</sub> 满足第二条，但当 n ≠ 0 时**不含 0**——因为由注 5.1(a)，0 不是任何元素的后继，而 S<sub>n</sub> 中除 n 外全是后继，n 本身又不是 0。缺了「0 ∈ N」这个条件，(N1) 用不上。

例如 n = 1 时 S₁ = {1, 2, 3, …}，它对 ν 封闭但不等于 ℕ。∎

**注** 这道题说明 (N1) 的两个条件缺一不可：只有「对 ν 封闭」不够，必须**从 0 起步**。

## 前瞻

公理只给出了 ℕ、0 与 ν，还没有加法与乘法。它们要靠 ν 递归地定义：n + 0 := n，n + ν(m) := ν(n + m)。这类「用前一步定义后一步」的定义方式是否合法，本身需要证明，即递归定理。见 [[num_aritmetica|自然数的算术]]。
