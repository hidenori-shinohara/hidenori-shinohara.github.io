---
layout: post
title:  "Whenever a sphere is expressed as the union of three closed sets $A_1, A_2$, and $A_3$, then at least one of these sets must contain a pair of antipodal points"
date:   2019-08-04
author: Hidenori
---

# Proposition
Whenever $S^2$ is expressed as the union of three closed sets $A_1, A_2$, and $A_3$, then at least one of these sets must contain a pair of antipodal points $\\{ x, -x \\}$.

# Solution

Since $S^2$ is nonempty, not all $A_1, A_2, A_3$ are empty.

If only one of them is nonempty, then it contains $(1, 0, 0)$ and $(-1, 0, 0)$, so we are done.
Suppose that at least two of them are nonempty.
Without loss of generality, suppose that $A_1 \ne \emptyset$ and $A_2 \ne \emptyset$.

For each $i = 1, 2$, define $d_i(x) = \inf \\{ d(x, y) \mid y \in A_i \\}$.
$d_1, d_2$ are well defined because we assumed that $A_1$ and $A_2$ are both nonempty.

Let $g: S^2 \rightarrow \mathbb{R}^2$ be defined such that $g(x) = (d_1(x), d_2(x))$.
By [the Borsuk-Ulam theorem](https://en.wikipedia.org/wiki/Borsuk–Ulam_theorem), there exists an $x \in S^2$ such that $d_1(x) = d_1(-x)$, and $d_2(x) = d_2(-x)$.

1. Suppose that $d_1(x) = d_1(-x) = 0$.
   Then $x$ and $-x$ are limit points of $A_1$.
   Since $A_1$ is closed, $A_1$ contains both $x$ and $-x$.
1. Suppose that $d_2(x) = d_2(-x) = 0$.
   Then $x$ and $-x$ are limit points of $A_2$.
   Since $A_2$ is closed, $A_2$ contains both $x$ and $-x$.
1. Suppose that $d_1(x) = d_1(-x) \ne 0$ and $d_2(x) = d_2(-x) \ne 0$.
   Then $x \notin A_1, -x \notin A_1, x \notin A_2$, and $-x \notin A_2$.
   This means $x, -x \in A_3$.
