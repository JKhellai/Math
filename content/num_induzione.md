---
id: num_induzione
label: 归纳原理与良序原理
parent: num_costruzioni
prerequisites: [num_aritmetica]
summary: 归纳原理有三种常用形式：从 0 起、从 n₀ 起、强归纳（可用此前全部情形）。良序原理说 ℕ 的每个非空子集有最小元，它由 (N1) 推出，是归纳的另一副面孔。
status: learning
refs: Amann–Escher, Analysis I §I.5
---

[[num_n|(N1)]] 已经用过多次。它的直接形式是关于**子集**的；实际证题时用的是关于**命题**的形式，而且常需要两种加强：从任意起点开始，以及在归纳步骤中调用此前的全部结论。[[num_aritmetica|加法与序]]已经就位，现在可以把这些形式完整写出来。

## 先做一个完整的例子

**待证**：对每个 n ≥ 1，前 n 个奇数之和等于 n²，即

1 + 3 + 5 + ⋯ + (2n − 1) = n²

**先手算几个**，看它是否可信：

n = 1：1 = 1 = 1²<br>
n = 2：1 + 3 = 4 = 2²<br>
n = 3：1 + 3 + 5 = 9 = 3²<br>
n = 4：1 + 3 + 5 + 7 = 16 = 4²

<svg viewBox="0 0 420 175" xmlns="http://www.w3.org/2000/svg">
<rect x="30" y="40" width="26" height="26" fill="#FF7F50" fill-opacity="0.5" stroke="#E0612F" stroke-width="1"/>
<text x="43" y="86" font-size="11" text-anchor="middle" fill="#555">1 = 1²</text>
<rect x="100" y="40" width="26" height="26" fill="#FF7F50" fill-opacity="0.5" stroke="#E0612F" stroke-width="1"/>
<rect x="126" y="40" width="26" height="26" fill="#5A5FE0" fill-opacity="0.35" stroke="#5A5FE0" stroke-width="1"/>
<rect x="100" y="66" width="26" height="26" fill="#5A5FE0" fill-opacity="0.35" stroke="#5A5FE0" stroke-width="1"/>
<rect x="126" y="66" width="26" height="26" fill="#5A5FE0" fill-opacity="0.35" stroke="#5A5FE0" stroke-width="1"/>
<text x="126" y="112" font-size="11" text-anchor="middle" fill="#555">1+3 = 2²</text>
<rect x="200" y="40" width="26" height="26" fill="#FF7F50" fill-opacity="0.5" stroke="#E0612F" stroke-width="1"/>
<rect x="226" y="40" width="26" height="26" fill="#5A5FE0" fill-opacity="0.35" stroke="#5A5FE0" stroke-width="1"/>
<rect x="200" y="66" width="26" height="26" fill="#5A5FE0" fill-opacity="0.35" stroke="#5A5FE0" stroke-width="1"/>
<rect x="226" y="66" width="26" height="26" fill="#5A5FE0" fill-opacity="0.35" stroke="#5A5FE0" stroke-width="1"/>
<rect x="252" y="40" width="26" height="26" fill="#00A070" fill-opacity="0.3" stroke="#00A070" stroke-width="1"/>
<rect x="252" y="66" width="26" height="26" fill="#00A070" fill-opacity="0.3" stroke="#00A070" stroke-width="1"/>
<rect x="200" y="92" width="26" height="26" fill="#00A070" fill-opacity="0.3" stroke="#00A070" stroke-width="1"/>
<rect x="226" y="92" width="26" height="26" fill="#00A070" fill-opacity="0.3" stroke="#00A070" stroke-width="1"/>
<rect x="252" y="92" width="26" height="26" fill="#00A070" fill-opacity="0.3" stroke="#00A070" stroke-width="1"/>
<text x="239" y="138" font-size="11" text-anchor="middle" fill="#555">1+3+5 = 3²</text>
<text x="320" y="70" font-size="11" fill="#777">每加一个奇数，</text>
<text x="320" y="90" font-size="11" fill="#777">正方形边长加一</text>
<text x="320" y="110" font-size="11" fill="#00A070">新增的 L 形有</text>
<text x="320" y="128" font-size="11" fill="#00A070">2n+1 个格子</text>
</svg>

