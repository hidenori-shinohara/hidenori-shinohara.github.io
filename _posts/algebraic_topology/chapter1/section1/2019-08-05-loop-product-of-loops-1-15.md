---
layout: post
title:  "A loop in a union of spaces is a product of loops each of which is contained in a space."
date:   2019-08-05
author: Hidenori
---

# Proposition
If a space $X$ is the union of collection of path-connected open sets $A_{\alpha}$ each containing the basepoint $x_0 \in X$ and if each intersection $A_{\alpha} \cap A_{\beta}$ is path-connected, then every loop in $X$ at $x_0$ is homotopic to a product of loops each of which is contained in a single $A_{\alpha}$.

# Solution
Let $f$ be a loop in $X$ whose basepoint is $x_0$.

Let $x \in I$ be given.
Then $f(x) \in A_{\alpha_x}$ for some $\alpha_x$.
Since $A_{\alpha_x}$ is open, $f^{-1}(A_{\alpha_x})$ is an open set in $I$ that contains $x$.

Let $K = \\{ f^{-1}(A_{\alpha_x}) \mid x \in I \\}$.
Then $K$ is an open cover of $I$.

From $K$, we can construct [$0 = s_0 < \cdots < s_m = 1$ such that each $[s_i, s_{i + 1}]$ is in $f^{-1}(A_{\alpha_x})$ for some $x \in I$.]({{ site.baseurl }}{% post_url /algebraic_topology/chapter1/section1/2019-08-05-finite-closed-intervals %})

For each $i = 1, 2, \cdots, m$, let $A_i$ denote the open set containing $f([s_{i - 1}, s_i])$.
Let $f_1, \cdots, f_m$ denote the path $f([s_{i - 1}, s_i])$.
In other words, $f_i(t) = f(s_{i - 1} + (s_i - s_{i - 1})t)$.
Then $f = f_1 \cdot f_2 \cdot \cdots \cdot f_m$.

Let $i = 1, 2, \cdots, m - 1$ be given.
$f(s_i) \in f([s_{i - 1}, s_i]) \subset A_i$ and $f(s_i) \in f([s_i, s_{i + 1}]) \subset A_{i + 1}$.
Since $A_i \cap A_{i + 1}$ is path connected and $x_0 \in A_i \cap A_{i + 1}$, there exists a path $g_i$ connecting $x_0$ to $f(s_i)$.

Then $f = (f_1 \cdot \overline{g_1}) \cdot (g_1 \cdot f_2 \cdot \overline{g_2}) \cdot (g_2 \cdot f_3 \cdot \overline{g_3}) \cdot \cdots \cdot (g_{m - 1} \cdot f_m)$.

Then $f_1 \cdot \overline{g_1}, g_1 \cdot f_2 \cdot \overline{g_2}, \cdots, g_{m - 1} \cdot f_m$ are loops in $A_1, \cdots, A_m$, respectively.
