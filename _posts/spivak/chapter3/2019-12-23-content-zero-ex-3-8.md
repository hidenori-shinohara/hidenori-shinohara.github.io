---
layout: post
title:  "$[a_1, b_1] \\times \\cdots \\times [a_n, b_n]$ does not have content 0"
date:   2019-12-23
author: Hidenori
---

# Proposition
Prove that $[a_1, b_1] \times \cdots \times [a_n, b_n]$ does not have content 0 if $a_i < b_i$ for each $i$.

## Solution
We will use the same approach that the proof of Theorem 3-5 uses.

Let $A = [a_1, b_1] \times \cdots \times [a_n, b_n]$.
Let $\\{ U_1, \cdots, U_k \\}$ be a finite cover of $A$ by closed rectangles.
We will assume each $U_i$ is a subset of $A$.
If some $U_i$ is not a subset of $A$, we can set $U_i$ to be $U_i \cap A$ because the intersection of two closed rectangles is a closed rectangle.
Let $t_{i, j}$'s denote all the end points of $\\{ U_1, \cdots, U_k \\}$ where each $t_{i, j}$ denotes an end point in the $i$th coordinate.
In other words,

* $a_1 = t_{1, 0} < t_{1, 1} < \cdots < t_{1, i_1} = b_1$.
* $a_2 = t_{2, 0} < t_{2, 1} < \cdots < t_{2, i_2} = b_2$.
* $\vdots$
* $a_n = t_{n, 0} < t_{n, 1} < \cdots < t_{n, i_n} = b_n$.

These create $\prod_{j=1}^{n} t_{j, i_j}$ rectangles of the form $[t_{1, j_1 - 1}, t_{1, j_1}] \times \cdots \times [t_{n, j_n - 1}, t_{n, j_n}]$.

* Each of those rectangles lies in at least one $U_i$ since $\\{ U_1, \cdots, U_k \\}$ is a cover of $A$.
* Each $v(U_i)$ is the sum of certain $(t_{1, j_1} - t_{1, j_1 - 1}) \times \cdots \times (t_{n, j_n} - t_{n, j_n - 1})$.

Therefore, $\sum_{i=1}^{k} v(U_i) \geq \sum (t_{1, j_1} - t_{1, j_1 - 1}) \times \cdots \times (t_{n, j_n} - t_{n, j_n - 1}) = \prod_{i=1}^{n} (b_i - a_i)$.

Thus there does not exist a finite cover whose volume is less than $\prod_{i=1}^{n} (b_i - a_i)$, so $A$ does not have content 0.
