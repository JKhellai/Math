---
id: fond_immagine_preimmagine
label: 像与原像
parent: fond_fondamenta
prerequisites: [fond_composizione, fond_insiemi, fond_famiglie]
summary: 函数 f 诱导两个集值函数 f:P(X)→P(Y) 与 f⁻¹:P(Y)→P(X)。原像与并、交、补都可交换，像只对并可交换、对交只有 ⊆——这个不对称贯穿此后的分析。
status: learning
refs: Amann–Escher, Analysis I §I.3
---

[[fond_composizione|上一节]]的注里出现了原像 f⁻¹(C)，它对任意函数（不要求双射）都有定义。本节把像与原像都看成**作用在子集上的函数**，考察它们在并、交、补下的行为。结论是一个不对称：原像与三种运算都可交换，像不然。这个不对称在此后（连续性、可测性）反复出现，值得一开始就讲清。

## 两个诱导的集值函数

设 f : X → Y。回忆[[fond_funzioni|像]]与[[fond_composizione|原像]]的定义：对 A ⊆ X、B ⊆ Y，

f(A) := { f(a) : a ∈ A } ⊆ Y

f⁻¹(B) := { x ∈ X : f(x) ∈ B } ⊆ X

把子集送到子集，这就给出两个函数：

f : P(X) → P(Y)，  A ↦ f(A)

f⁻¹ : P(Y) → P(X)，  B ↦ f⁻¹(B)

其中 P(X) 是 X 的[[fond_insiemi|幂集]]。这里同一个符号 f 兼指原函数 X → Y 与诱导的集值函数 P(X) → P(Y)；从括号里是元素还是集合可分辨，不致混淆。

**注（纤维）** 对 y ∈ Y，记 f⁻¹(y) := f⁻¹({y}) = { x ∈ X : f(x) = y }，称 f 在 y 处的**纤维**(fiber)，即方程 f(x) = y 的解集，可能为空。即使 f 不双射、逆函数不存在，纤维 f⁻¹(y) 也总有定义。

## 命题 3.8：像与原像对集合运算的行为

**命题（A–E 命题 3.8）** 设 f : X → Y，{Aα} 是 X 的一族子集，{Bα} 是 Y 的一族子集。则：

关于**像** f：

(i) A ⊆ B ⊆ X ⟹ f(A) ⊆ f(B)

(ii) f(⋃α Aα) = ⋃α f(Aα)

(iii) f(⋂α Aα) ⊆ ⋂α f(Aα)

(iv) f(Aᶜ) ⊇ f(X) \ f(A)

关于**原像** f⁻¹：

(i′) B ⊆ B′ ⊆ Y ⟹ f⁻¹(B) ⊆ f⁻¹(B′)

(ii′) f⁻¹(⋃α Bα) = ⋃α f⁻¹(Bα)

(iii′) f⁻¹(⋂α Bα) = ⋂α f⁻¹(Bα)

(iv′) f⁻¹(Bᶜ) = (f⁻¹(B))ᶜ

**对比 (iii)(iv) 与 (iii′)(iv′)：原像那侧全是等号，像那侧只是包含。** 换句话说，**原像 f⁻¹ 与并、交、补三种运算都可交换；像 f 只与并可交换，对交、补一般只有单向包含。** 这是本节的要点。

## 证明

原书把这些证明留给读者。逐条补上。证明的基本手法：要证两个集合相等，就证元素属于左边 ⟺ 属于右边；要证包含，就证 ⟹。

**(i)**<br>
y ∈ f(A) ⟹ ∃a ∈ A : y = f(a)<br>
（像的定义）

a ∈ A ⊆ B ⟹ a ∈ B ⟹ y = f(a) ∈ f(B)

故 f(A) ⊆ f(B)。∎

**(ii)** 证 f(⋃α Aα) = ⋃α f(Aα)，两向包含：

