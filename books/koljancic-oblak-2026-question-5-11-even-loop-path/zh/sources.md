# 来源、证据与贡献

Haobo Ma、Wenlin Zhang，*Koljančić–Oblak Question 5.11 (arXiv:2604.21552v1, Section 5): nSSP witnesses for looped double paths*，第 2 版（2026），[版本 DOI:10.5281/zenodo.23920568](https://doi.org/10.5281/zenodo.23920568)，CC BY 4.0。[概念 DOI:10.5281/zenodo.23920567](https://doi.org/10.5281/zenodo.23920567) 标识版本系列；这里引用的是第 2 版。[公开原文源码](https://github.com/mathesis-papers/10.5281-zenodo.23920567/blob/17531a2ffbd726120e9f2d0097311056d715320a/manuscript/note.tex) 包含 Theorem 1、Lemmas 2–4、Corollaries 5–6 及完整原始论证。Haobo Ma 的机构是 ChronoAI Pte Ltd, Singapore；Wenlin Zhang 的机构是 National University of Singapore 及 ChronoAI Pte Ltd, Singapore。

## 数学的来源

- S. Koljančić、P. Oblak，*Combinatorial aspects of the nonsymmetric strong spectral property for graphs*，Electronic Journal of Linear Algebra **42**（2026），755–779，[DOI:10.13001/ela.2026.10523](https://doi.org/10.13001/ela.2026.10523)；[arXiv:2604.21552v1](https://arxiv.org/abs/2604.21552v1)。Definitions 1.1、1.3、1.5 定义性质及允许／要求之别；Question 5.11 位于第 5 节，期刊第 776 页。Theorem 5.7(Cc) 给出奇数阶障碍；Theorem 5.7(A) 给出内部自环的不要求性构造。
- Carptopus，*Spectral separation and the non-symmetric strong spectral property for looped double paths*，2026 年 8 月 19 日，8 月 22 日修订；[带日期的源码](https://raw.githubusercontent.com/Carptopus/MathExplore-Notes/e57ee007380cbc351eb371d8e991303cab5f1e48/research/nssp-looped-double-paths/nssp-looped-double-paths.tex)，第 0.2 版 [DOI:10.5281/zenodo.22059007](https://doi.org/10.5281/zenodo.22059007)。Theorem 4.1 是单自环谱等价刻画，Theorem 5.2 给出单自环存在性，Theorem 6.1 是完整存在判据，Corollary 6.2 回答偶数阶问题。本论文承认其优先成果，并采用相同的奇偶分离机制。
- J. Michor、G. Teschl，*Reconstructing Jacobi matrices from three spectra*，载于 *Spectral Methods for Operators of Mathematical Physics*，OTAA **154**（2004），151–154，[DOI:10.1007/978-3-0348-7947-7_9](https://doi.org/10.1007/978-3-0348-7947-7_9)。Theorem 2.1 提供相关的三谱重构背景。这里直接计算微分，并非仅凭全局重构唯一性推出导数非奇异。
- S. M. Fallat、H. Tracy Hall、J. C.-H. Lin、B. L. Shader，*The bifurcation lemma for strong properties in the inverse eigenvalue problem of a graph*，Linear Algebra and its Applications **648**（2022），70–87，[DOI:10.1016/j.laa.2022.04.009](https://doi.org/10.1016/j.laa.2022.04.009)，Theorem 5.4；另见 Koljančić–Oblak 的 Lemma 1.2。其保持相似性的 Superpattern Lemma 比这里证明的正整数存在性后果更强。

## 形式陈述覆盖什么

[偶数阶 Lean 定理](lean:D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPathNSSP.result) 陈述：对每个正偶数阶与非空自环集，存在具有精确支撑的实数见证，测试矩阵取遍全部实矩阵。[支路恢复定理](lean:D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPath.branch_variation_injective) 陈述任意长度的恢复引理。这是 [陈述章](statements.md) 中两个精确对应。

更广的书面论证证明了对称与正整数性、奇数阶判据、没有总阶数奇偶限制的连接恢复、整数支路分离、固定矩阵的谱等价刻画、最大公因数判据及家族推论。原文报告的有限有理数检查包括：所有自环集合至 8 阶、支路微分至 10 阶、至 12 阶的 78 个单自环位置，以及 3 至 12 阶的内部自环失败构造。这些是原文报告的有限检查；全阶结论依赖完整书面证明。

## 可以参与的具体工作

共享请求协调已经证明的数学结论的形式化：

- [一般连接恢复](https://github.com/the-omega-institute/trureturing-requests/issues/154)：复用已有支路恢复与特征多项式微分，去掉额外的总阶数奇偶假设。
- [整数支路分离](https://github.com/the-omega-institute/trureturing-requests/issues/155)：把明确的 $M=d+1$ 构造形式化，覆盖所有可行支路奇偶组合。
- [完整存在判据](https://github.com/the-omega-institute/trureturing-requests/issues/156)：依赖前两项，扩展到奇数阶及对称正整数见证，保留已有偶数阶精确定理。
- [单自环等价关系与最大公因数判据](https://github.com/the-omega-institute/trureturing-requests/issues/157)：复用恢复论证，加入共同特征值障碍，再推出算术判据。
- [自环家族与超图案](https://github.com/the-omega-institute/trureturing-requests/issues/158)：从存在判据和谱等价关系推出分类，保留小阶边界及明确失败矩阵。

先在规范请求中协调范围，再在贡献者自己的 fork 上建立专注分支，依照 [上游 dev 的现有规则](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md) 直接提交 PR。原问题作者、早期证明作者、本论文作者和形式化贡献者分别保留相应贡献。PR 合入与平台验证凭据是两种不同证据。
