---
layout: post
title:  "An example of a polynomial mapping"
date:   2019-11-11
author: Hidenori
---

# Proposition
Let $V$ be the twisted cubic in $\mathbb{R}^3$ and let $W = V(v - u - u^2)$ in $\mathbb{R}^2$.
Show that $\phi(x, y, z) = (xy, z + x^2y^2)$ defines a polynomial mapping from $V$ to $W$.

# Solution
$V = V(y - x^2, z - x^3) = \\{ (a, a^2, a^3) \mid a \in \mathbb{R} \\}$.
Then $\forall (a, a^2, a^3) \in V, \phi(a, a^2, a^3) = (a^3, a^6 + a^3)$.
Since $v - u - u^2 = (a^6 + a^3) - a^3 - (a^3)^2 = 0$, so $\phi(V) \subset W$.
Therefore, $\phi$ is indeed a polynomial mapping from $V$ to $W$.