y ∈ f(⋃α Aα)<br>
 ⟺ ∃a ∈ ⋃α Aα : y = f(a)<br>
 ⟺ ∃α, ∃a ∈ Aα : y = f(a)<br>
 ⟺ ∃α : y ∈ f(Aα)<br>
 ⟺ y ∈ ⋃α f(Aα)<br>
（第 2 步用[[fond_insiemi|并集]]的定义：属于并 ⟺ 属于某个 Aα；每步都是等价，故得等号）∎

**(iii)** 只有 ⊆：

y ∈ f(⋂α Aα) ⟹ ∃a ∈ ⋂α Aα : y = f(a)

a ∈ ⋂α Aα ⟹ ∀α : a ∈ Aα ⟹ ∀α : y = f(a) ∈ f(Aα) ⟹ y ∈ ⋂α f(Aα)

故 f(⋂α Aα) ⊆ ⋂α f(Aα)。∎

**为什么反向不成立**：y ∈ ⋂α f(Aα) 意味着**每个** Aα 里都有某元素映到 y，但这些元素可以**各不相同**；未必存在一个**公共**元素同时属于所有 Aα 又映到 y。下面的反例把这一点做实。

**(iv)** f(X) \ f(A) ⊆ f(Aᶜ)：

y ∈ f(X) \ f(A)<br>
 ⟹ y ∈ f(X) ∧ y ∉ f(A)<br>
 ⟹ (∃x ∈ X : f(x) = y) ∧ (∀a ∈ A : f(a) ≠ y)

第一个合取给出一个 x 使 f(x) = y；第二个说凡映到 y 的都不在 A，故这个 x ∉ A，即 x ∈ Aᶜ。于是 y = f(x) ∈ f(Aᶜ)。∎

（反向一般不成立，理由与 (iii) 同类：Aᶜ 中某元素映到 y，不排除 A 中另有元素也映到 y，于是 y 仍可能落在 f(A) 里。）

**(i′)**<br>
x ∈ f⁻¹(B) ⟹ f(x) ∈ B ⊆ B′ ⟹ f(x) ∈ B′ ⟹ x ∈ f⁻¹(B′)<br>
（原像的定义）∎

**(ii′)**<br>
x ∈ f⁻¹(⋃α Bα)<br>
 ⟺ f(x) ∈ ⋃α Bα<br>
 ⟺ ∃α : f(x) ∈ Bα<br>
 ⟺ ∃α : x ∈ f⁻¹(Bα)<br>
 ⟺ x ∈ ⋃α f⁻¹(Bα)<br>
（关键在第 2 步：条件全都落在 f(x) 这**单个**元素上，"f(x) 属于某个 Bα"没有 (iii) 里那种"公共元素"的障碍）∎

**(iii′)**<br>
x ∈ f⁻¹(⋂α Bα)<br>
 ⟺ f(x) ∈ ⋂α Bα<br>
 ⟺ ∀α : f(x) ∈ Bα<br>
 ⟺ ∀α : x ∈ f⁻¹(Bα)<br>
 ⟺ x ∈ ⋂α f⁻¹(Bα)<br>
（同样，条件只关乎 f(x) 一个元素是否落在每个 Bα 中，故交也得等号）∎

**(iv′)**<br>
x ∈ f⁻¹(Bᶜ)<br>
 ⟺ f(x) ∈ Bᶜ<br>
 ⟺ f(x) ∉ B<br>
 ⟺ x ∉ f⁻¹(B)<br>
 ⟺ x ∈ (f⁻¹(B))ᶜ<br>
（补也得等号）∎

**根源**：原像的条件永远是「**f(x) 这一个元素**是否落在某集合中」，逻辑上「f(x) ∈ ⋃Bα」「f(x) ∈ ⋂Bα」「f(x) ∈ Bᶜ」分别就是「∃α」「∀α」「¬」——集合运算与逻辑联结词一一对应，原样透过 f⁻¹。像的条件却是「**是否存在某个** a ∈ A 映到 y」，多了一层存在量词；而存在量词与「交、补」不交换（∃ 与 ∀、¬ 不能随意换序），障碍由此而来。

