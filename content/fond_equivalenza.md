---
id: fond_equivalenza
label: 等价关系与商集
parent: fond_fondamenta
prerequisites: [fond_relazioni, fond_funzioni]
summary: 自反、对称、传递的关系称等价关系；它把 X 分割成互不相交的等价类，全体等价类构成商集 X/∼。任何函数 f 诱导等价关系 f(x)=f(y)，其等价类恰是纤维。
status: learning
refs: Amann–Escher, Analysis I §I.4
---

[[fond_relazioni|上一节]]列出了关系的三种性质。三条同时具备的关系有特殊地位：它把集合切成若干互不相交的块，块内的元素被视为「同类」。此后构造 ℤ、ℚ 时反复使用这个机制。

## 定义

**定义（等价关系）** X 上的关系若同时是[[fond_relazioni|自反、对称、传递]]的，称 X 上的一个**等价关系**(equivalence relation)，通常记作 ∼。

即 ∼ 满足

∀x ∈ X : x ∼ x<br>
x ∼ y ⟹ y ∼ x<br>
(x ∼ y) ∧ (y ∼ z) ⟹ x ∼ z

**定义（等价类、代表元、商集）** 设 ∼ 是 X 上的等价关系。对每个 x ∈ X，集合

[x] := { y ∈ X ; y ∼ x }

称 x 的**等价类**(equivalence class)，[x] 中的每个元素称这个等价类的一个**代表元**(representative)。全体等价类构成的集合

X/∼ := { [x] ; x ∈ X }

读作「X 模 ∼」，称**商集**(quotient set)。

由定义，X/∼ 的元素都是 X 的子集，故 X/∼ ⊆ [[fond_insiemi|P(X)]]。

**注** 「代表元」一词的含义：等价类 [x] 由它的任何一个成员**决定**——下面会证明 y ∼ x ⟹ [y] = [x]，所以用 x 还是用 y 来命名这个类都一样。这一点是商集能正常工作的基础。

## 分划

**定义（分划）** 集合 X 的一个**分划**(partition)是 P(X) ∖ {∅} 的一个子集 𝒜，满足

∀x ∈ X, ∃! A ∈ 𝒜 : x ∈ A

即：𝒜 由 X 的一些非空子集组成，每个 x 恰好属于其中一个。等价地说，𝒜 中的成员**两两不相交**，且它们的并是 X。

## 商集是一个分划

**命题（A–E 命题 4.1）** 设 ∼ 是 X 上的等价关系。则 X/∼ 是 X 的一个分划。

**证明** 分三步。

**每个等价类非空，且并起来是 X。**

∀x ∈ X : x ∼ x ⟹ x ∈ [x]<br>
（用自反性；故每个 [x] 非空，且每个 x 至少落在一个类中）

于是 X = ⋃<sub>x∈X</sub> [x]。

**两个等价类要么相同、要么不相交。** 设 [x] 与 [y] 有公共元素 z：

z ∈ [x] ∩ [y] ⟹ (z ∼ x) ∧ (z ∼ y)<br>
⟹ (x ∼ z) ∧ (z ∼ y)（对第一项用对称性）<br>
⟹ x ∼ y（传递性）

再证由 x ∼ y 可得 [x] = [y]，两向包含：

w ∈ [x] ⟹ w ∼ x ⟹ w ∼ y（用 x ∼ y 与传递性）⟹ w ∈ [y]<br>
w ∈ [y] ⟹ w ∼ y ⟹ w ∼ x（由 x ∼ y 用对称性得 y ∼ x，再用传递性）⟹ w ∈ [x]

故 [x] = [y]。所以两个等价类若相交，则必相同。

**每个 x 恰属于一个类。** x ∈ [x] 给出存在性；若 x ∈ A 且 x ∈ B（A, B ∈ X/∼），则 A 与 B 相交，由上一步 A = B，给出唯一性。∎

