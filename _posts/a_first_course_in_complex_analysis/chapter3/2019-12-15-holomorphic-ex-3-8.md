---
layout: post
title:  "Holomorphic function and the unit circle"
date:   2019-12-15
author: Hidenori
---

# Proposition
Suppose that $f$ is holomorphic in the region $G$ and $f(G)$ is a subset of the unit circle.
Show that $f$ is constant.

# Solution
If $f(G) = \\{ 1 \\}$, we are done.
Suppose otherwise.
Let $g \in G$ such that $f(g) \ne 1$.
Let $U$ be a neighborhood of $g$ in $G$ such that $1 \notin f(U)$.
Then let $h: U \rightarrow \mathbb{C}$ such that $h(z) = (1 + f(z)) / (1 - f(z))$.
Then $h$ is holomorphic because a composition of two holomorphic functions is holomorphic.
[As shown in this post](/2019/12/15/mobius-transformation-unit-circle-ex-3-7.html), $h$ maps $U$ into the imaginary line.
Therefore, $h_x = 0$.
By the Cauchy-Riemann equations, $h_y = 0$, so $h$ is constant.
Since the Mobius transformation $z \mapsto (1 + z) / (1 - z)$ is not a constant map, $h$ is constant if and only if $f$ is on $U$.

Since $G$ is connected, such $U$'s overlap, so $f$ is constant.