## 反例：像对交只有包含

**例** 取 X := {1, 2, 3}，Y := {a, b}，f(1) := a，f(2) := a，f(3) := b。设 A := {1}，B := {2}。

<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="mi" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#555"/>
    </marker>
  </defs>
  <ellipse cx="90" cy="100" rx="46" ry="72" fill="none" stroke="#888" stroke-width="1.3"/>
  <ellipse cx="270" cy="100" rx="42" ry="60" fill="none" stroke="#888" stroke-width="1.3"/>
  <text x="90" y="16" font-size="14" text-anchor="middle" fill="#333">X</text>
  <text x="270" y="26" font-size="14" text-anchor="middle" fill="#333">Y</text>
  <circle cx="90" cy="55" r="4" fill="#E0612F"/><text x="74" y="59" font-size="12" fill="#E0612F">1</text>
  <circle cx="90" cy="100" r="4" fill="#5A5FE0"/><text x="74" y="104" font-size="12" fill="#5A5FE0">2</text>
  <circle cx="90" cy="145" r="4" fill="#333"/><text x="74" y="149" font-size="12" fill="#333">3</text>
  <circle cx="270" cy="78" r="4" fill="#333"/><text x="284" y="82" font-size="12" fill="#333">a</text>
  <circle cx="270" cy="122" r="4" fill="#333"/><text x="284" y="126" font-size="12" fill="#333">b</text>
  <line x1="104" y1="57" x2="256" y2="76" stroke="#E0612F" stroke-width="1.3" marker-end="url(#mi)"/>
  <line x1="104" y1="100" x2="256" y2="80" stroke="#5A5FE0" stroke-width="1.3" marker-end="url(#mi)"/>
  <line x1="104" y1="143" x2="256" y2="122" stroke="#555" stroke-width="1.3" marker-end="url(#mi)"/>
  <text x="42" y="192" font-size="11" fill="#E0612F">A={1}</text>
  <text x="112" y="192" font-size="11" fill="#5A5FE0">B={2}</text>
  <text x="210" y="192" font-size="11" fill="#777">f(1)=f(2)=a</text>
</svg>

A ∩ B = ∅ ⟹ f(A ∩ B) = f(∅) = ∅

f(A) = {a}，f(B) = {a} ⟹ f(A) ∩ f(B) = {a}

∅ ⊊ {a} ⟹ f(A ∩ B) ⊊ f(A) ∩ f(B)

等号失败的原因正如 (iii) 的分析：a 同时在 f(A) 和 f(B) 里，是因为 1 映到 a、2 也映到 a，但 1 与 2 是**不同**的点，A ∩ B 里并没有公共元素。**f 单射时这种情形不会发生**，(iii) 与 (iv) 对单射 f 升级为等号（练习 (c)）。

## 复合的原像

**命题** f : X → Y，g : Y → V，则对 C ⊆ V，

(g ∘ f)⁻¹(C) = f⁻¹(g⁻¹(C))，  即 (g ∘ f)⁻¹ = f⁻¹ ∘ g⁻¹。

这里三个 ⁻¹ 都是**集值原像**（不要求任何函数可逆），与[[fond_composizione|上一节可逆时的 (g∘f)⁻¹ = f⁻¹∘g⁻¹]]同形，但那里是逆函数、这里是原像，成立的条件更宽。

**证明**<br>
x ∈ (g ∘ f)⁻¹(C)<br>
 ⟺ (g ∘ f)(x) ∈ C<br>
 ⟺ g(f(x)) ∈ C<br>
 ⟺ f(x) ∈ g⁻¹(C)<br>
 ⟺ x ∈ f⁻¹(g⁻¹(C))<br>
（第 3 步、第 4 步各用一次原像的定义）∎

## 函数集的记号

**定义** X 到 Y 的全体函数构成的集合记 Funct(X, Y)，也记 **Yˣ**。