<svg viewBox="0 0 420 215" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="qa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#5A5FE0"/>
</marker>
</defs>
<ellipse cx="140" cy="105" rx="122" ry="88" fill="none" stroke="#888" stroke-width="1.3"/>
<text x="30" y="30" font-size="13" fill="#555">X</text>
<ellipse cx="92" cy="62" rx="42" ry="30" fill="#FF7F50" fill-opacity="0.22" stroke="#E0612F" stroke-width="1.2"/>
<circle cx="75" cy="55" r="3.5" fill="#333"/><circle cx="105" cy="50" r="3.5" fill="#333"/><circle cx="92" cy="76" r="3.5" fill="#333"/>
<text x="92" y="36" font-size="11" text-anchor="middle" fill="#E0612F">[a]</text>
<ellipse cx="192" cy="70" rx="38" ry="28" fill="#00C884" fill-opacity="0.20" stroke="#00A070" stroke-width="1.2"/>
<circle cx="178" cy="60" r="3.5" fill="#333"/><circle cx="205" cy="72" r="3.5" fill="#333"/><circle cx="180" cy="84" r="3.5" fill="#333"/>
<text x="192" y="44" font-size="11" text-anchor="middle" fill="#00A070">[b]</text>
<ellipse cx="140" cy="152" rx="52" ry="30" fill="#979AFF" fill-opacity="0.22" stroke="#5A5FE0" stroke-width="1.2"/>
<circle cx="115" cy="147" r="3.5" fill="#333"/><circle cx="145" cy="140" r="3.5" fill="#333"/><circle cx="162" cy="160" r="3.5" fill="#333"/><circle cx="128" cy="165" r="3.5" fill="#333"/>
<text x="140" y="190" font-size="11" text-anchor="middle" fill="#5A5FE0">[c]</text>
<ellipse cx="350" cy="105" rx="48" ry="82" fill="none" stroke="#888" stroke-width="1.3"/>
<text x="350" y="14" font-size="13" text-anchor="middle" fill="#555">X/∼</text>
<circle cx="350" cy="58" r="5" fill="#E0612F"/><text x="362" y="62" font-size="11" fill="#E0612F">[a]</text>
<circle cx="350" cy="105" r="5" fill="#00A070"/><text x="362" y="109" font-size="11" fill="#00A070">[b]</text>
<circle cx="350" cy="152" r="5" fill="#5A5FE0"/><text x="362" y="156" font-size="11" fill="#5A5FE0">[c]</text>
<line x1="136" y1="55" x2="296" y2="58" stroke="#5A5FE0" stroke-width="1.1" marker-end="url(#qa)" opacity="0.6"/>
<line x1="232" y1="72" x2="300" y2="100" stroke="#5A5FE0" stroke-width="1.1" marker-end="url(#qa)" opacity="0.6"/>
<line x1="194" y1="160" x2="300" y2="150" stroke="#5A5FE0" stroke-width="1.1" marker-end="url(#qa)" opacity="0.6"/>
<text x="255" y="200" font-size="10" text-anchor="middle" fill="#777">p 把每个元素送到它所在的类</text>
</svg>

## 典范商映射

由上述命题，每个 x 属于唯一的等价类，故下述对应有意义。

**定义** 

p = p<sub>X</sub> : X → X/∼，  x ↦ [x]

称从 X 到 X/∼ 的**（典范）商映射**(quotient function)。

**它是良定义的[[fond_funzioni|函数]]**：每个 x ∈ X 有唯一确定的 [x]（即 x 所属的那个唯一的类），故对应满足「每个输入恰好一个输出」。

**它是[[fond_iniettive_suriettive|满射]]**：

∀ A ∈ X/∼ ⟹ A = [x] 对某 x ∈ X（商集的定义）⟹ A = p(x)<br>
（故 X/∼ 中每个元素都被取到）

p 一般**不是单射**：同一类里的不同元素被送到同一个类，即 x ∼ y 而 x ≠ y 时 p(x) = p(y)。

## 例

**(a)（A–E）** X 为伦敦全体居民，定义 x ∼ y :⟺ x 与 y 有相同的双亲。这是等价关系；两位居民属于同一等价类当且仅当他们是兄弟姐妹。

**(b)（A–E）** X 上**最小**的等价关系是[[fond_relazioni|对角线]] Δ<sub>X</sub>，即相等关系。此时每个等价类是单点集 [x] = {x}，商集 X/∼ 与 X 一一对应。（「最小」指作为 X × X 的子集最小：任何等价关系都必须含对角线，因为自反性正是这个要求。）

**(c)（A–E，重要）** 设 f : X → Y 是函数。定义

x ∼ y  :⟺  f(x) = f(y)

**这是 X 上的等价关系**：

自反：f(x) = f(x)<br>
对称：f(x) = f(y) ⟹ f(y) = f(x)<br>
传递：f(x) = f(y) ∧ f(y) = f(z) ⟹ f(x) = f(z)<br>
（三条都直接来自相等本身的性质）

它的等价类恰是 f 的[[fond_immagine_preimmagine|纤维]]：

[x] = f<sup>−1</sup>( f(x) )<br>
（[x] 由「与 x 有相同函数值」的元素组成，正是 f(x) 处的纤维）

进一步，存在**唯一**的函数 f° : X/∼ → Y 使下图交换，即 f = f° ∘ p：

