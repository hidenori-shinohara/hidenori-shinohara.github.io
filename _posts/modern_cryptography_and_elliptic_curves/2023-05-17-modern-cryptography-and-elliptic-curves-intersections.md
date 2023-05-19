---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Intersections of lines and conics"
date:   2023-05-17
author: Hidenori
---

Exercise from P.40 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> In how many points can two arbitrary lines (in the plane) intersect?

For each $i = 1, 2$, let $f_i(x, y) = a_ix + b_iy + c_i$.

At least one of $a_1$ or $b_1$ must be nonzero since $f_1$ is a line.
Without loss of generality, $b_1 \ne 0$.
Then $Z(f_1) = \\{ (x, y) \mid y = \alpha x + \beta \\}$ for $\alpha = \frac{-a_1}{b_1}, \beta = \frac{-c_1}{b_1}$.

By plugging this into $f_2(x, y) = 0$, we get $0 = Ax + B$ for some $A, B$.

- If $A = B = 0$, then there are infinitely many solutions.
  This happens when $f_1 = f_2$ for instance.
- If $A = 0 \ne B$, then there is no solution.
  This happens when $f_1 = f_2 + 1$ for instance.
- if $A \ne 0$, there is exactly one solution.
  This happens when $f_1 = x + y, f_2 = x - y$ for instance.


> In how many points can a line and a conic intersect?

We claim that it has to be either 0, 1, 2, $\infty$.
Examples:

- No intersection: $f(x, y) = (x + y)^2$ and $g(x, y) = x + y - 1$.
- 1 intersection: $f(x, y) = (x + y)^2$ and $g(x, y) = x$.
- 2 intersections: $f(x, y) = (x + y)^2 - 1, $g(x, y) = x - y - 1$.
    - At an intersection $(a + 1, a)$, we have $(2a + 1)^2 = 1$. In other words, $a = 0$ or $a = -1$.
- Infinitely many intersections: $f(x, y) = (x + y)^2$ and $g(x, y) = x + y$.

And now we claim that they are the only possibilities.
Let $f$ be the conic and $g(x, y) = \alpha x + \beta y + \gamma$.
Since $g$ is a line, at least one of $\alpha$ or $\beta$ is nonzero.
Without loss of generality, $\beta \ne 0$.
Then $Z(g)$ is the set of points satisfying $y = ax + b$ for some $a, b \in \mathbb{R}$.
By plugging this into $f(x, y)$, we get $Ax^2 + Bx + C = 0$ for some $A, B, C \in \mathbb{R}$.

If $A = B = C = 0$, then there are infinitely many $x$'s that satisfy this equation.
If $A = B = 0 \ne C$, then there is no solution.
Otherwise, it is easy to see that there is either one or two solutions.

