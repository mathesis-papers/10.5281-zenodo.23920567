# 精确陈述与完整证明

设 $[n]=\{1,\ldots,n\}$，$n\geq1$。图案 $P_{n,L}$ 在相邻点间有双向弧，并且恰在 $L\subseteq[n]$ 有自环。矩阵具有这个图案，是说非零位置恰好等于这些弧与自环。若对每个实数 $n\times n$ 矩阵 $X$ 都有

$$
A\circ X=0,\quad AX^{\mathsf T}=X^{\mathsf T}A
\quad\Longrightarrow\quad X=0,
$$

则 $A$ 具有 nSSP。“允许”对具有精确支撑的矩阵取存在量词；“要求”取全称量词。下面对应原文共用一个计数器的 Theorem 1、Lemmas 2–4、Corollaries 5–6，证明依照这些原文论证改写。完整存在判据与单自环的等价刻画已有 Carptopus 的早期证明；奇数阶障碍来自 Koljančić–Oblak 的 Theorem 5.7(Cc)。

## 完整判据与偶数阶部分

::: {.theorem #thm-criterion title="完整存在判据" mathesis="collected:koljancic-oblak-2026-question-5-11-even-loop-path:2:s1" status="written-proof" proof="pf-thm-criterion" doi="10.5281/zenodo.23920568" source="Theorem 1, Section 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/156"}
双向路径 $P_{n,L}$ 允许 nSSP 当且仅当

$$
\begin{cases}
L\ne\varnothing,& n\text{ 为偶数},\\
L\cap\{1,3,\ldots,n\}\ne\varnothing,& n\text{ 为奇数}.
\end{cases}
$$

凡允许 nSSP 的图案，都有一个对称见证，其非零项全为正整数。
:::

::: {.theorem #thm-even title="偶数阶存在性" mathesis="collected:koljancic-oblak-2026-question-5-11-even-loop-path:2:s1" lean="D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPathNSSP.result"}
对每个正偶数 $n$ 和每个非空 $L\subseteq[n]$，存在实数 $n\times n$ 矩阵 $A$，其支撑恰为 $P_{n,L}$，且具有 nSSP；测试范围为全体实数矩阵 $X$，不要求对称或零对角。
:::

这恰是 [@thm-criterion] 的偶数阶存在性部分。其 Lean 陈述给出精确支撑的实数见证。对称与正整数结论属于上面的完整书面陈述。完整判据在支持引理之后的 [证明](#proof-main) 中建立。

## 从多项式变化恢复边参数

对实数序列 $q$，定义 continuant 及其线性变化为

$$
P_0=1,\quad P_1=x,\quad P_{k+2}=xP_{k+1}-q_kP_k,
$$

$$
\dot P_0=\dot P_1=0,
$$

$$
\dot P_{k+2}=x\dot P_{k+1}-\dot q_kP_k-q_k\dot P_k.
$$

对 $m$ 点支路，$q_0,\ldots,q_{m-2}$ 表示内部边，$q_{m-1}$ 表示连接中心的边。实际对称边权为 $b_k$ 时，$q_k=b_k^2$。归纳可得：$P_m$ 首一、次数为 $m$、奇偶性为 $m$；$\dot P_m$ 奇偶性相同，$m\geq2$ 时次数不超过 $m-2$。初始两个变化多项式为零。下述次数界均包含零多项式。

::: {.lemma #lem-branch title="递推恢复" mathesis="collected:koljancic-oblak-2026-question-5-11-even-loop-path:2:s2" lean="D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPath.branch_variation_injective"}
对任意整数 $m\geq0$、非零实参数 $q_0,\ldots,q_{m-1}$ 以及任意实变化 $\dot q_0,\ldots,\dot q_{m-1}$，若 $\dot P_m=\dot P_{m+1}=0$，则对每个 $0\leq k<m$ 都有 $\dot q_k=0$。
:::

::: {.proof #pf-lem-branch}
$m=0$ 时没有参数需要恢复。$m\geq1$ 时，由递推和两个零变化得到

$$
\dot q_{m-1}P_{m-1}+q_{m-1}\dot P_{m-1}=0.
$$

$P_{m-1}$ 首一，而 $\dot P_{m-1}$ 次数更低，所以 $x^{m-1}$ 的系数是 $\dot q_{m-1}$。故它为零；再用 $q_{m-1}\ne0$ 得到 $\dot P_{m-1}=0$。于是对连续两个零变化 $\dot P_{m-1},\dot P_m$ 向下归纳。$m=1$ 时 $P_0=1$、$\dot P_0=0$，同样成立。这就是原文 Lemma 2 及所引 Lean 定理的恢复论证。
:::

选定自环位置 $\ell$，令 $r=\ell-1$、$s=n-\ell$，两条支路都从远端向中心读取。它们的 continuant 记为 $P,Q$，令 $U=P_r$、$V=Q_s$。中心自环权重为 $a$ 时，沿中心展开 $\det(xI-A)$ 得到

$$
H=(x-a)UV-q_{r-1}P_{r-1}V-p_{s-1}UQ_{s-1},
$$

某条支路为空时省略相应项。代入递推可写成

$$
H=P_{r+1}V+UQ_{s+1}-(x+a)UV.
$$

$r=0$ 或 $s=0$ 时相应的两个 continuant 为 $1,x$，公式依然成立。

::: {.lemma #lem-joined title="连接恢复" mathesis="collected:koljancic-oblak-2026-question-5-11-even-loop-path:2:s3" status="written-proof" proof="pf-lem-joined" doi="10.5281/zenodo.23920568" source="Lemma 3, Section 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/154"}
设 $r,s\geq0$。若 $a\ne0$、两条支路的全部边参数（包括连接中心的边）非零，且 $U,V$ 互素，则 $\dot H=0$ 迫使 $\dot a=0$ 及所有边参数变化为零。
:::

::: {.proof #pf-lem-joined}
令 $T=\dot U V+U\dot V$。求导得到

$$
\dot H=W-aT-\dot aUV,
$$

$$
\begin{aligned}
W={}&\dot P_{r+1}V+P_{r+1}\dot V\\
 &+\dot UQ_{s+1}+U\dot Q_{s+1}-xT.
\end{aligned}
$$

$W$ 每项奇偶性为 $r+s+1$；$T$ 与 $UV$ 的奇偶性为 $r+s$。分离多项式的两种奇偶部分，得到 $W=0$ 和 $aT+\dot aUV=0$。$UV$ 首一且次数为 $r+s$，$T$ 次数严格更低；$r+s=0$ 时 $T=0$。比较最高次系数即得 $\dot a=0$；再由 $a\ne0$ 得到 $T=0$。

从 $\dot UV+U\dot V=0$ 及互素性可知 $U\mid\dot U$、$V\mid\dot V$。严格次数界迫使两个变化都为零。此时 $W=0$ 化为

$$
\dot P_{r+1}V+U\dot Q_{s+1}=0.
$$

再次利用互素性得到 $U\mid\dot P_{r+1}$、$V\mid\dot Q_{s+1}$。支路长度为正时，$\deg\dot P_{r+1}<r$、$\deg\dot Q_{s+1}<s$；长度为零时相应变化恒为零。所以这两个变化也为零。对两条支路分别应用 [@lem-branch] 即可。奇偶部分的分离对任意 $r,s$ 都成立，无须限制 $r+s$ 的奇偶性。这是原文 Lemma 3。
:::

## 选择整数边权

::: {.lemma #lem-separation title="整数权重分离" mathesis="collected:koljancic-oblak-2026-question-5-11-even-loop-path:2:s4" status="written-proof" proof="pf-lem-separation" doi="10.5281/zenodo.23920568" source="Lemma 4, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/155"}
若非负支路长度 $r,s$ 至少一个为偶数，则可以选择正整数边权（包括连接中心的边），使两条支路的特征多项式互素。
:::

::: {.proof #pf-lem-separation}
空支路的多项式是 1，另一侧任取正整数边权即可。否则选一条偶长度 $d\geq2$ 的支路，把它的内部边及连接边全取为 $M=d+1$，另一侧的边全取 1。零对角、常边权 $M$ 的 $d$ 点路径的特征值为

$$
2M\cos\left(\frac{j\pi}{d+1}\right),\qquad 1\leq j\leq d.
$$

验证方法是取第 $i$ 坐标为 $\sin(ij\pi/(d+1))$ 的向量，用正弦加法公式检查特征向量方程；边界坐标 $i=0,d+1$ 都为零。这 $d$ 个特征值互不相同，故已给出全部谱。$d$ 偶时，最小绝对值为

$$
2(d+1)\sin\left(\frac{\pi}{2(d+1)}\right)>2,
$$

其中用了 $0<t<\pi/2$ 时 $\sin t>2t/\pi$。同一公式说明单位边权支路的特征值全在 $(-2,2)$。故两边谱不相交。实对称矩阵的特征值全实，特征多项式在实数域分裂；没有共同根就互素。连接中心的边不影响删点后的支路谱，所选连接权重也都是正整数。这证明原文 Lemma 4。
:::

## 从恢复引理推出 nSSP {#proof-main}

::: {.proof #pf-thm-criterion}
先设可以选择自环 $\ell$，使至少一条支路长度为偶数。用 [@lem-separation] 选择边权，自环取 $a=1$，得到对称整数单自环矩阵 $A_0$。

先对任意边权非零、支路互素的实对称单自环路径证明 nSSP；这个论证也将用于 [@cor-spectral]。该矩阵的谱简单：特征向量的第一个坐标确定后，第一行给出第二个坐标，后面的行依次给出其余坐标，因为每条邻接边非零。第一个坐标若为零，整向量都为零。因此每个特征空间至多一维。由实对称谱定理，有正交矩阵 $O$ 使 $O^{\mathsf T}AO=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$，各 $\lambda_i$ 互异。

令 $\mathcal S$ 为支撑在 $n-1$ 条路径边及选定自环上的对称实矩阵空间，其维数为 $n$。考虑线性映射

$$
B\longmapsto\operatorname{diag}(O^{\mathsf T}BO)\in\mathbb R^n.
$$

若输出对角线为零，则 $\det(xI-A-tB)$ 在 $t=0$ 的导数为

$$
-\sum_i (O^{\mathsf T}BO)_{ii}\prod_{j\ne i}(x-\lambda_j)=0.
$$

这是在特征向量坐标的对角矩阵处对行列式求导：一阶项替换一行，仅该行对角项有贡献。故整个多项式导数 $\dot H=0$。边权 $b$ 对应平方参数变化 $\dot q=2b\dot b$。每个 $b\ne0$，所以 [@lem-joined] 迫使所有边与自环变化为零，即 $B=0$。映射在两个相同有限维数的空间间单射，因而也是满射。

现取任意通过 nSSP 测试的实矩阵 $X$。$Y=O^{\mathsf T}X^{\mathsf T}O$ 与 $\operatorname{diag}(\lambda_i)$ 交换。其非对角项满足 $(\lambda_i-\lambda_j)Y_{ij}=0$，所以 $Y=\operatorname{diag}(y_i)$。逐项消去条件对每个 $B\in\mathcal S$ 给出 $\operatorname{tr}(X^{\mathsf T}B)=0$。利用满射性选择一个 $B$，其谱坐标对角线恰为 $(y_i)$。迹在共轭下不变，于是

$$
0=\operatorname{tr}\bigl(YO^{\mathsf T}BO\bigr)=\sum_i y_i^2.
$$

所有 $y_i$ 都为零，故 $Y=X=0$。这里没有假设 $X$ 对称。

为添入剩余自环，把 nSSP 写为线性映射

$$
F_A:X\longmapsto(A\circ X,\ AX^{\mathsf T}-X^{\mathsf T}A)
$$

的单射性。固定基下系数连续依赖于 $A$。单射即满列秩，由一个非零极大子式见证；在 $A_0$ 的某邻域中它仍非零。令 $D=\sum_{j\in L\setminus\{\ell\}}E_{jj}$。则对所有充分大的正整数 $N$，$A_0+N^{-1}D$ 有 nSSP。因 $c\ne0$ 时 $F_{cA}=cF_A$，矩阵 $NA_0+D$ 有 nSSP，支撑恰好正确，保持对称，非零项全为正整数。不需要添加自环时取 $N=1$。

偶数阶有 $r+s=n-1$ 为奇数，任意自环选择都产生一条偶支路。奇数阶若 $\ell$ 为奇数，则两条支路都偶。构造包括 $n=1,L=\{1\}$，此时取矩阵 $(1)$。

证明必要性：$L=\varnothing$ 时，任意该图案的矩阵都有非零测试矩阵 $X=I$。若 $n=2k+1$ 且所有自环位于偶数点，把 $k+1$ 个奇数点排在 $k$ 个偶数点之前。任意该图案的矩阵（可以不对称）具有形式

$$
A=\begin{pmatrix}0&B\\C&D\end{pmatrix},
$$

$$
\begin{aligned}B&\in\mathbb R^{(k+1)\times k},\\C&\in\mathbb R^{k\times(k+1)}.\end{aligned}
$$

由维数，存在非零 $u,v\in\mathbb R^{k+1}$ 满足 $Cu=0$、$v^{\mathsf T}B=0$。在偶数点坐标补零，得到 $Au=0$、$v^{\mathsf T}A=0$。$X=vu^{\mathsf T}\ne0$ 仅支撑在奇数—奇数位置，而 $A$ 在那里为零。且 $X^{\mathsf T}=uv^{\mathsf T}$ 与 $A$ 的左右乘积都为零，故交换。这就是 Koljančić–Oblak 的障碍。必要性得证，也完成了原文 Theorem 1 的证明，依赖为 Lemmas 2–4 及第 4 节的添环论证。
:::

## 固定的单自环矩阵

::: {.corollary #cor-spectral title="单自环判据" mathesis="collected:koljancic-oblak-2026-question-5-11-even-loop-path:2:s5" status="written-proof" proof="pf-cor-spectral" doi="10.5281/zenodo.23920568" source="Corollary 5, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/157"}
对一个实对称、不可约三对角矩阵，若唯一非零对角项在 $\ell$ 处，则它有 nSSP 当且仅当删去 $\ell$ 后的两条支路的谱不相交。特别地，若边权全为 1，自环值任意非零，则有 nSSP 当且仅当 $\gcd(\ell,n+1)=1$。
:::

::: {.proof #pf-cor-spectral}
充分性就是 [前面证明](#proof-main) 中应用 [@lem-joined] 的谱对角映射论证。边权可以带符号，只要非零；其平方为正，且 $2b\dot b=0$ 仍推出 $\dot b=0$。

证明必要性：若两支路共有特征值 $\mu$，每条支路的对应特征向量在连接端坐标都非零，这由前面的端点递推可知。分别缩放，使它们在中心行的加权贡献相消。合并两边向量，在 $\ell$ 处补零，就得到非零 $z$，满足 $Az=\mu z$。设 $S$ 是沿路径正负交替的对角矩阵。零对角部分 $J=A-aE_{\ell\ell}$ 满足 $SJ=-JS$；又因 $z_\ell=0$，有 $A(Sz)=-\mu Sz$。因此

$$
X=zz^{\mathsf T}+(Sz)(Sz)^{\mathsf T}
$$

是与 $A$ 交换的对称矩阵。其迹为 $2\|z\|^2>0$，故非零。邻接位置的两项因交替符号而相消；自环位置因 $z_\ell=0$ 而为零。所以 $A\circ X=0$，与 nSSP 矛盾。这是归于 Carptopus 的 Theorem 4.1 的单自环障碍。

单位边权时，记 $b=n+1-\ell$，两支路的特征值分别为

$$
2\cos(j\pi/\ell),\qquad 1\leq j<\ell,
$$

$$
2\cos(k\pi/b),\qquad 1\leq k<b.
$$

余弦在 $(0,\pi)$ 上单射，共同特征值等价于某个真分数 $j/\ell=k/b$。这恰在 $d=\gcd(\ell,b)>1$ 时发生：若 $d>1$，取 $j=\ell/d$、$k=b/d$；反之把共同分数约分，其大于 1 的分母必同时整除 $\ell,b$。最后 $\gcd(\ell,b)=\gcd(\ell,n+1)$。端点的空支路没有特征值，对应分母为 1，也没有共同真分数。这包括 $n=1$。原文 Corollary 5 得证。
:::

## 推论与不要求性的例子

::: {.corollary #cor-families title="自环家族" mathesis="collected:koljancic-oblak-2026-question-5-11-even-loop-path:2:s6" status="written-proof" proof="pf-cor-families" doi="10.5281/zenodo.23920568" source="Corollary 6, Section 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/158"}
奇数 $n\geq3$、仅中心点有自环时，$n\equiv1\pmod4$ 的图案允许但不要求 nSSP；$n\equiv3\pmod4$ 时不允许。所有内部点有自环的图案在每个 $n\geq4$ 时允许但不要求 nSSP；$1\leq n\leq3$ 时不允许。单点且有自环的图案要求 nSSP。任一允许路径的有向超图案也允许 nSSP，并有非零项全为正整数的见证。
:::

::: {.proof #pf-cor-families}
中心点 $(n+1)/2$ 为奇数当且仅当 $n\equiv1\pmod4$，所以 [@thm-criterion] 给出存在性分类。每个奇数 $n\geq3$ 的单位边权中心自环矩阵都不满足最大公因数判据，因为 $\gcd((n+1)/2,n+1)=(n+1)/2>1$。在允许的同余类中，这就证明不要求性。

偶数 $n\geq4$ 的内部自环集非空；奇数 $n\geq5$ 的内部包含奇数位置 3，故两者都允许。$n=1,2$ 时内部为空；$n=3$ 时唯一内部点为偶数，故这些小阶均不允许。

为证不要求性，令 $C$ 为单位边权路径矩阵，两个端点各有权重 1 的自环；令 $E$ 为全 1 矩阵。$C$ 的每行、每列和都为 2，故 $CE=EC=2E$。置

$$
B=I-C,\qquad Y=I-E+C.
$$

$B$ 恰在内部点对角处非零，每条邻接边也非零，故具有所需图案。$Y$ 在这些位置都为零：内部对角是 $1-1+0$，邻接处是 $0-1+1$。非邻接处如 $n\geq3$ 时的 $(1,3)$，$Y=-1$，所以 $Y\ne0$。$I,C,E$ 彼此交换，故 $BY=YB$；$Y$ 又对称，因此是 $B$ 的非零 nSSP 测试矩阵。这个构造对应 Koljančić–Oblak 的 Theorem 5.7(A)。

$n=1$ 且有自环时，$A=(a)$、$a\ne0$，由 $A\circ X=0$ 直接得到 $X=0$。

最后，取允许路径的正整数见证 $A_0$，令 $D$ 在每个新增有向弧处为 1、其余为零。由同一开放性论证，充分大的正整数 $N$ 使 $A_0+N^{-1}D$ 有 nSSP；整体缩放得到精确超图案见证 $NA_0+D$。新增弧有方向时不要求这个见证对称。至此证明原文 Corollary 6；文献中保持相似性的 Superpattern Lemma 比这里的存在性结论更强。
:::