手算只能验证有限个 n。要对**一切** n 成立，需要归纳。

**归纳基础（n₀ = 1）**：1 = 1 · 1 = 1²，成立。

**归纳假设**：设对某个 n ≥ 1 有 1 + 3 + ⋯ + (2n − 1) = n²。

**归纳步骤**：要证 n + 1 的情形，即

1 + 3 + ⋯ + (2(n+1) − 1) = (n+1)²

左边的最后一项是 2(n+1) − 1 = 2n + 1，故

1 + 3 + ⋯ + (2n + 1)<br>
= [ 1 + 3 + ⋯ + (2n − 1) ] + (2n + 1)　（把最后一项单独拆出）<br>
= n² + (2n + 1)　（**用归纳假设**）<br>
= n² + 2n + 1<br>
= (n + 1)²　（由[[num_aritmetica|分配律]]展开可验证）

归纳步骤完成，结论对一切 n ≥ 1 成立。∎

**注意归纳假设用在哪一步**：只用了一次，就是把方括号里那一整串替换成 n²。归纳法的全部力量都集中在这一步——**它允许你把「上一个情形」当作已知**。

## 归纳法的标准格式

设对每个 n ∈ ℕ 给定一个命题 A(n)。要证 A(n) 对一切 n 成立，做两件事：

**(a) 归纳基础**：证明 A(0) 为真。

**(b) 归纳步骤**，分两半：

**(α) 归纳假设**：设 A(n) 对某个 n ∈ ℕ 为真。<br>
**(β) 由 (α) 及此前已证的结论，推出 A(n + 1) 为真。**

**为什么这样就够了**：令 N := { n ∈ ℕ ; A(n) 为真 }。(a) 给出 0 ∈ N，(b) 给出 n ∈ N ⟹ n + 1 ∈ N。由 [[num_n|(N1)]]，N = ℕ。∎

**注（归纳假设不是循环论证）** (α) 中「设 A(n) 为真」不是假定结论成立。要证的是蕴含式 A(n) ⟹ A(n+1)，而[[fond_dimostrazioni|证蕴含式的标准做法]]正是「设前件为真，推出后件」。假设的是**某一个** n 的情形，推出的是**下一个**；结合基础，才逐级传遍全体。

## 从 n₀ 起的归纳

上面的例子实际上从 n₀ = 1 起步，而不是 0。这需要一点点推广。

**命题（A–E 命题 5.7，归纳原理）** 设 n₀ ∈ ℕ，且对每个 n ≥ n₀ 给定命题 A(n)。若

**(i)** A(n₀) 为真，<br>
**(ii)** 对每个 n ≥ n₀，由 A(n) 为真可推出 A(n + 1) 为真，

则 A(n) 对一切 n ≥ n₀ 为真。

**证明** 把指标**平移**，化归到从 0 起的情形。令

N := { n ∈ ℕ ; A(n + n₀) 为真 }

**0 ∈ N**：A(0 + n₀) = A(n₀)，由 (i) 为真。

**n ∈ N ⟹ n + 1 ∈ N**：设 A(n + n₀) 为真。因 n + n₀ ≥ n₀，由 (ii) 得 A((n + n₀) + 1) 为真，即 A((n + 1) + n₀) 为真（用[[num_aritmetica|加法结合律与交换律]]）。

由 (N1)，N = ℕ，即 A(m) 对一切 m ≥ n₀ 为真（取 m = n + n₀，当 n 跑遍 ℕ 时 m 跑遍 ≥ n₀ 的全部自然数）。∎

**平移的意思**：原来的 n₀, n₀+1, n₀+2, … 被重新编号成 0, 1, 2, …，于是又能用标准的 (N1)。

## 例：2ⁿ > n²（n ≥ 5）

