---
layout: post
title:  "Modern Cryptography and Elliptic Curves: The number of points on an elliptic curve"
date:   2023-08-18
author: Hidenori
---

Important property in Modern Cryptography and Elliptic Curves - A Beginner’s Guide.

> For any prime $p \geq 3$, $U_p$ has exactly $(p - 1) / 2$ squares.


More formally, we are trying to show:

$$
\begin{align*}
    \abs{ \{ x \in U_p \mid \exists y, y \cdot y = x \} } = \frac{p - 1}{2}.
\end{align*}
$$

[In a previous post](/2023/08/16/modern-cryptography-and-elliptic-curves-elliptic-curve-cyclic.html), we showed that $U_p$ is cyclic.

Let $\phi$ be an isomorphism from $U_p$ to $\mathbb{Z}_{p - 1}$.

Let $x \in U_p$ be given.

$$
\begin{align*}
    \exists y, y \cdot y = x
        &\iff \exists y, \phi(y) + \phi(y) = \phi(x) \\
        &\iff \exists y', y' + y' \equiv \phi(x) \pmod{p - 1} \\
        &\iff \phi(x) \in \{ 0, 2, 4, \cdots, (p - 3) \}
\end{align*}
$$

as $p - 1$ is an even number.
Therefore, there are exactly $\frac{p - 1}{2}$ squares.

TODO: Add a section on how we use this to guess the number of points

