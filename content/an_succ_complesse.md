---
id: an_succ_complesse
label: 复数列的收敛
parent: an_analisi
prerequisites: [an_algebra_limiti, alg_complessi]
summary: 复数列 (zₙ) 收敛 当且仅当 实部 (Re zₙ) 与虚部 (Im zₙ) 分别收敛,且 lim zₙ = lim Re zₙ + i·lim Im zₙ——把复数列的收敛拆成两个实数列的收敛。
status: learning
refs: Amann–Escher, Analysis I §II.2
---

## 把复数列拆成两个实数列

[[an_convergenza|收敛]]的定义对 [[alg_complessi|ℂ]] 一字通用——复数列 (zₙ) 收敛到 a,就是 |zₙ − a| → 0。但 ℂ 没有序,夹逼用不上,运算法则虽然能用却常嫌笨重。这一节给出一个把复数列收敛**完全转译**成实数列收敛的判据:只需分别看实部和虚部。这样一来,ℂ 上的极限问题就化归到熟悉的 ℝ 上,前面所有实数列的工具(运算法则、夹逼)都能间接用上。

先补一条对 ℝ、ℂ 都成立的小结论。

**命题(模的连续性).** 若 zₙ → a(在 K 中),则 |zₙ| → |a|。

**证明.** 给定 ε > 0,取 N 使 n ≥ N 时 |zₙ − a| < ε。由[[an_valore_assoluto|反向三角不等式]],

| |zₙ| − |a| | ≤ |zₙ − a| < ε，  n ≥ N。

故 |zₙ| → |a|。∎

（这条[[an_convergenza|上一节练习]]在实数情形证过;反向三角不等式对复数的模同样成立,所以证明一字不变。它说「取模」这个操作不破坏收敛——逼近 a 的点,其到原点的距离也逼近 a 到原点的距离。）

## 主定理：实部虚部分别收敛

**定理.** 设 (zₙ) 是复数列。则以下等价:

(i) (zₙ) 收敛;
(ii) 实部 (Re zₙ) 与虚部 (Im zₙ) 都收敛(作为实数列)。

且此时

lim zₙ = lim (Re zₙ) + i·lim (Im zₙ)。

几何上,这再自然不过:把 zₙ 看成平面上的点,它趋近 a,等价于它的**横坐标趋近 a 的横坐标、纵坐标趋近 a 的纵坐标**——平面上的逼近,就是两个方向上的逼近同时发生。

<svg viewBox="0 0 380 300" xmlns="http://www.w3.org/2000/svg">
  <!-- 轴 -->
  <line x1="50" y1="230" x2="288" y2="230" stroke="#888" stroke-width="1.2"/>
  <line x1="70" y1="249" x2="70" y2="68" stroke="#888" stroke-width="1.2"/>
  <path d="M 288 230 L 280 226 L 280 234 z" fill="#888"/>
  <path d="M 70 68 L 66 76 L 74 76 z" fill="#888"/>
  <text x="292" y="234" font-size="11" fill="#555">Re</text>
  <text x="58" y="76" font-size="11" fill="#555">Im</text>
  <!-- 刻度 -->
  <line x1="165" y1="227" x2="165" y2="233" stroke="#888" stroke-width="0.8"/>
  <text x="165" y="245" font-size="10" text-anchor="middle" fill="#999">1</text>
  <line x1="260" y1="227" x2="260" y2="233" stroke="#888" stroke-width="0.8"/>
  <text x="260" y="245" font-size="10" text-anchor="middle" fill="#999">2</text>
  <line x1="67" y1="135" x2="73" y2="135" stroke="#888" stroke-width="0.8"/>
  <text x="60" y="139" font-size="10" text-anchor="end" fill="#999">i</text>
  <!-- 极限 a -->
  <circle cx="184" cy="144" r="4.5" fill="#E0612F"/>
  <text x="192" y="140" font-size="12" fill="#E0612F">a</text>
  <!-- a 的投影 -->
  <line x1="184" y1="144" x2="184" y2="230" stroke="#E0612F" stroke-width="0.8" stroke-dasharray="3,3"/>
  <line x1="184" y1="144" x2="70" y2="144" stroke="#E0612F" stroke-width="0.8" stroke-dasharray="3,3"/>
  <circle cx="184" cy="230" r="3" fill="#E0612F" opacity="0.7"/>
  <circle cx="70" cy="144" r="3" fill="#E0612F" opacity="0.7"/>
  <text x="184" y="262" font-size="9" text-anchor="middle" fill="#E0612F">Re a</text>
  <text x="44" y="148" font-size="9" fill="#E0612F">Im a</text>
  <!-- 螺旋数列点 -->
  <polyline points="221,73 160,112 157,149 178,164 195,156 197,140 186,133 176,139 176,149" fill="none" stroke="#5A5FE0" stroke-width="0.9" opacity="0.45"/>
  <g fill="#5A5FE0">
    <circle cx="221" cy="73" r="2.8"/><circle cx="160" cy="112" r="2.8"/><circle cx="157" cy="149" r="2.8"/><circle cx="178" cy="164" r="2.8"/><circle cx="195" cy="156" r="2.8"/><circle cx="197" cy="140" r="2.8"/><circle cx="186" cy="133" r="2.8"/><circle cx="176" cy="139" r="2.8"/><circle cx="176" cy="149" r="2.8"/></g>
  <text x="225" y="70" font-size="10" fill="#5A5FE0">zₙ</text>
  <text x="200" y="290" font-size="10" text-anchor="middle" fill="#777">zₙ 在平面上趋近 a ⟺ 两个坐标投影各自趋近 Re a、Im a</text>