<svg viewBox="0 0 420 175" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="fq" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#555"/>
</marker>
</defs>
<text x="80" y="45" font-size="14" text-anchor="middle" fill="#333">X</text>
<text x="320" y="45" font-size="14" text-anchor="middle" fill="#333">Y</text>
<text x="200" y="145" font-size="14" text-anchor="middle" fill="#333">X/∼</text>
<line x1="96" y1="40" x2="303" y2="40" stroke="#555" stroke-width="1.3" marker-end="url(#fq)"/>
<text x="200" y="30" font-size="13" text-anchor="middle" fill="#555">f</text>
<line x1="88" y1="58" x2="180" y2="128" stroke="#555" stroke-width="1.3" marker-end="url(#fq)"/>
<text x="118" y="105" font-size="13" fill="#555">p</text>
<line x1="222" y1="128" x2="314" y2="58" stroke="#E0612F" stroke-width="1.3" marker-end="url(#fq)"/>
<text x="278" y="105" font-size="13" fill="#E0612F">f°</text>
<text x="200" y="168" font-size="10" text-anchor="middle" fill="#777">图交换 ⟺ f = f° ∘ p</text>
</svg>

**f° 的定义与良定义性**：令 f°([x]) := f(x)。这个定义用到了代表元 x，必须确认换个代表元结果不变：

[x] = [y] ⟹ x ∼ y ⟹ f(x) = f(y)<br>
（第 2 步用 ∼ 的定义）

故 f°([x]) 的值不依赖于代表元的选择，f° 良定义。

**f° 是单射**：

f°([x]) = f°([y]) ⟹ f(x) = f(y) ⟹ x ∼ y ⟹ [x] = [y]

**im(f°) = im(f)**：由 f = f° ∘ p 与 p 满射即得。特别地，**f 满射时 f° 是双射**。

**注** 这个例子给出一个一般机制：**任何函数都可以分解为「先取商、再单射」**。它的用处在于，把一个不单射的函数「压」成单射——凡取值相同的输入先被合并成一个类。后面构造 ℤ、ℚ 时用的正是这个手法：先造一大堆有序对，再用等价关系把「应当视为相同」的粘合起来。

**(d)（A–E）** 设 ∼ 是 X 上的等价关系，Y 是 X 的非空子集，则 ∼ 到 Y 上的[[fond_relazioni|限制]]是 Y 上的等价关系。（三条性质都是对「所有元素」的要求，限制到子集后仍成立。）

## 练习

(a) 在整数集上定义 m ∼ n :⟺ m − n 是 3 的倍数（借用整数的算术）。验证这是等价关系，写出全部等价类，并说明商集有多少个元素。

(b) 判断下列关系是否为等价关系，逐条检查三个性质：

① X = {1,2,3}，R := { (1,1), (2,2), (3,3), (1,2) }<br>
② 在整数集上，m ∼ n :⟺ m ≤ n

(c) 设 ∼ 是 X 上的等价关系，x, y ∈ X。证明

[x] = [y]  ⟺  x ∼ y

## 参考解答

**(a)** 记 ∼ 为「差是 3 的倍数」。

自反：m − m = 0 = 3·0 ✓<br>
对称：m − n = 3k ⟹ n − m = 3(−k) ✓<br>
传递：m − n = 3k ∧ n − l = 3k′ ⟹ m − l = (m−n) + (n−l) = 3(k + k′) ✓

故是等价关系。等价类按被 3 除的余数划分，共三个：

[0] = { …, −3, 0, 3, 6, … }（余 0）<br>
[1] = { …, −2, 1, 4, 7, … }（余 1）<br>
[2] = { …, −1, 2, 5, 8, … }（余 2）

商集有 **3** 个元素。∎

**(b)** ① **不是**等价关系。自反 ✓（三个对角元素都在）；传递 ✓（逐一检查可拼接的只有 (1,1)+(1,2)=(1,2) ∈ R 等，都成立）；但**对称失败**——(1,2) ∈ R 而 (2,1) ∉ R。

② **不是**等价关系。自反 ✓（m ≤ m）；传递 ✓（m ≤ n ≤ l ⟹ m ≤ l）；但**对称失败**——1 ≤ 2 成立而 2 ≤ 1 不成立。

（≤ 满足自反、传递，但不满足对称，而满足「反对称」：m ≤ n ∧ n ≤ m ⟹ m = n。这种关系称序关系，是另一类重要的关系。）∎

**(c)** 

**⟸** 这一步已在命题 4.1 的证明中做过：设 x ∼ y，则两向包含给出 [x] = [y]。

**⟹** 设 [x] = [y]。由自反性 x ∼ x，故 x ∈ [x] = [y]，即 x ∈ [y]，按等价类的定义即 x ∼ y。∎

**注** 这条命题说明：**等价类相等与代表元等价是一回事**。所以谈论一个等价类时，可以任取其中一个成员来称呼它，不会引起歧义——这正是「代表元」这个词的依据，也是上面 f° 良定义性的核心。

## 前瞻

关系的另一大类是**序关系**：自反、传递，但把对称换成**反对称**（x ≤ y 且 y ≤ x ⟹ x = y）。练习 (b)② 里的 ≤ 就是例子。序关系刻画「谁在谁前面」，是后面讨论[[num_estremo_superiore|上界与上确界]]的基础。