这个例子说明为什么需要 n₀ ≠ 0：结论在小的 n 处**不成立**。

先看小的情形：

n = 0：2⁰ = 1 > 0 = 0² ✓<br>
n = 1：2¹ = 2 > 1 = 1² ✓<br>
n = 2：2² = 4，2² = 4，**不是** > ✗<br>
n = 3：2³ = 8 < 9 = 3² ✗<br>
n = 4：2⁴ = 16 = 4²，**不是** > ✗<br>
n = 5：2⁵ = 32 > 25 = 5² ✓

从 n = 5 起才稳定成立，所以取 n₀ = 5。

**归纳基础**：32 > 25 ✓（上面已验）

**归纳假设**：设对某个 n ≥ 5 有 2ⁿ > n²。

**归纳步骤**：

2^(n+1) = 2 · 2ⁿ > 2 · n² = n² + n²　（**用归纳假设**，再把 2n² 写成 n² + n²）

现在需要 n² ≥ 2n + 1。因 n ≥ 5：

n · n ≥ 5n　（[[num_aritmetica|定理 5.3(x)]]，两边乘 n）<br>
5n = 2n + 3n > 2n + 1　（因 n ≥ 5 ⟹ 3n ≥ 15 > 1）

故 n² > 2n + 1。代回：

2^(n+1) > n² + n² > n² + 2n + 1 = (n + 1)²

归纳步骤完成，结论对一切 n ≥ 5 成立。∎

## 强归纳

有时证 A(n + 1) 需要用到的不止 A(n)，而是 A(n₀), …, A(n) 全部。

**命题（A–E 命题 5.9）** 设 n₀ ∈ ℕ，且对每个 n ≥ n₀ 给定命题 A(n)。若

**(i)** A(n₀) 为真，<br>
**(ii)** 对每个 n ≥ n₀，由「A(k) 对一切 n₀ ≤ k ≤ n 为真」这一假设可推出 A(n + 1) 为真，

则 A(n) 对一切 n ≥ n₀ 为真。

<svg viewBox="0 0 420 195" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="ia" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#5A5FE0"/>
</marker>
<marker id="ib" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#E0612F"/>
</marker>
</defs>
<text x="20" y="24" font-size="12" fill="#5A5FE0">普通归纳：只用前一个</text>
<circle cx="50" cy="55" r="13" fill="none" stroke="#5A5FE0" stroke-width="1.2"/><text x="50" y="60" font-size="11" text-anchor="middle" fill="#333">0</text>
<circle cx="115" cy="55" r="13" fill="none" stroke="#5A5FE0" stroke-width="1.2"/><text x="115" y="60" font-size="11" text-anchor="middle" fill="#333">1</text>
<circle cx="180" cy="55" r="13" fill="none" stroke="#5A5FE0" stroke-width="1.2"/><text x="180" y="60" font-size="11" text-anchor="middle" fill="#333">2</text>
<circle cx="245" cy="55" r="13" fill="none" stroke="#5A5FE0" stroke-width="1.2"/><text x="245" y="60" font-size="11" text-anchor="middle" fill="#333">3</text>
<circle cx="310" cy="55" r="13" fill="#979AFF" fill-opacity="0.3" stroke="#5A5FE0" stroke-width="1.5"/><text x="310" y="60" font-size="11" text-anchor="middle" fill="#333">4</text>
<line x1="258" y1="55" x2="295" y2="55" stroke="#5A5FE0" stroke-width="1.5" marker-end="url(#ia)"/>
<text x="350" y="59" font-size="10" fill="#5A5FE0">只有一支箭</text>
<text x="20" y="110" font-size="12" fill="#E0612F">强归纳：可用此前全部</text>
<circle cx="50" cy="145" r="13" fill="none" stroke="#E0612F" stroke-width="1.2"/><text x="50" y="150" font-size="11" text-anchor="middle" fill="#333">0</text>
<circle cx="115" cy="145" r="13" fill="none" stroke="#E0612F" stroke-width="1.2"/><text x="115" y="150" font-size="11" text-anchor="middle" fill="#333">1</text>
<circle cx="180" cy="145" r="13" fill="none" stroke="#E0612F" stroke-width="1.2"/><text x="180" y="150" font-size="11" text-anchor="middle" fill="#333">2</text>
<circle cx="245" cy="145" r="13" fill="none" stroke="#E0612F" stroke-width="1.2"/><text x="245" y="150" font-size="11" text-anchor="middle" fill="#333">3</text>
<circle cx="310" cy="145" r="13" fill="#FF7F50" fill-opacity="0.3" stroke="#E0612F" stroke-width="1.5"/><text x="310" y="150" font-size="11" text-anchor="middle" fill="#333">4</text>
<path d="M 58 136 Q 180 100 300 136" fill="none" stroke="#E0612F" stroke-width="1.2" marker-end="url(#ib)"/>
<path d="M 123 138 Q 215 112 299 139" fill="none" stroke="#E0612F" stroke-width="1.2" marker-end="url(#ib)"/>
<path d="M 191 141 Q 245 122 298 141" fill="none" stroke="#E0612F" stroke-width="1.2" marker-end="url(#ib)"/>
<line x1="258" y1="145" x2="295" y2="145" stroke="#E0612F" stroke-width="1.2" marker-end="url(#ib)"/>
<text x="350" y="149" font-size="10" fill="#E0612F">全部可用</text>
<text x="210" y="185" font-size="10" text-anchor="middle" fill="#777">两者结论相同，强归纳只是把归纳假设放宽</text>
</svg>

