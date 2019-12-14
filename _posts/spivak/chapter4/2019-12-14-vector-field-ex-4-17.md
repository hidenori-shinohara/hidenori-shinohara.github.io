---
layout: post
title:  "Vector field"
date:   2019-12-14
author: Hidenori
---

# Proposition
If $f:\mathbb{R}^n \rightarrow \mathbb{R}^n$, define a vector field $\mathbf{f}$ by $\mathbf{f}(p) = f(p)_p \in \mathbb{R}^n_p$.
1. Show that every vector field $F$ on $\mathbb{R}^n$ is of the form $\mathbf{f}$ for some $f$.
1. Show that $\div \mathbf{f} = \trace f'$.

# Solution
## 1
Define $f_i:\mathbb{R}^n \rightarrow \mathbb{R}^n$ such that $f_i(p) = F^i(p)$ for each $i$.
Let $f(p) = (f_1(p), \cdots, f_n(p))$.
Then $F = \mathbf{f}$.

## 2

$$
\begin{align*}
  \div \mathbf{f}
    &= D_1F^1 + \cdots + D_nF^n \\
    &= D_1f_1 + \cdots + D_nf_n \\
    &= f'_{1, 1} + \cdots + f'_{n, n} \\
    &= \trace f'.
\end{align*}
$$

