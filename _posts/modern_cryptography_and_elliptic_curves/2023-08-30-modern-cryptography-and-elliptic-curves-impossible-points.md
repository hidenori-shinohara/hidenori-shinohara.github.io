---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Points that never exist"
date:   2023-08-30
author: Hidenori
---

Let $y^2 = x^3 + ax + b$ be an elliptic curve over a field $F$.

We claim that all points are one of the following:
- $[0, 1, 0]$.
- $[x, y, 1]$ for some $x, y \in F$

First, we will show that none of the following points are on this curve:

- $[1, y, 0]$ for any $y \in F$.

This is because

$$
\begin{align*}
    y^2z = x^3 + axz^2 + bz^3
    &\implies
        y^2 \cdot 0 = 1^3 + a \cdot 1 \cdot 0^2  + b \cdot 0^3 \\
    &\implies
        0 = 1
\end{align*}
$$

This implies that if the $z$ coordinate is 0, then the $x$ coordinate must be zero.
Since $[0, 0, 0]$ is not a point, this implies that any point of the form $[0, y, 0]$ is equivalent to $[0, 1, 0]$.
Finally, this implies that all the remaining points have a nonzero $z$ coordinate.
Therefore, whenever we consider a point on an elliptic curve, we only need to consider the point at infinity $[0, 1, 0]$ and any point of the form $[x, y, 1]$.
