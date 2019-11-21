---
layout: post
title:  "Total degree of a polynomial"
date:   2019-11-21
author: Hidenori
---

# Proposition
If $h \in k[x_1, \cdots, x_n]$ has total degree $N$ and if $\displaystyle F(t_1, \cdots, t_n) = \big(\frac{f_1(t_1, \cdots, t_m)}{g_1(t_1, \cdots, t_m)}, \cdots, \frac{f_n(t_1, \cdots, t_m)}{g_n(t_1, \cdots, t_m)}\big)$,
show that $(g_1 \cdots g_n)^N(h \circ F)$ is a polynomial in $k[t_1, \cdots, t_m]$.

# Solution
If $h$ is not, then $(g_1 \cdots g_n)^N(h \circ F) = \sum (g_1 \cdots g_n)^N(h_i \circ F)$ where $h_i$'s are the monomials of $h$.
Therefore, it suffices to show this for the case that $h$ is a monomial without a coefficient.
Suppose $h = F_1^{k_1} \cdots F_n^{k_n}$ where each $k_i \geq 0$ and $\sum k_i = N$.

Then

$$
\begin{align*}
  (g_1 \cdots g_n)^N(F_1^{k_1} \cdots F_n^{k_n})
    &= (g_1^N \cdots g_n^N)(F_1^{k_1} \cdots F_n^{k_n}) \\
    &= (g_1^NF_1^{k_1}) \cdots (g_n^NF_n^{k_n}) \\
    &= (g_1^{N-k_1}f_1^{k_1}) \cdots (g_n^{N - k_n}f_n^{k_n}) \in k[t_1, \cdots, t_m].
\end{align*}
$$
