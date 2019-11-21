---
layout: post
title:  "Any linear subspace of $k^n$ is irreducible"
date:   2019-11-21
author: Hidenori
---

# Proposition
Let $k$ be an infinite field.
1. Show that any straight line in $k^n$ is irreducible.
1. Prove that any linear subspace of $k^n$ is irreducible.

# Solution
## 1
Let $a = (a_1, \cdots, a_n), b = (b_1, \cdots, b_n)$ be two distinct lines on the given line.
Then for every $t \in k$, $a + (a - b)t$ must be a point on the line because we are given a straight line.
Moreover, every point on the line can be represented as $a + (a - b)t$ for some $t \in k$.

Therefore, consider the parametrization $x_1 = f_1(t), \cdots, x_n = f_n(t)$ where $f_i(t) = a_i + (a_i - b_i)t$.
By Proposition 5 on P.208 (Ideals, Varieties, and Algorithms), $V$ defined parametrically by $x_i = f_i$ is irreducible.

## 2
Let $S$ be a linear subspace of $k^n$.

From linear algebra, we know the existence of a finite basis where each basis corresponds to a straight line.
Let $m$ be the number of elements in the basis.
Using the argument above, the $j$th straight line can be parametrized as $x_i = f_{i, j}(t_j)$ for each $i$.

Every point in $S$ can be expressed as a linear combination of basis elements.
In other words, every point in $S$ can e expressed as

$$
\begin{align*}
  x_1 &= f_{1, 1}(t_1) + f_{1, 2}(t_2) + \cdots + f_{1, m}(t_m), \\
  \vdots \\
  x_n &= f_{n, 1}(t_1) + f_{n, 2}(t_2) + \cdots + f_{n, m}(t_m).
\end{align*}
$$

for some $t_1, \cdots, t_m$.
Let $f_i(t_1, \cdots, t_m) = f_{i, 1}(t_1) + \cdots + f_{i, m}(t_m)$.
Then we have a parametrization $x_i = f_i(t_1, \cdots, t_m)$ of $S$, thus $S$ is irreducible by the same proposition.
