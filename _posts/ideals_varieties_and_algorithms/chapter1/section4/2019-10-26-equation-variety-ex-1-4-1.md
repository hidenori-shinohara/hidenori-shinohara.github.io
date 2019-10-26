---
layout: post
title:  "Intersection of a circle and a hyperbola"
date:   2019-10-26
author: Hidenori
---

# Proposition
Consider the equations

$$
\begin{align*}
  x^2 + y^2 - 1 &= 0, \\
  xy - 1 &= 0
\end{align*}
$$

which describe the intersection of a circle and a hyperbola.

1. Use algebra to eliminate $y$ from the above equations.
1. Show how the polynomial found in part (1) lies in $\ev{ x^2 + y^2 - 1, xy - 1 }$.

# Solution
## 1
Since $y = 1/x$, we have $x^4 - x^2 + 1 = 0$.

## 2
$x^4 - x^2 + 1 = x^2(x^2 + y^2 - 1) - (xy + 1)(xy - 1) \in \ev{x^2 + y^2 - 1, xy - 1}$.
