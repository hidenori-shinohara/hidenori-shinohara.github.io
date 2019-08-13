---
layout: post
title:  "Prove that the circle is not a retract of the closed disk."
date:   2019-08-13
author: Hidenori
---

# Proposition
Prove that the circle is not a retract of the closed disk.

# Solution
Let $\overline{D} = \\{ z \in \mathbb{C} \mid \abs{z} \leq 1 \\}$ and $S^1 = \\{ z \in \mathbb{C} \mid \abs{z} = 1 \\}$.

We will first show that $\overline{D}$ is simply connected.

$\overline{D}$ is path-connected.
We will check if $\pi_1(\overline{D}, 0)$ is trivial.
Let $[f] \in \pi_1(\overline{D}, 0)$ be given.
Consider $H: I \times I \rightarrow \overline{D}$ such that $H(s, t) = (1 - t)f(s)$.

* $H$ is continuous.
* $\forall s \in I, H(s, 0) = f(s)$.
* $\forall s \in I, H(s, 1) = 0$.
* $\forall t \in I, H(0, t) = (1 - t)f(0) = 0$.
* $\forall t \in I, H(1, t) = (1 - t)f(1) = 0$.

Therefore, $f$ is path-homotopic to $e_0$ where $e_0$ is the constant function at $0$.
Thus $\pi_1(\overline{D}, 0) = \\{ [e_0] \\}$, so $\overline{D}$ is simply connected.

A retract of a simply connected space is simply connected.
(See Corollary 7.29 on P.198 of Introduction to Topological Manifolds)
Since $\overline{D}$ is simply connected and [$S^1$ is not](https://en.wikipedia.org/wiki/Fundamental_group#Circle), $S^1$ cannot be a retract of $\overline{D}$.

