---
layout: post
title:  "Ideal of a point"
date:   2019-11-17
author: Hidenori
---

# Proposition
Show that $I(\\{a_1, \cdots, a_n\\}) = \ev{x_1 - a_1, \cdots, x_n - a_n}$.

# Solution
Let $I = I(\\{a_1, \cdots, a_n\\})$.
Since each $x_i - a_i$ vanishes at $\\{a_1, \cdots, a_n\\}$, $x_i - a_i \in I$ for each $i$.
Thus $\ev{x_1 - a_1, \cdots, x_n - a_n} \subset I$.
$\ev{x_1 - a_1, \cdots, x_n - a_n}$ is a maximal ideal by Proposition 9 on P.210 (Ideals, Varieties, and Algorithms).

On the other hand, $I \ne k[x_1, \cdots, x_n]$ because $(x_1 - a_1) \cdots (x_n - a_n) + 1 \notin I$.
Therefore, $I = \ev{x_1 - a_1, \cdots, x_n - a_n}$.
