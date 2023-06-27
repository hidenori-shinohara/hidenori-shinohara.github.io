---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Direct sums of cyclic groups of coprime sizes"
date:   2023-06-27
author: Hidenori
---

Theorem 6.11 from P.139 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> $$\mathbb{Z}_{m} \times \mathbb{Z}_{n} \cong \mathbb{Z}_{mn}$$ if and only if $\gcd(m, n) = 1$.

$$\mathbb{Z}_{m} \times \mathbb{Z}_{n} \cong \mathbb{Z}_{mn}$$ if and only if $(1, 1)$ is a generator.

$(1, 1)$ is a generator if and only if the set of solutions to the following system of equations is $\langle mn \rangle$:

$$
\begin{align*}
    x &\equiv 0 \pmod m \\
    x &\equiv 0 \pmod n.
\end{align*}
$$

This is equivalent to $\lcm(m, n) = 1$, which in turn is equivalent to $\gcd(m, n) = 1$.

