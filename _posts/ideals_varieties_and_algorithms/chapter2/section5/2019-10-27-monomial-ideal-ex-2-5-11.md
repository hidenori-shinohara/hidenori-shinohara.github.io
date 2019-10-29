---
layout: post
title:  "Monomial ideal and constant terms"
date:   2019-10-29
author: Hidenori
---

# Proposition
Let $f \in k[x_1, \cdots, x_n]$.
If $f \notin \ev{ x_1, \cdots, x_n }$, then show $\ev{ x_1, \cdots, x_n, f } = k[x_1, \cdots, x_n]$.

# Solution
Since $f \in k[x_1, \cdots, x_n]$, $f = c_{\alpha_1} x^{\alpha_1} + \cdots + c_{\alpha_n} x^{\alpha_n}$ for some $\alpha_i$ and nonzero $c_{\alpha_i}$.

For each $i$, if $\alpha_i \ne 0$, then $c_{\alpha_i} x^{\alpha_i} \in \ev{ x_1, \cdots, x_n }$.
Thus $\alpha_i = 0$ for some $i$.
Then $1 = \alpha_i^{-1}(f - \sum_{j \ne i} c_{\alpha_j}x_{\alpha_j}) \in \ev{ x_1, \cdots, x_n, f }$.
Therefore, $\ev{ x_1, \cdots, x_n, f } = k[x_1, \cdots, x_n]$.
