---
layout: post
title:  "An example of a quirk of a variety in the reals"
date:   2019-11-14
author: Hidenori
---

# Proposition
Give an example to show that [the result](/2019/11/14/polynomial-implicitization-ex-3-3-2.html) is false over $\mathbb{R}$.

# Solution
Let $F: \mathbb{R} \rightarrow \mathbb{R}$ be defined such that $F(t) = t^2$.

Let $I = \ev{x - f_1(t)} = \ev{x - t^2}$.
Let $V = V(I) = \\{ (a, a^2) \mid a \in \mathbb{R} \\}$.
Then $\pi_1(V) = [0, \infty)$.
On the other hand, $I_1 = \ev{0}$, so $V(I_1) = \mathbb{R}$.
Suppose there exists a variety $W$ such that $V(I_1) \setminus W \subset F(\mathbb{R}) = [0, \infty)$.
Then $(-\infty, 0) \subset W \subsetneq V(I_1) = \mathbb{R}$.
$W$ is a vanish set of an ideal of polynomials of 1 variable, and if the ideal is nonzero, $W$ cannot have infinitely many elements.
Therefore, $W$ must be a vanish set of $\ev{0}$.
However, this implies $W = \mathbb{R}$, so this is a contradiction.
