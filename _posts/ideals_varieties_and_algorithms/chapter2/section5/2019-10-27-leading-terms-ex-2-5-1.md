---
layout: post
title:  "Leading terms of polynomials and generators of an ideal"
date:   2019-10-27
author: Hidenori
---

# Proposition
Let $I = \ev{ g_1, g_2, g_3 } \subset \mathbb{R}[x, y, z]$, where $g_1 = xy^2 - xz + y, g_2 = xy - z^2$ and $g_3 = x - yz^4$.
Using the lex order, give an example of $g \in I$ such that $\LT(g) \notin \ev{ \LT(g_1), \LT(g_2), \LT(g_3) }$.

# Solution
$\LT(g_1 - yg_2 + zg_3) = \LT(-yz^5 + yz^2 + y) = -yz^5$.
Since $x \mid \LT(g_i)$ for each $i$, $-yz^5 \notin \ev{ \LT(g_1), \LT(g_2), \LT(g_3) }$.
