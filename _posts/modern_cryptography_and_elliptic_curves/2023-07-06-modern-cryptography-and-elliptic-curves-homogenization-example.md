---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Example of Homogenization"
date:   2023-07-06
author: Hidenori
---

Exercise from P.159 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Given affine curves $x = y^2$ and $y = −3$, find the points of intersection of the corresponding projective curves.

After homogenization, we obtain:
- $zx = y^2$
- $y = -3z$.

We split this into two cases:
- $z = 0$. Then $y$ must be $0$, but $x$ does not have to be. Therefore, $[1, 0, 0]$ is a solution. Indeed, for any $t \in \mathbb{R}$, $(t, 0, 0)$ satisfies the system of equations.
- $z \ne 0$. Without loss of generality, set $z = 1$. Then we obtain $[9, -3, 1]$. Indeed for any $t \in \mathbb{R}$, $(9t, -3t, t)$ is a solution.

Therefore, the corresponding projective curves intersect at $[1, 0, 0]$ and $[9, -3, 1]$.