**证明** 令 B(n) := 「A(k) 对一切 n₀ ≤ k ≤ n 为真」。对 B 用普通归纳（命题 5.7）。

**B(n₀)**：即 A(n₀) 为真，由 (i)。

**B(n) ⟹ B(n + 1)**：设 B(n)，即 A(k) 对 n₀ ≤ k ≤ n 全为真。由 (ii) 得 A(n + 1) 为真。把它与 B(n) 合起来，得 A(k) 对 n₀ ≤ k ≤ n + 1 全为真，即 B(n + 1)。

由命题 5.7，B(n) 对一切 n ≥ n₀ 为真。特别地，取 k = n 得 A(n) 对一切 n ≥ n₀ 为真。∎

**注** 强归纳不是更强的公理，它由普通归纳推出。差别只在**使用时的便利**：归纳步骤中可以调用此前任意多个已证情形，而不必只用紧邻的那一个。

## 良序原理

(N1) 还有一副面孔，形式上与归纳很不一样，用起来常常更顺手。

**命题（A–E 命题 5.5）** ℕ 是**良序**的(well ordered)，即：**ℕ 的每个非空子集都有最小元**。

**证明（反证）** 设 A ⊆ ℕ 非空，且 A **没有**最小元。令

B := { n ∈ ℕ ; n 是 A 的[[fond_ordine|下界]] }

即「一切不超过 A 中每个元素的自然数」。用 (N1) 证 B = ℕ。

**0 ∈ B**：由[[num_aritmetica|0 = min(ℕ)]]，0 ≤ a 对一切 a ∈ ℕ 成立，特别地对一切 a ∈ A 成立。故 0 是 A 的下界。

**n ∈ B ⟹ n + 1 ∈ B**：设 n 是 A 的下界，即 ∀a ∈ A : n ≤ a。

此时 **n ∉ A**——否则 n 既属于 A 又是 A 的下界，那 n 就是 A 的最小元，与「A 无最小元」矛盾。

于是对一切 a ∈ A，有 n ≤ a 且 n ≠ a，即 n < a。由[[num_aritmetica|定理 5.3(vi)]]（n 与 n+1 之间没有别的自然数），n < a 蕴含 n + 1 ≤ a。故 n + 1 也是 A 的下界，即 n + 1 ∈ B。

由 (N1)，B = ℕ。

