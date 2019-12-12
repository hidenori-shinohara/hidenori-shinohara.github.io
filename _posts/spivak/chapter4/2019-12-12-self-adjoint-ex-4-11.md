---
layout: post
title:  "The matrix of a self-adjoint linear transformation"
date:   2019-12-12
author: Hidenori
---

# Proposition
If $T$ is an inner product on $V$, a linear transformation $f: V \rightarrow V$ is called self-adjoint (with respect to $T$) if $T(x, f(y)) = T(f(x), y)$ for $x, y \in V$.
If $v_1, \cdots, v_n$ is an orthonormal basis and $A = (a_{ij})$ is the matrix of $f$ with respect to this basis, show that $a_{ij} = a_{ji}$.

# Solution

We have $f(v_i) = \sum_{j=1}^{n} a_{ji} v_j$ for each $i$.
Let $s, t \in \\{ 1, \cdots, n \\}$ be given.
* $T(f(v_s), v_t) = \sum_{j=1}^{n} a_{js} T(v_j, v_t) = a_{ts}$.
* $T(v_s, f(v_t)) = \sum_{j=1}^{n} a_{jt} T(v_s, v_j) = a_{st}$.

Since $T(f(v_s), v_t) = T(v_s, f(v_t))$, $a_{ts} = a_{st}$.
