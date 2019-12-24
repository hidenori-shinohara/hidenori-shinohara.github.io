---
layout: post
title:  "If every local ring has no nonzero nilpotent element, then the ring has no nonzero nilpotent element"
date:   2019-12-24
author: Hidenori
---

# Proposition
Let $A$ be a ring.
Suppose that, for each prime ideal $p$, the local ring $A_p$ has no nilpotent element $\ne 0$.
Show that $A$ has no nilpotent element $\ne 0$.
If each $A_p$ is an integral domain, is $A$ necessarily an integral domain?

# Solution
$N(A)$, the nilradical of $A$, is an $A$-module.
For every prime $p$, $(N(A))_p = S^{-1}N(A)$ where $S = A \setminus p$.
By Corollary 3.12[Atiyah], $S^{-1}N(A) = N(S^{-1}A)$.
We are given that $N(S^{-1}A) = N(A_p) = 0$.
Therefore, $\forall p \in \Spec(A), (N(A))_p = 0$.
By Proposition 3.8[Atiyah], $N(A) = 0$.
In other words, the only nilpotent element of $A$ is 0.

It is possible that each $A_p$ is an integral domain and $A$ is NOT an integral domain.
Let $A = \mathbb{Z} / (2) \times \mathbb{Z} / (2)$.
There are only 4 ideals.

* $\\{ (0, 0) \\}$.
* $\\{ (0, 0), (1, 0) \\}$.
* $\\{ (0, 0), (0, 1) \\}$.
* $A$.

This is because the ideals are additive subgroups so the order must be 1, 2, or 4.
Then subgroups of order 2 must contain $(0, 0)$.
$\\{ (0, 0), (1, 1) \\}$ is not an ideal because $(1, 0) \cdot (1, 1) = (1, 0)$.

Among the 4 ideals, the only prime ideals are $\ev{(0, 1)}$ and $\ev{(1, 0)}$.
It is clear that they are symmetric, so we will show that $A_p$ is an integral domain when $p = \ev{(1, 0)}$.

First, we claim that $\frac{(1, 0)}{(1, 1)} = \frac{(1, 0)}{(0, 1)} = 0$.
This is because $(0, 1) \cdot ((1, 0) - (0, 0)) = 0$ where $(0, 1) \in A \setminus p$.

Suppose $(x/y) \cdot (z/w) = 0 = (0, 0)/(1, 1)$ where $x, z \in A$ and $y, w \in A \setminus p$.
Then $u(xz) = 0$ for some $u \in A \setminus p = \\{ (0, 1), (1, 1) \\}$

* If $x = (0, 0)$ or $z = (0, 0)$, we are done.
* Suppose otherwise.
  Then $xz = (0, 0)$ or $(1, 0)$ because $A \setminus p = \\{ (0, 1), (1, 1) \\}$.
  If $xz = (0, 0)$, then $\\{ x, z \\} = \\{ (0, 1), (1, 0) \\}$.
  If $xz = (1, 0)$, then $(1, 0) \in \\{ x, z \\}$.
  In each case, we know that one of $x/y$ or $z/w$ is 0 because $(1, 0) / (1, 1) = (1, 0) / (0, 1) = 0$ as shown above.

Therefore, $A_p$ is an integral domain.
However, $A$ is not an integral domain because $(1, 0) \cdot (0, 1) = (0, 0)$.