**导出矛盾**：因 A 非空，取 m ∈ A。则 m ∈ ℕ = B，即 m 是 A 的下界。而 m 又属于 A，故 m 是 A 的最小元——与「A 无最小元」矛盾。∎

**注（三者的关系）** (N1)、归纳原理、良序原理讲的是同一件事的三种说法：

**(N1)**：含 0 且对后继封闭的子集是全体。<br>
**归纳原理**：A(0) 真且 A(n) ⟹ A(n+1)，则 A 处处真。<br>
**良序原理**：非空子集必有最小元。

上面由 (N1) 推出了良序原理。反过来也能由良序原理推出归纳（练习 (c)）。实际证题时按方便选用：**要「逐级推进」时用归纳，要「取一个最小的反例」时用良序**。

## 练习

(a) 用归纳法证明：∀n ∈ ℕ，0 + 1 + 2 + ⋯ + n = n(n+1)/2。（提示：从 n₀ = 0 起。此处允许使用[[num_aritmetica|定理 5.3]] 的算术律。）

(b) 用归纳法证明：∀n ≥ 1，2ⁿ ≥ n + 1。

(c) 用**良序原理**证明归纳原理的基本形式：设 A(0) 为真，且 ∀n : A(n) ⟹ A(n+1)。证明 A(n) 对一切 n 成立。（提示：反设不然，考虑「使 A 为假的 n」构成的集合。）

## 参考解答

**(a)** 记 S(n) := 0 + 1 + ⋯ + n。

**归纳基础（n = 0）**：S(0) = 0，而 0·(0+1)/2 = 0。相等 ✓

**归纳假设**：设 S(n) = n(n+1)/2。

**归纳步骤**：

S(n+1) = S(n) + (n+1)　（把最后一项拆出）<br>
= n(n+1)/2 + (n+1)　（**用归纳假设**）<br>
= (n+1) · [ n/2 + 1 ]　（提出公因子 n+1）<br>
= (n+1) · (n+2)/2

这正是 (n+1)((n+1)+1)/2。归纳完成。∎

**(b) 归纳基础（n = 1）**：2¹ = 2，1 + 1 = 2。有 2 ≥ 2 ✓

**归纳假设**：设对某个 n ≥ 1 有 2ⁿ ≥ n + 1。

**归纳步骤**：

2^(n+1) = 2 · 2ⁿ ≥ 2(n + 1)　（**用归纳假设**，两边乘 2，由定理 5.3(x)）<br>
= 2n + 2 = (n + 2) + n<br>
≥ n + 2　（因 n ≥ 1 ≥ 0，加上非负的 n 只会变大）

而 n + 2 = (n+1) + 1，正是所需。归纳完成。∎

**(c)** 设 A(0) 为真且 ∀n : A(n) ⟹ A(n+1)。反设结论不成立，即存在某个 n 使 A(n) 为假。令

F := { n ∈ ℕ ; A(n) 为假 }

由反设 F ≠ ∅。由**良序原理**，F 有最小元 m := min(F)。

**m ≠ 0**：因 A(0) 为真，0 ∉ F。

故 m ≥ 1，于是 m 有前驱：由[[num_n|注 5.1(a)]]，存在 m′ 使 m = m′ + 1。

**A(m′) 为真**：因 m′ < m 而 m 是 F 中最小的，故 m′ ∉ F。

由假设 A(m′) ⟹ A(m′ + 1) = A(m)，得 A(m) 为真。但 m ∈ F 说明 A(m) 为假——矛盾。

故 F = ∅，即 A(n) 对一切 n 成立。∎

**注** 这个证法的套路是「**取最小的反例**」：假设有反例，取最小的那个，再说明它的前一个不是反例，从而推出它自己也不是反例，矛盾。这是良序原理最常见的用法。

## 前瞻

良序原理的一个直接应用是整数的除法：给定 m ≥ 1 与 n，可以在「所有形如 n − km 的非负数」中取最小者，得到唯一的商与余数。由此还能推出每个大于 1 的自然数都可分解为素数之积。见 [[num_divisione|带余除法与素因数分解]]。
