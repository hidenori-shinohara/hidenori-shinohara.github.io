---
layout: post
title:  "$\\pi_1(S^n) = 0$ if $n \\geq 2$"
date:   2019-08-05
author: Hidenori
---

# Proposition
$\pi_1(S^n) = 0$ if $n \geq 2$.

# Solution
Let $p = (0, 0, \cdots, 0, 1)$.
Let $A_1 = S^n \setminus \\{ p \\}, A_2 = S^n \setminus \\{ -p \\}$.
Then $A_1, A_2$ are both open and $A_1 \cup A_2 = S^n$.

As shown [in this post]({{ site.baseurl }}{% post_url /algebraic_topology/chapter1/section1/2019-08-05-finite-closed-intervals %}), $A_1, A_2$ are homeomorphic to $\mathbb{R}^n$.

We claim that $A_1 \cap A_2 = S^n \setminus \\{ p, -p \\}$ is homeomorphic to $S^{n - 1} \times \mathbb{R}$.

Define $f: S^n \setminus \\{ p, -p \\} \rightarrow S^{n - 1} \times \mathbb{R}$ and $g: S^{n - 1} \times \mathbb{R} \rightarrow S^n \setminus \\{ p, -p \\}$ such that:

* $f(x_1, \cdots, x_n, x_{n + 1}) = ((x_1 / c, \cdots, x_n / c), \tan \frac{x_{n + 1} \pi}{2})$ where $c = \sqrt{1 - x_{n + 1}^2}$.
* $g((y_1, \cdots, y_n), y) = (y_1\sqrt{1 - d^2}, \cdots, y_n\sqrt{1 - d^2}, d)$ where $d = \frac{2}{\pi}\arctan y$.

They are well-defined because:

* $(x_1 / c)^2 + \cdots + (x_n / c)^2 = (x_1^2 + \cdots + x_n^2) / (1 - x_{n + 1}^2) = 1$, and $\frac{x_{n + 1}\pi}{2} \in (-\pi / 2, \pi / 2)$.
* $(y_1\sqrt{1 - d^2})^2 + \cdots + (y_n\sqrt{1 - d^2})^2 + d^2 = (1 - d^2)(y_1^2 + \cdots + y_n^2) + d^2 = 1$, and $\frac{2}{\pi}\arctan y \in (-1, 1)$.

They are both continuous because each coordinate function is continuous.
We claim that $f \circ g$ is the identity on $S^{n - 1} \times \mathbb{R}$ and $g \circ f$ is the identity on $S^n \setminus \\{ p, -p \\}$.

* $f(g((y_1, \cdots, y_n), y)) = f(y_1\sqrt{1 - d^2}, \cdots, y_n\sqrt{1 - d^2}, d) = (y_1, \cdots, y_n, y)$.
* $g(f(x_1, \cdots, x_n, x_{n + 1})) = g((x_1 / c, \cdots, x_n / c), \tan \frac{x_{n + 1} \pi}{2}) = (\frac{x_1\sqrt{1 - d^2}}{c}, \cdots, \frac{x_n\sqrt{1 - d^2}}{c}, d)$.
  Then $d = \frac{2}{\pi}\arctan (\tan \frac{x_{n + 1}\pi}{2}) = x_{n + 1}$, and $c = \sqrt{1 - x_{n + 1}^2}$.
  Therefore, $g \circ f = id$.
  
Therefore, $S^{n - 1} \times \mathbb{R}$ and $S^n \setminus \\{ p, -p \\}$ are homeomorphic.

Let $x_0 \in A_1 \cap A_2$.
Since $S^n$ is path-connected, it does not matter which point to use as the basepoint, so we will use $x_0$.

* Since $\mathbb{R}^n$ is path-connected, $A_1, A_2$ are path-connected.
  Moreover, they are open.
* $A_1 \cup A_2 = S^n$.
* Since $n \geq 2$, $S^{n - 1}$ is path-connected. Therefore, $S^{n - 1} \times \mathbb{R}$ is path-connected, so $A_1 \cap A_2$ is path-connected.
* $x_0 \in A_1 \cap A_2$.

By [the proposition proved in this post]({{ site.baseurl }}{% post_url /algebraic_topology/chapter1/section1/2019-08-05-loop-product-of-loops-1-15 %}), every loop in $S^n$ based at $x_0$ is homotopic to a product of loops in $A_1$ or $A_2$.
Since $A_1, A_2$ are homeomorphic to $\mathbb{R}^n$, $\pi_1(A_1, x_0) = \pi_1(A_2, x_0) = 0$.
Thus every loop in $S^n$ based at $x_0$ is homotopic to the constant loop at $x_0$, so $\pi_1(S^n, x_0) = 0$.
