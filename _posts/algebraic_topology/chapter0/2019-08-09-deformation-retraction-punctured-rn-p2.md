---
layout: post
title:  "Deformation retraction of $\\mathbb{R}^n \\setminus \\{ 0 \\}$ onto $S^{n - 1}$"
date:   2019-08-09
author: Hidenori
---

# Proposition
Construct an explicit deformation retraction of $\mathbb{R}^n \setminus \\{ 0 \\}$ onto $S^{n - 1}$.

# Solution
Let $F: \mathbb{R}^n \setminus \\{ 0 \\} \times I \rightarrow S^{n - 1}$ be defined such that

$$
\begin{align*}
  F((x_1, \cdots, x_n), t) = \frac{(x_1, \cdots, x_n)}{(1 - t) + td}
\end{align*}
$$

where $d = \sqrt{x_1^2 + \cdots + x_n^2}$.

* $F$ is continuous since $(1 - t) + td$ is continuous and a quotient of a continuous function by a continuous function is continuous.
* $F(x, t) = x$ for any $x \in S^{n - 1}$ and $t \in I$.
* $F(x, 1) \in S_1$ for any $x \in S^{n - 1}$.

Therefore, $F$ is a deformation retraction of $\mathbb{R}^n \setminus \\{ 0 \\}$ onto $S^{n - 1}$.

