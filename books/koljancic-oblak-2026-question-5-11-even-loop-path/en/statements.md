# Precise statements and complete proofs

Write $[n]=\{1,\ldots,n\}$, $n\geq1$. The pattern $P_{n,L}$ has both arcs between consecutive vertices and exactly the loops at $L\subseteq[n]$. A matrix has this pattern when its nonzero entries are exactly these positions. It has nSSP if, for every real $n\times n$ matrix $X$,

$$
A\circ X=0,\quad AX^{\mathsf T}=X^{\mathsf T}A
\quad\Longrightarrow\quad X=0.
$$

“Allows” is existential over matrices with that exact support; “requires” is universal. The statements below correspond to the manuscript's Theorem 1, Lemmas 2–4 and Corollaries 5–6, which share one numbering counter. Proofs are adapted from those source arguments. Carptopus previously proved the full existence criterion and single-loop equivalence; the odd-order obstruction is Koljančić–Oblak's Theorem 5.7(Cc).

## The criterion and its even-order part

::: {.theorem #thm-criterion title="Full existence criterion" mathesis="collected:koljancic-oblak-2026-question-5-11-even-loop-path:2:s1" status="written-proof" proof="pf-thm-criterion" doi="10.5281/zenodo.23920568" source="Theorem 1, Section 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/156"}
The double path $P_{n,L}$ allows nSSP if and only if

$$
\begin{cases}
L\ne\varnothing,& n\text{ even},\\
L\cap\{1,3,\ldots,n\}\ne\varnothing,& n\text{ odd}.
\end{cases}
$$

Whenever it allows nSSP, it has a symmetric witness with positive integer nonzero entries.
:::

::: {.theorem #thm-even title="Even-order existence" mathesis="collected:koljancic-oblak-2026-question-5-11-even-loop-path:2:s1" lean="D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPathNSSP.result"}
For every positive even integer $n$ and every nonempty $L\subseteq[n]$, there exists a real $n\times n$ matrix $A$ with exact support $P_{n,L}$ and nSSP, tested against all real $X$ without symmetry or diagonal restrictions.
:::

This is the exact even-order existential part of [@thm-criterion]. Its Lean statement asserts real existence and exact support. The symmetry and positive-integer conclusions belong to the broader written statement above. The full criterion is proved after its supporting lemmas, in [the proof below](#proof-main).

## Recovering edge variations

For a real sequence $q$ define the continuants and their linearized variations by

$$
P_0=1,\quad P_1=x,\quad P_{k+2}=xP_{k+1}-q_kP_k,
$$

$$
\dot P_0=\dot P_1=0,
$$

$$
\dot P_{k+2}=x\dot P_{k+1}-\dot q_kP_k-q_k\dot P_k.
$$

For a branch of $m$ vertices, parameters $q_0,\ldots,q_{m-2}$ describe its internal edges and $q_{m-1}$ its attachment to the center. For actual symmetric edges $b_k$, $q_k=b_k^2$. Induction gives: $P_m$ is monic of degree $m$ and parity $m$; $\dot P_m$ has the same parity and degree at most $m-2$ for $m\geq2$. The initial variations are zero. Degree inequalities below include the zero polynomial.

::: {.lemma #lem-branch title="Backward recovery" mathesis="collected:koljancic-oblak-2026-question-5-11-even-loop-path:2:s2" lean="D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPath.branch_variation_injective"}
For every integer $m\geq0$, real parameters $q_0,\ldots,q_{m-1}\ne0$, and arbitrary real variations $\dot q_0,\ldots,\dot q_{m-1}$, if $\dot P_m=\dot P_{m+1}=0$, then $\dot q_k=0$ for every $0\leq k<m$.
:::

::: {.proof #pf-lem-branch}
For $m=0$ there is nothing to recover. For $m\geq1$, the recurrence and the two zero variations give

$$
\dot q_{m-1}P_{m-1}+q_{m-1}\dot P_{m-1}=0.
$$

The coefficient of $x^{m-1}$ is $\dot q_{m-1}$, since $P_{m-1}$ is monic and $\dot P_{m-1}$ has lower degree. Thus $\dot q_{m-1}=0$. Nonvanishing of $q_{m-1}$ then gives $\dot P_{m-1}=0$. Descend to length $m-1$ with the consecutive zero variations $\dot P_{m-1},\dot P_m$. This also handles $m=1$, where $P_0=1$ and $\dot P_0=0$. This is the recovery argument of manuscript Lemma 2 and the cited Lean theorem.
:::

Take a chosen loop at $\ell$, put $r=\ell-1$, $s=n-\ell$, and read both branches from their far endpoints toward the center. Use $P$ and $Q$ for their continuants, with $U=P_r$, $V=Q_s$. If the central loop has weight $a$, expansion of $\det(xI-A)$ at that vertex gives

$$
H=(x-a)UV-q_{r-1}P_{r-1}V-p_{s-1}UQ_{s-1},
$$

omitting a branch term when its length is zero. Substituting the recurrence yields

$$
H=P_{r+1}V+UQ_{s+1}-(x+a)UV.
$$

This formula includes $r=0$ or $s=0$: the corresponding continuants are $1,x$.

::: {.lemma #lem-joined title="Joined recovery" mathesis="collected:koljancic-oblak-2026-question-5-11-even-loop-path:2:s3" status="written-proof" proof="pf-lem-joined" doi="10.5281/zenodo.23920568" source="Lemma 3, Section 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/154"}
Let $r,s\geq0$. If $a\ne0$, all edge parameters on both branches (including their attaching edges) are nonzero, and $U,V$ are coprime, then $\dot H=0$ forces $\dot a=0$ and every edge-parameter variation to vanish.
:::

::: {.proof #pf-lem-joined}
Set $T=\dot U V+U\dot V$. Differentiation gives

$$
\dot H=W-aT-\dot aUV,
$$

$$
\begin{aligned}
W={}&\dot P_{r+1}V+P_{r+1}\dot V\\
 &+\dot UQ_{s+1}+U\dot Q_{s+1}-xT.
\end{aligned}
$$

All terms of $W$ have parity $r+s+1$; $T$ and $UV$ have parity $r+s$. The two polynomial parities therefore give $W=0$ and $aT+\dot aUV=0$. Since $UV$ is monic of degree $r+s$ and $T$ has strictly lower degree (or is zero when $r+s=0$), its top coefficient gives $\dot a=0$. As $a\ne0$, $T=0$.

From $\dot UV+U\dot V=0$ and coprimality, $U\mid\dot U$ and $V\mid\dot V$. Strict degree bounds force both variations to vanish. Now $W=0$ reduces to

$$
\dot P_{r+1}V+U\dot Q_{s+1}=0.
$$

Coprimality again gives $U\mid\dot P_{r+1}$ and $V\mid\dot Q_{s+1}$. For a positive branch length, $\deg\dot P_{r+1}<r$ and $\deg\dot Q_{s+1}<s$; for a zero length the corresponding variation is identically zero. Thus these two variations vanish. Apply [@lem-branch] on each branch. The separation into opposite polynomial parities works for every $r,s$, without a parity restriction on $r+s$. This is manuscript Lemma 3.
:::

## Choosing integer branch weights

::: {.lemma #lem-separation title="Integer separation" mathesis="collected:koljancic-oblak-2026-question-5-11-even-loop-path:2:s4" status="written-proof" proof="pf-lem-separation" doi="10.5281/zenodo.23920568" source="Lemma 4, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/155"}
If at least one of the nonnegative branch lengths $r,s$ is even, the branches can be chosen with positive integer edge weights, including their attachments, and coprime characteristic polynomials.
:::

::: {.proof #pf-lem-separation}
An empty branch has polynomial 1, so any positive integer weights on the other branch suffice. Otherwise choose an even branch length $d\geq2$. Give its internal and attaching edges weight $M=d+1$, and every edge on the other side weight 1. A zero-diagonal $d$-point path with constant weight $M$ has eigenvalues

$$
2M\cos\left(\frac{j\pi}{d+1}\right),\qquad 1\leq j\leq d.
$$

Indeed, the vector with $i$th coordinate $\sin(ij\pi/(d+1))$ satisfies the eigenvector equation by the sine addition identity, including zero boundary coordinates at $i=0,d+1$. These $d$ eigenvalues are distinct, so they exhaust the spectrum. Since $d$ is even, the least absolute value is

$$
2(d+1)\sin\left(\frac{\pi}{2(d+1)}\right)>2,
$$

using $\sin t>2t/\pi$ for $0<t<\pi/2$. The unit-weight branch has all eigenvalues strictly between $-2$ and $2$ by the same formula. Hence the spectra are disjoint. Real symmetric matrices have real eigenvalues and characteristic polynomials splitting over $\mathbb R$; disjoint roots mean coprime polynomials. Attachments do not change the spectra of the branches after deletion, and the chosen attaching weights are positive integers. This proves manuscript Lemma 4.
:::

## From recovery to nSSP {#proof-main}

::: {.proof #pf-thm-criterion}
First suppose a loop $\ell$ can be selected so that at least one branch length is even. Use [@lem-separation] and loop weight $a=1$ to form the symmetric integer one-loop matrix $A_0$.

We first explain why coprime branches imply nSSP for any real symmetric one-loop path with nonzero edges; the argument will also be used for [@cor-spectral]. Such a matrix has simple spectrum. For an eigenvector, the first row determines its second coordinate from its first, and successive rows determine every subsequent coordinate because each adjacent edge is nonzero. A zero first coordinate forces the whole vector to vanish. Each eigenspace has dimension at most one; the symmetric spectral theorem yields an orthogonal $O$ and distinct real eigenvalues with $O^{\mathsf T}AO=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$.

Let $\mathcal S$ be the real space of symmetric matrices supported on the $n-1$ path edges and the chosen loop. It has dimension $n$. Consider the linear map

$$
B\longmapsto\operatorname{diag}(O^{\mathsf T}BO)\in\mathbb R^n.
$$

If this diagonal is zero, the derivative of $\det(xI-A-tB)$ at $t=0$ is

$$
-\sum_i (O^{\mathsf T}BO)_{ii}\prod_{j\ne i}(x-\lambda_j)=0.
$$

This follows by differentiating the determinant at the diagonal matrix in eigenvector coordinates; a first-order term replaces one row, and only its diagonal entry contributes. Thus the whole polynomial derivative $\dot H$ is zero. For an edge $b$, the squared parameter changes by $\dot q=2b\dot b$. Each $b\ne0$, so [@lem-joined] forces all edge changes and the loop change to vanish: $B=0$. The map is injective between spaces of equal finite dimension, and therefore surjective.

Let any unrestricted real $X$ pass the nSSP tests. Then $Y=O^{\mathsf T}X^{\mathsf T}O$ commutes with $\operatorname{diag}(\lambda_i)$. Its off-diagonal entries satisfy $(\lambda_i-\lambda_j)Y_{ij}=0$, so $Y=\operatorname{diag}(y_i)$. For every $B\in\mathcal S$, entrywise annihilation gives $\operatorname{tr}(X^{\mathsf T}B)=0$. By surjectivity choose $B$ whose spectral diagonal is $(y_i)$. Invariance of trace now gives

$$
0=\operatorname{tr}\bigl(YO^{\mathsf T}BO\bigr)=\sum_i y_i^2.
$$

All $y_i$ vanish, hence $Y=X=0$. No symmetry assumption on $X$ was used.

To add the remaining loops, view nSSP as injectivity of the linear map

$$
F_A:X\longmapsto(A\circ X,\ AX^{\mathsf T}-X^{\mathsf T}A).
$$

In fixed bases its entries depend continuously on $A$. Injectivity is full column rank, witnessed by a nonzero maximal minor; its nonzero value persists in a neighborhood of $A_0$. Let $D=\sum_{j\in L\setminus\{\ell\}}E_{jj}$. Therefore $A_0+N^{-1}D$ has nSSP for all sufficiently large positive integers $N$. Since $F_{cA}=cF_A$ for $c\ne0$, $NA_0+D$ has nSSP, exact support, symmetry and positive integer nonzero entries. If no loops are added, take $N=1$.

For even $n$, $r+s=n-1$ is odd, so every loop choice gives an even branch. For odd $n$ and odd $\ell$, both branches are even. The construction includes $n=1,L=\{1\}$: take the matrix $(1)$.

For necessity, if $L=\varnothing$, the nonzero matrix $X=I$ passes both tests for every matrix of the pattern. If $n=2k+1$ and all loops are even, order the $k+1$ odd vertices before the $k$ even vertices. An arbitrary, possibly nonsymmetric, matrix of this pattern has form

$$
A=\begin{pmatrix}0&B\\C&D\end{pmatrix},
$$

$$
\begin{aligned}B&\in\mathbb R^{(k+1)\times k},\\C&\in\mathbb R^{k\times(k+1)}.\end{aligned}
$$

Dimension gives nonzero $u,v\in\mathbb R^{k+1}$ with $Cu=0$ and $v^{\mathsf T}B=0$. Extend them by zero on the even vertices. Then $Au=0$, $v^{\mathsf T}A=0$, and $X=vu^{\mathsf T}\ne0$ is supported on odd–odd positions, where $A$ is zero. Furthermore $X^{\mathsf T}=uv^{\mathsf T}$ commutes with $A$, since both products are zero. This is Koljančić–Oblak's obstruction. It proves necessity and completes manuscript Theorem 1, using Lemmas 2–4 and Section 4's enlargement argument.
:::

## A fixed single-loop matrix

::: {.corollary #cor-spectral title="Single-loop criterion" mathesis="collected:koljancic-oblak-2026-question-5-11-even-loop-path:2:s5" status="written-proof" proof="pf-cor-spectral" doi="10.5281/zenodo.23920568" source="Corollary 5, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/157"}
For a real symmetric irreducible tridiagonal matrix with exactly one nonzero diagonal entry, at $\ell$, nSSP holds if and only if the two branches obtained by deleting $\ell$ have disjoint spectra. In particular, if every edge has weight 1 and the loop has any nonzero value, nSSP holds exactly when $\gcd(\ell,n+1)=1$.
:::

::: {.proof #pf-cor-spectral}
The sufficiency argument is the spectral-diagonal map in [the preceding proof](#proof-main), using [@lem-joined]. It applies to any signed nonzero edges, since their squares are positive and $2b\dot b=0$ still implies $\dot b=0$.

For necessity, suppose the branches share an eigenvalue $\mu$. Each branch eigenvector has a nonzero coordinate at its attachment, by the same endpoint recurrence used for simple spectrum. Rescale the two eigenvectors so their weighted contributions at the central row cancel. Combining them and putting zero at $\ell$ gives a nonzero vector $z$ with $Az=\mu z$. Let $S$ be the diagonal matrix with alternating signs along the path. The zero-diagonal part $J=A-aE_{\ell\ell}$ satisfies $SJ=-JS$. As $z_\ell=0$, $A(Sz)=-\mu Sz$. Therefore

$$
X=zz^{\mathsf T}+(Sz)(Sz)^{\mathsf T}
$$

is nonzero, symmetric, and commutes with $A$. It is nonzero because its trace is $2\|z\|^2>0$. At each neighboring pair the two outer-product entries cancel because the signs alternate; at the loop they vanish because $z_\ell=0$. Thus $A\circ X=0$, contradicting nSSP. This is the single-loop obstruction credited to Carptopus, Theorem 4.1.

For unit edges, put $b=n+1-\ell$. The branch eigenvalues are

$$
2\cos(j\pi/\ell),\qquad 1\leq j<\ell,
$$

$$
2\cos(k\pi/b),\qquad 1\leq k<b.
$$

Cosine is injective on $(0,\pi)$, so a common eigenvalue is equivalent to $j/\ell=k/b$ for an interior fraction. Such a fraction exists exactly when $d=\gcd(\ell,b)>1$: for $d>1$, use $j=\ell/d$, $k=b/d$; conversely a reduced common fraction has denominator greater than 1 dividing both $\ell$ and $b$. Finally $\gcd(\ell,b)=\gcd(\ell,n+1)$. An endpoint branch is empty, its denominator is 1, and there is no common eigenvalue. This includes $n=1$. This proves manuscript Corollary 5.
:::

## Consequences and failures of requirement

::: {.corollary #cor-families title="Loop families" mathesis="collected:koljancic-oblak-2026-question-5-11-even-loop-path:2:s6" status="written-proof" proof="pf-cor-families" doi="10.5281/zenodo.23920568" source="Corollary 6, Section 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/158"}
For odd $n\geq3$ with the sole loop at the central vertex, the pattern allows but does not require nSSP when $n\equiv1\pmod4$, and does not allow nSSP when $n\equiv3\pmod4$. The pattern with loops at all interior vertices allows but does not require nSSP for every $n\geq4$; for $1\leq n\leq3$ it does not allow nSSP. The one-point pattern with its loop requires nSSP. Every directed superpattern of an allowing path also allows nSSP with a positive-integer witness.
:::

::: {.proof #pf-cor-families}
The central vertex $(n+1)/2$ is odd precisely when $n\equiv1\pmod4$, so [@thm-criterion] gives the existence alternatives. For every odd $n\geq3$, the unit-edge central-loop matrix fails the gcd test because $\gcd((n+1)/2,n+1)=(n+1)/2>1$. In the allowing class this proves nonrequirement.

For even $n\geq4$, the interior loop set is nonempty. For odd $n\geq5$, it contains the odd position 3. Thus both allow. For $n=1,2$ the interior is empty, and for $n=3$ its sole vertex is even, so none of these smaller patterns allows.

To show nonrequirement, let $C$ be the unit-edge path matrix with unit loops at its two endpoints, and let $E$ be the all-ones matrix. Each row and column sum of $C$ is 2, hence $CE=EC=2E$. Put

$$
B=I-C,\qquad Y=I-E+C.
$$

Then $B$ has nonzero diagonal exactly at interior vertices and nonzero entries on every path edge, so it has the required pattern. On these support positions $Y$ is zero: its interior diagonal is $1-1+0$, and its neighbor entries are $0-1+1$. At a nonneighbor position, for example $(1,3)$ when $n\geq3$, $Y=-1$, so $Y\ne0$. Since $I,C,E$ commute, $BY=YB$; $Y$ is symmetric, hence it is a nonzero nSSP test matrix for $B$. This is the construction related to Koljančić–Oblak's Theorem 5.7(A).

For $n=1$ with its loop, $A=(a)$, $a\ne0$, and $A\circ X=0$ directly forces $X=0$.

Finally let $A_0$ be a positive-integer witness for an allowing path and let $D$ equal 1 at each added directed arc and 0 elsewhere. The same openness argument gives $A_0+N^{-1}D$ with nSSP for all sufficiently large positive integers $N$. Scaling gives the exact superpattern witness $NA_0+D$. It need not be symmetric when the added arcs are directed. This proves manuscript Corollary 6; the literature's similarity-preserving Superpattern Lemma is stronger than this existence consequence.
:::
