---
layout: post
title:  "$M_x$ consists of tangent vectors"
date:   2019-12-17
author: Hidenori
---

# Proposition
Show that $M_x$ consists of the tangent vectors at $t$ of curves $c$ in $M$ with $c(t) = x$.

# Solution
[We will use this discussion on tangent vectors in this solution](/2019/11/27/tangent-vector-ex-4-14.html)

Without loss of generality, we assume that $t = 0$.

Let $M \subset \mathbb{R}^n$ be a $k$-dimensional manifold and $x \in M$.
Let $f:W \rightarrow \mathbb{R}^n$ be a coordinate system around $x$ with $f(a) = x$.

Let $$f_{*}(v_a) \in M_x = f_{*}(\mathbb{R}^k_a)$$ be given.
Let $c: [0, 1] \rightarrow \mathbb{R}^k_a$ be defined such that $c(t) = a + vt$.

Then the tangent vector at $0$ is $$c_{*}((e_1)_0) = ((c^1)'(0), \cdots, (c^k)'(0))_{a} = v_a$$.
Moreover, the tangent vector to $f \circ c$ at 0 is $f_*(v_a)$.

Therefore, given an arbitrary element in $M_x$, we can always find a curve such that the element is the tangent vector of the curve.

Let $c$ be a curve in $M$ with $c(0) = x$.
We will show that the tangent vector at $0$ of the curve $c$ is in $M_x$.
Since the tangent vector only depends on the local behavior of $c$, we will assume that $c[0, 1] \subset f(W)$.
Then $f^{-1} \circ c$ is a smooth curve in $\mathbb{R}^k$.
Then the tangent vector to $f^{-1} \circ c$ at 0 is $(f^{-1} \circ c)_{*}((e_1)_0)$.
This is a vector at $(f^{-1} \circ c)(0) = f^{-1}(c(0)) = f^{-1}(x) = a$.
Therefore, $$c_{*}((e_1)_0) = f_*((f^{-1} \circ c)_{*}((e_1)_0)) \in f_{*}(\mathbb{R}^k_a) = M_x$$.
