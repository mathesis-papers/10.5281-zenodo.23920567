# Choosing weights for a path

Take a row of points joined to their neighbors in both directions, and add loops at selected points. Can we put nonzero real weights on these connections so that the resulting table has no hidden algebraic obstruction? S. Koljančić and P. Oblak's Question 5.11 asks this for an even number of points. The answer is yes whenever at least one loop is present. The paper gives the full existence criterion as well: for an odd number of points, at least one loop must be at an odd-numbered position, counting from an endpoint. Every admissible pattern has a symmetric example whose nonzero entries are positive integers.

This is an explanation of version 2 of the paper by Haobo Ma and Wenlin Zhang. Their manuscript credits Carptopus with an earlier proof of the full existence criterion and the single-loop spectral characterization, dated 19 August 2026 and revised 22 August. The present paper gives an explicit integer construction, a greatest-common-divisor test for unit edge weights, and classifications of two loop families. [Sources and contributions](sources.md) identifies the original question, earlier proof, and present paper.

## How a table records a path

Start with five points numbered $1,2,3,4,5$, both arrows between each neighboring pair, and a loop only at point 3. Record the weights in a real $5\times5$ matrix $A$: the entry $A_{ij}$ is the weight from $i$ to $j$. An arrow requires a nonzero entry; a missing arrow requires zero. A symmetric choice gives opposite arrows equal weights. For example,

$$
A=\begin{pmatrix}
0&3&0&0&0\\
3&0&3&0&0\\
0&3&1&1&0\\
0&0&1&0&1\\
0&0&0&1&0
\end{pmatrix}.
$$

A pattern **allows** a property if at least one choice of its weights has it. It **requires** that property if every legal choice has it. A single pattern can have both successful and unsuccessful choices. This five-point pattern does: unit edge weights fail, while changing the two edges on the left to 3 succeeds.

The property here is the non-symmetric Strong Spectral Property, abbreviated nSSP. It is a linear algebra test. Take any real matrix $X$ and impose

$$
A\circ X=0,
$$

$$
AX^{\mathsf T}=X^{\mathsf T}A.
$$

The first product is entry by entry: wherever $A$ is nonzero, $X$ must be zero. The second equation says that $A$ and the transpose of $X$ commute: their multiplication order makes no difference. If the zero matrix is the only $X$ passing both tests, $A$ has nSSP. The test matrix need not be symmetric and has no imposed zero diagonal. Choosing a symmetric $A$ does not restrict the test.

A two-point calculation makes the test tangible. Choose

$$
A=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
$$

The entrywise condition leaves only one possible unknown:

$$
X=\begin{pmatrix}0&0\\0&t\end{pmatrix}.
$$

Ordinary matrix multiplication takes the dot product of a row with a column. Here it gives

$$
AX^{\mathsf T}=\begin{pmatrix}0&t\\0&0\end{pmatrix},
$$

$$
X^{\mathsf T}A=\begin{pmatrix}0&0\\t&0\end{pmatrix}.
$$

Equality forces $t=0$. This is an nSSP witness on two points with one loop. It also shows why we must allow diagonal entries in $X$: the test itself, rather than a preliminary restriction, eliminates $t$.

## Remove the looped point and inspect the branches

Remove point 3 in the example. Two paths of two points remain. A two-point branch has matrix

$$
\begin{pmatrix}0&b\\b&0\end{pmatrix}.
$$

It multiplies the vector $(1,1)$ by $b$ and $(1,-1)$ by $-b$. Such multipliers are called eigenvalues; their collection is the spectrum. Thus the left branch has spectrum $\{-3,3\}$ and the right branch has $\{-1,1\}$. They are disjoint.

The paper proves that a symmetric path matrix with nonzero neighboring weights and exactly one nonzero loop has nSSP precisely when these two branch spectra are disjoint. Unit weights give identical two-point branches and fail. The displayed weights separate their spectra and succeed. The edges attaching the branches to the center also have nonzero weights, and the central loop is 1. [Precise statements and proofs](statements.md) gives the equivalence, including an empty branch when the loop is at an endpoint.

The film follows this example through spectral separation, recovery of weight changes, and insertion of additional loops.

::: {.film src="001-separated-branches"}
Two branches of a five-point path: unit weights share eigenvalues; weights 3 on the left and 1 on the right separate their spectra.
:::

## Why parity controls existence

Number the $n$ points $1,\ldots,n$ from an endpoint and let $L$ be the loop set. The criterion is ready to use:

| Number of points | Necessary and sufficient condition for allowing nSSP | Example |
| --- | --- | --- |
| $n$ even | $L$ is nonempty | On six points, a loop at any position suffices |
| $n$ odd | $L$ contains an odd position | On five points, a loop at 3 works; a sole loop at 2 cannot |

