---
layout: post
title:  "Special case of the Pohlig-Hellman algorithm"
date:   2023-09-11
author: Hidenori
---

Suppose that $p, q_1, q_2$ are prime numbers such that $p - 1 = q_1 q_2$ with $q_1 \ne q_2$.
Suppose that we can solve $g^x = h$ in $O(S_{q})$ if $\abs{g} = q$ for any $g, e \in \mathbb{F}_p$.

Note that an element in $\mathbb{F}_p$ has an order of $1, q_1, q_2, q_1q_2$.
Therefore, we don't have to worry about prime powers.

We claim that we can solve $g^x = h$ in $O(S_{q_1} + S_{q_2})$.

Let $g, h$ be given.

We assume $\abs{g} = q_1q_2$ as the other cases are trivial.

Now we solve the following two equations:

- $(g^{q_2})^{x_1} = h^{q_2}$.
- $(g^{q_1})^{x_2} = h^{q_1}$.

We can solve them in $O(S_{q_1} + S_{q_2})$ as $\abs{g^{q_2}} = q_1$ and $\abs{g^{q_1}} = q_2$.
As $\gcd(q_1, q_2) = 1$, the CRT guarantees the existence of $x$ such that $x \equiv x_1 \pmod{q_1}$ and $x \equiv x_2 \pmod{q_2}$.

Let $k_1, k_2, c_1, c_2 \in \mathbb{Z}$ be chosen such that:

- $x = x_1 + k_1q_1$
- $x = x_2 + k_2q_2$
- $c_1q_1 + c_2q_2 = 1$

Then we have

$$
\begin{align*}
    g^x &= (g^x)^1 \\
        &= (g^x)^{c_1q_1 + c_2q_2} \\
        &= (g^x)^{c_1q_1}(g^x)^{c_2q_2} \\
        &= ((g^{q_1})^x)^{c_1}((g^{q_2})^x)^{c_2} \\
        &= ((g^{q_1})^{x_2 + k_2q_2})^{c_1}((g^{q_2})^{x_1 + k_1q_1})^{c_2} \\
        &= (g^{q_1x_2 + k_2q_1q_2})^{c_1}(g^{q_2x_1 + k_1q_1q_2})^{c_2} \\
        &= (g^{q_1x_2}g^{k_2q_1q_2})^{c_1}(g^{q_2x_1}g^{k_1q_1q_2})^{c_2} \\
        &= (g^{q_1x_2})^{c_1}(g^{q_2x_1})^{c_2} \\
        &= (h^{q_1})^{c_1}(h^{q_2})^{c_2} \\
        &= h^{c_1q_1 + c_2q_2} \\
        &= h^{1} \\
        &= h.
\end{align*}
$$