</svg>

**证明.** 关键是两组不等式,把「复数的模」与「实部虚部的绝对值」互相控制。对任意 z = x + iy(x = Re z,y = Im z):

|Re z| ≤ |z|,  |Im z| ≤ |z|，  且   |z| ≤ |Re z| + |Im z|。

前两条来自[[alg_complessi|模的性质]](|x| = √(x²) ≤ √(x²+y²) = |z|);第三条由 |z| = √(x²+y²) ≤ √(x²) + √(y²) = |x| + |y|（或三角不等式）。

**(i) ⟹ (ii).** 设 zₙ → a,记 a = Re a + i·Im a。由前两条不等式(用在 zₙ − a 上):

|Re zₙ − Re a| = |Re(zₙ − a)| ≤ |zₙ − a|，

而 |zₙ − a| → 0,由「被零数列压住」,|Re zₙ − Re a| → 0,即 Re zₙ → Re a。虚部同理 Im zₙ → Im a。

**(ii) ⟹ (i).** 设 Re zₙ → α、Im zₙ → β,令 a := α + iβ。由第三条不等式(用在 zₙ − a 上):

|zₙ − a| ≤ |Re zₙ − α| + |Im zₙ − β|，

右边两项都是零数列,其和也是零数列([[an_algebra_limiti|和法则]]),故 |zₙ − a| → 0,即 zₙ → a。

两个方向都成立,且极限 a = α + iβ = lim Re zₙ + i·lim Im zₙ。∎

这条定理的实际意义:**复数列的收敛,被一劳永逸地化简成两个实数列的收敛**。算复数列极限时,拆出实部虚部,各自用实数列的工具(运算法则、夹逼)算清,再用 lim zₙ = lim Re + i·lim Im 拼回去。下面是范例。

## 一个例子

求 lim zₙ,其中 zₙ = (n+1)/(n+2) + i·(2n²)/(n²+1)。

拆开看两部分。实部 Re zₙ = (n+1)/(n+2),[[an_algebra_limiti|上一节]]算过 → 1。虚部 Im zₙ = (2n²)/(n²+1),分子分母同除 n²:2/(1 + 1/n²) → 2/(1+0) = 2(运算法则)。两部分都收敛,由定理

lim zₙ = 1 + i·2 = 1 + 2i。∎

整个过程没碰一次复数的 ε–N——拆成两个实数列,各自用熟悉的法则,拼回去。

## 一道激活练习

用实部虚部判据求下列复数列的极限(或判定发散):

(a) zₙ = (3n)/(n+1) + i·(1 − 1/n)；
(b) zₙ = (1/n)·(cos n + i·sin n)（提示:实部虚部各自夹逼;cos、sin 有界）；
(c) zₙ = iⁿ（提示:看它的实部数列 Re(iⁿ) 是什么——回忆 [[alg_complessi|i 的四周期]];这个实部数列收敛吗？）。

## 参考解答

(建议先自己写完再看。)

**(a)** 实部 (3n)/(n+1) = 3/(1+1/n) → 3。虚部 1 − 1/n → 1。两部分都收敛,故 **lim zₙ = 3 + i**。

**(b)** 实部 (cos n)/n:由 −1 ≤ cos n ≤ 1 得 −1/n ≤ (cos n)/n ≤ 1/n,[[an_confronto|夹逼]]给 → 0。虚部 (sin n)/n 同理 → 0。两部分都 → 0,故 **lim zₙ = 0 + 0i = 0**。

**(c)** zₙ = iⁿ 循环取值 1, i, −1, −i, 1, i, …（[[alg_complessi|i 的四周期]]）。看实部数列 Re(iⁿ):依次是 Re(1)=1, Re(i)=0, Re(−1)=−1, Re(−i)=0,即 1, 0, −1, 0, 1, 0, −1, 0, …——这个实数列有三个聚点 1, 0, −1,**发散**([[an_sottosuccessioni|子列]]判据:取下标 ≡0 (mod 4) 的子列恒为 1、≡2 的恒为 −1,两子列极限不同)。实部都不收敛,由本节定理,(iⁿ) **发散**。∎（这也印证了[[alg_complessi|i 的四周期]]:iⁿ 永远在四个值间跳,不向任何单点靠拢。）

回顾:复数列收敛与否,全看实部虚部两个实数列——**有一个发散,整个复数列就发散**(如 (c));两个都收敛,极限就是两个实极限拼成的复数。这把 ℂ 上所有收敛问题,都拉回了 ℝ 的地盘。

## 往前看一步

§II.2 的运算法则到此完整:实数列的和差积商与序(夹逼),复数列的实虚拆分,都已就位。但所有这些工具有一个共同的前提——**它们只能处理已知收敛、或能被夹住的数列**。还有一大类数列,我们能看出它「在往一个方向走」,却既拆不开、也找不到夹板,比如单调递增有上界的 (1 + 1/n)ⁿ。要断定这类数列收敛,运算法则和夹逼都无能为力,必须回到 ℝ 最深的性质:**完备性**。下一节,完备性将第一次在极限理论里正面登场——证明「单调递增且有上界的实数列必收敛」。这就是 [[an_monotone|单调收敛定理]] 的内容,也是通向 e 与无穷级数的门。
