---
layout: post
title:  "The unit interval with the endpoints glued together is homeomorphic to the unit circle"
date:   2019-08-24
author: Hidenori
---

# Proposition
$I$ with the equivalence relation $0 \sim 1$ is homeomorphic to $S^1$.

# Solution

The equivalence relation is the same as $a \sim b \iff a - b \in \mathbb{Z}$.

Let $p: I \rightarrow I / \sim$ such that $p(t) = [t]$ for each $t \in I$.
Let $f: I \rightarrow S^1$ such that $f(t) = (\cos (2\pi t), \sin (2\pi t))$.

Each component function of $f$ is continuous, so $f$ is continuous.
Let $\tilde{f}: I / \sim \rightarrow S^1$ be defined such that $\tilde{f}([t]) = f(t)$.
This is well defined because $f(0) = f(1)$.
Moreover, we have $f = \tilde{f} \circ p$.
We claim that $\tilde{f}$ is a homeomorphism.

* Injective?

Let $[t_1], [t_2] \in I / \sim$.
Suppose $\tilde{f}([t_1]) = \tilde{f}([t_2])$.
Then $f(t_1) = f(t_2)$, so $\cos (2\pi t_1) = \cos (2\pi t_2)$.
Since $\cos$'s period is $2\pi$, $t_1 - t_2 \in \mathbb{Z}$, so $t_1 \sim t_2$.

* Surjective?

Each point in $S^1$ can be expressed as $(\cos (2\pi t), \sin (2 \pi t))$.
Let $t' = t - \lfloor t \rfloor$.
Then $t' \in I$, and $\tilde{f}([t]) = (\cos (2\pi t), \sin (2 \pi t))$.

* Continuous?

Let $U \subset S^1$ be open.
Then $f^{-1}(U)$ is open in $I$ because $f$ is continuous.
Since $f^{-1}(U) = (\tilde{f} \circ p)^{-1}(U)$, $p^{-1}(\tilde{f}^{-1}(U))$ is open.
Since $p$ is a quotient map, $\tilde{f}^{-1}(U)$ is open.
Therefore, $\tilde{f}$ is continuous.

We have shown that $\tilde{f}$ is a continuous bijection.
We claim that $I / \sim$ is compact and $S^1$ is Hausdorff.

* $I / \sim$ compact?
    * Let $K = \\{ U_{\alpha} \\}$ be an open cover of $I / \sim$.
      Then $\\{ p^{-1}(U_{\alpha}) \\}$ is an open cover of $I$ because $p$ is continuous.
      Since $I$ is compact, there exist $p^{-1}(U_{\alpha_1}), \cdots, p^{-1}(U_{\alpha_n})$ that cover $I$.
      Since $p$ is surjective, $p(I) = I / \sim$.
      Then we have $p(I) = p(\bigcup_{i=1}^{n} p^{-1}(U_{\alpha_1})) = \bigcup_{i = 1}^{n} p(p^{-1}(U_{\alpha_i}))$.
      Since $p$ is surjective, $p(p^{-1}(U_{\alpha_i})) = U_{\alpha_i}$ for each $i$.
      Therefore, $U_{\alpha_1}, \cdots, U_{\alpha_n}$ cover $I / \sim$.

* $S^1$ Hausdorff?
    * $\mathbb{R}^2$ is Hausdorff, so its subspace $S^1$ is Hausdorff.

[Since $\tilde{f}$ is a continuous bijection from a compact space into a Hausdorff space, it is a homeomorphism.]({% post_url /introduction_to_topological_manifolds/chapter3/2019-08-24-continuous-bijection %})