Choose an admissible loop $\ell$. Removing it leaves branches of lengths $r=\ell-1$ and $s=n-\ell$. If $n$ is even, $r+s$ is odd, so one branch length is even and the other is odd. If $n$ is odd and $\ell$ is odd, both lengths are even. In either admissible case, at least one branch has even length.

An even-length branch with zero diagonal has no zero eigenvalue. Its weights can therefore be enlarged to move every eigenvalue away from zero. The manuscript makes the choice explicit: on an even branch of length $d$, give every internal edge and its attachment to the center weight $d+1$; give all edges on the other side weight 1. Every eigenvalue on the scaled branch then has absolute value greater than 2, while every eigenvalue on the unit branch has absolute value less than 2. An empty branch has no eigenvalues to collide with anything.

The forbidden cases also have concrete obstructions. Without loops, the identity matrix $I$ vanishes wherever $A$ is nonzero and commutes with $A$, so it is a nonzero test matrix. At odd order, if all loops are at even positions, there is one more odd position than even position. This size difference supplies nonzero right and left nullvectors supported on the odd positions. Their outer product produces a nonzero test matrix. This obstruction is due to Koljančić–Oblak, Theorem 5.7(Cc); the exact argument appears in the [proof of the criterion](statements.md#proof-main).

## Why separation detects every hidden matrix

Polynomials turn the branch spectra into algebra we can track term by term. Write $q_k$ for the square of an edge weight and define

$$
P_0=1,\qquad P_1=x,
$$

$$
P_{k+2}=xP_{k+1}-q_kP_k.
$$

For example, $P_2=x^2-q_0$ and $P_3=x^3-(q_0+q_1)x$. The roots of $P_m$ are the eigenvalues of the $m$-point branch. The recurrence also shows that $P_m$ has only even powers when $m$ is even, and only odd powers when $m$ is odd. These recursive polynomials are called continuants.

Now change every edge weight and the loop a little. A dot denotes its rate of change, such as $\dot q_k$. Suppose the characteristic polynomial of the whole path has zero first-order change. The nonzero loop separates this condition into even and odd polynomial parts. Disjoint branch spectra mean that their polynomials have no common factor. This fact, together with degree bounds, forces the two branch-polynomial variations separately to be zero. Running the recurrence backward forces every $\dot q_k$ and the loop variation to be zero too.

There is one more bridge to the unrestricted matrix $X$. A symmetric path with nonzero neighboring weights has distinct eigenvalues: an eigenvector's first coordinate determines the rest successively through the row equations. In eigenvector coordinates, a commuting matrix must be diagonal. The first-order recovery just proved says that changes in the edges and loop detect every diagonal direction independently. Meanwhile $A\circ X=0$ makes $X$ orthogonal to all those changes. The final calculation is a sum of real squares equal to zero, forcing each term to vanish. The exact detection map and sum-of-squares calculation are in the [complete proof](statements.md#proof-main).

## From one loop to every prescribed loop

nSSP says that a linear system has only the zero solution, or equivalently that its coefficient matrix has full column rank. A nonzero determinant of a square submatrix witnesses that rank. A sufficiently small continuous change preserves its nonzero value. Thus we may add small positive weights at the other required loop positions and keep nSSP.

The integer conclusion survives too. Let $A_0$ be the integer one-loop witness and let $D$ have entry 1 at each loop still to be added. For every sufficiently large positive integer $N$,

$$
A_0+N^{-1}D
$$

has nSSP. Multiplying the whole matrix by $N$ preserves the zero-solution test, so

$$
NA_0+D
$$

is a positive-integer witness with exactly the desired support. This proves existence; it does not give a formula for the smallest suitable $N$.

## A test that avoids computing eigenvalues

With exactly one nonzero loop and every edge weight equal to 1, the test becomes

$$
\gcd(\ell,n+1)=1.
$$

For six points and $\ell=3$, $\gcd(3,7)=1$, so unit weights succeed. For five points and $\ell=3$, $\gcd(3,6)=3$, so unit weights fail, although the adjusted weights at the beginning succeed. This arithmetic condition tests the specified unit-edge matrix; it does not replace the parity criterion for existence of some weights.

The exact real existence statement at even order for every nonempty loop set, and the branch-recovery lemma, have pinned Lean declarations. Symmetry, positive integrality, the odd-order extension, the single-loop equivalence and the two family classifications receive manuscript-based written proofs in the next chapter, where each statement is matched to its evidence. A general classification of patterns that require nSSP is a separate question.

The aligned Chinese and English seminar editions use the same example and inference order.

::: {.slides src="seminar"}
Begin with the five-point example, state the criterion, and explain continuants and first-order recovery.
:::
