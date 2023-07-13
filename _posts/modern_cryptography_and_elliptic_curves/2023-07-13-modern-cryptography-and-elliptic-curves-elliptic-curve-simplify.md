---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Simplify elliptic curves"
date:   2023-07-13
author: Hidenori
---

Exercise from P.180 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Transform $p(z) = z^3+ Az^2+ Bz + C$ into the form of $q(x) = x^3 + ax + b$ without changing the discriminant.

As discussed earlier in the chapter, setting $z = x - A / 3$ achieves that.

The discriminant of $p$ is $\Pi_{i < j} (r_i - r_j)^2$ where $r_i$ is a root of $p(z)$.
$t: r \mapsto r + A / 3$ is a bijective relation between the roots of $p(z)$ and $q(x)$.
Note that for any roots $r_i, r_j$ of $p(z)$, $t(r_i) - t(r_j) = r_i - r_j$.
Therefore, the discriminant remains the same.


