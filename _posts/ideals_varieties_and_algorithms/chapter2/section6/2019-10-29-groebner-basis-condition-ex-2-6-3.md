---
layout: post
title:  "A sufficient condition for a basis to be a Groebner basis"
date:   2019-10-29
author: Hidenori
---

# Proposition
If $G = \\{ g_1, \cdots, g_k \\}$ is a basis for $I$ with the property that $\overline{f}^{G} = 0$ for all $f \in I$, then $G$ is a Groebner basis.

# Solution
For each $(i, j)$ pair, $S(g_i, g_j) = \frac{x^{\gamma}}{\LT(g_i)} g_i - \frac{x^{\gamma}}{\LT(g_j)} g_j$ where $x^{\gamma} = \lcm(\LT(g_i), \LT(g_j))$.
Therefore, $\frac{x^{\gamma}}{\LT(g_i)}, \frac{-x^{\gamma}}{\LT(g_j)} \in k[x_1, \cdot, x_n]$, so $S(g_i, g_j) \in I$.

This implies that for each $(i, j)$ pair, $\overline{S(i, j)}^{G} = 0$.
By Buchberger's Criterion (Theorem 6, P.86 of Ideals, Varieties, and Algorithms), $G$ must be a Groebner basis.