记号 Yˣ 与笛卡尔幂 Xⁿ 一致：Xⁿ（X 自乘 n 次）可等同于「从 {1, …, n} 到 X 的全体函数」——一个 n 元组 (x₁, …, xₙ) 就是把 i 送到 xᵢ 的函数。于是 Xⁿ = X^{{1,…,n}}，正是 Yˣ 记号在 Y = X、指标集为 {1,…,n} 时的特例。

**注** 由[[fond_funzioni|函数是有序对的集合]]，Yˣ ⊆ P(X × Y)。又若 U ⊆ Y ⊆ V，则把值域看得更宽不改变函数本身，故 Funct(X, U) ⊆ Funct(X, Y) ⊆ Funct(X, V)。

## 练习

(a) 证明命题 3.8 中的 (iii′)：f⁻¹(⋂α Bα) = ⋂α f⁻¹(Bα)。（若已随正文读过，独立重写一遍。）

(b) 举例说明 (iv) 中的包含 f(Aᶜ) ⊇ f(X) \ f(A) 一般是真包含（找一个 f 与 A 使 f(Aᶜ) 严格大于右边）。

(c) 证明：若 f 单射，则 (iii) 升级为等号，即 f(A ∩ B) = f(A) ∩ f(B) 对一切 A, B ⊆ X 成立。

## 参考解答

**(a)**<br>
x ∈ f⁻¹(⋂α Bα)<br>
 ⟺ f(x) ∈ ⋂α Bα<br>
 ⟺ ∀α : f(x) ∈ Bα<br>
 ⟺ ∀α : x ∈ f⁻¹(Bα)<br>
 ⟺ x ∈ ⋂α f⁻¹(Bα)<br>
（第 1、4 步用原像定义，第 2 步用交集定义；每步等价故得等号）∎

**(b)** 沿用正文的 f : {1,2,3} → {a,b}，f(1) = f(2) = a，f(3) = b。取 A := {1}。

Aᶜ = {2, 3} ⟹ f(Aᶜ) = {a, b}

f(X) = {a, b}，f(A) = {a} ⟹ f(X) \ f(A) = {b}

{a, b} ⊋ {b} ⟹ f(Aᶜ) ⊋ f(X) \ f(A)

真包含成立。原因：a 既被 A 中的 1 命中、又被 Aᶜ 中的 2 命中，故 a 同时在 f(A) 与 f(Aᶜ) 里，f(Aᶜ) 因此比「f(X) 去掉 f(A)」多出 a。∎

**(c)** 由 (iii) 已有 f(A ∩ B) ⊆ f(A) ∩ f(B)，只需证反向 ⊇。

y ∈ f(A) ∩ f(B)<br>
 ⟹ y ∈ f(A) ∧ y ∈ f(B)<br>
 ⟹ (∃a ∈ A : f(a) = y) ∧ (∃b ∈ B : f(b) = y)

于是 f(a) = y = f(b)。用 f 单射：

f(a) = f(b) ⟹ a = b

记这个公共元素为 a = b，它既在 A 又在 B，故 a ∈ A ∩ B，且 f(a) = y，即 y ∈ f(A ∩ B)。

故 f(A) ∩ f(B) ⊆ f(A ∩ B)，结合 (iii) 得等号。∎

（对照正文反例：等号失败恰恰因为 f 不单射，才有「a、b 不同却映到同一 y」；单射堵死了这条路，公共元素被迫存在。）

## 前瞻

至此 [[fond_funzioni|函数]]、[[fond_iniettive_suriettive|单射满射双射]]、[[fond_composizione|复合与逆]]、像与原像构成 A–E §I.3 的完整内容。原像"尊重一切集合运算"这一性质，是日后定义[[an_continuita|连续函数]]（用开集的原像仍是开集来刻画连续）与可测函数的技术基础——那里正需要原像与并、交、补自由交换。下一步离开函数，转向关系与运算的另一支，或按既定路线推进数系的构造。
