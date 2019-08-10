---
layout: post
title:  "Construct an explicit deformation retraction of the torus with one point deleted onto two circles."
date:   2019-08-10
author: Hidenori
---

# Proposition
Construct an explicit deformation retraction of the torus with one point deleted onto a graph consisting of two circles intersecting in a point, namely, longitude and meridian circles of the torus.

# Solution
First, we will define a torus.
Let $X = \\{ (x, y) \in \mathbb{R}^2 \mid \abs{x} \leq 1 \land \abs{y} \leq 1 \\}$.
Define $f_1, f_2$ such that

$$
\begin{align*}
  f_1(x, y)
    &= \begin{cases}
      (x, y) & (x \ne -1) \\
      (1, y) & (x = -1).
    \end{cases} \\
  f_2(x, y)
    &= \begin{cases}
      (x, y) & (y \ne -1) \\
      (x, 1) & (y = -1).
    \end{cases}
\end{align*}
$$

Let $p = f_1 \circ f_2$.
Let $Y = p(X) = \\{ (x, y) \in \mathbb{R}^2 \mid \abs{x} \leq 1, \abs{y} \leq 1, x \ne -1, y \ne -1 \\}$.
Then $Y$ with the quotient topology induced by $p$ is a torus.

Next, we will define a function on $X$ because it is easier to see continuity when dealing with real functions, rather than functions on quotient spaces.
Let $g((x, y), t): X \times I \rightarrow X$ be defined such that

$$
\begin{align*}
  g((x, y), t) &= (x / \phi(t), y / \phi(t))
\end{align*}
$$

where $\phi(t) = (1 - t) + t \max \\{ \abs{x}, \abs{y} \\}$.

Then $g$ is continuous since each component function is a continuous real function.

Lastly, we will define a deformation retraction.
The composition $p \circ g$ maps $X \times I$ into $Y$ continuously because both $p$ and $g$ are continuous.

Let $(x, y) \in Y, t \in I$ be given.
We claim that $(x, y) \maps g((x, y), t)$ is constant on $p^{-1}(\\{ (x, y) \\})$.

* If $x \ne -1$ and $y \ne -1$, then $p^{-1}(\\{ (x, y) \\}) = \\{ (x, y) \\}$.
* If $x = -1$ and $y \ne -1$, then $p^{-1}(\\{ (x, y) \\}) = \\{ (1, y), (-1, y) \\}$.
* If $x \ne -1$ and $y = -1$, then $p^{-1}(\\{ (x, y) \\}) = \\{ (x, 1), (x, -1) \\}$.
* If $x = -1$ and $y = -1$, then $p^{-1}(\\{ (x, y) \\}) = \\{ (1, 1), (-1, 1), (1, -1), (-1, -1) \\}$.

TODO

