---
layout: post
title:  "An Introduction to Mathematical Cryptography: Pohlig-Hellman Algorithm"
date:   2023-10-01
author: Hidenori
---

This is my notes for Theorem 2.32 in _An Introduction to Mathematical Cryptography_.

Let $G$ be a finite abelian group and $g \in G$ be an element of order $N = q_1^{e_1} \cdots q_t^{e_t}$.

We will solve $h = g^x$.

First, let $g_i = g^{N / q_i^{e_i}}$ and $h_i = h^{N / q_i^{e_i}}$.
And we will solve $g_i^{y_i} = h_i$ for each $i$.
This should be relatively easy as $g_i$ has an order $q_i^{e_i}$, which is significantly smaller than $N$.
See the book for an accurate time complexity analysis.

Now, we will solve the system of equations:

$$
\begin{align*}
    y &\equiv y_1 \pmod{q_1^{e_1}} \\
    y &\equiv y_2 \pmod{q_2^{e_2}} \\
    \cdots \\
    y &\equiv y_t \pmod{q_t^{e_t}} \\
\end{align*}
$$

By the CRT, we can find a solution $y$ to this.
We claim that this $y$ is the solution to the original problem.
For that, we first use the extended Euclid's algorithm to find $c_i$'s such that $c_1 \frac{N}{q_1^{e_1}} + \cdots + c_t \frac{N}{q_t^{e_t}}$.

$$
\begin{align*}
    g^Y &= g^{Y \cdot 1} \\
        &= g^{Y \cdot \sum c_i\frac{N}{q_i^{e_i}}} \\
        &= \prod g^{c_i Y \frac{N}{q_i^{e_i}}} \\
        &= \prod \big(g^{Y\frac{N}{q_i^{e_i}}}\big)^{c_i} \\
        &= \prod \big((g^{\frac{N}{q_i^{e_i}}})^{y_i}(g^{\frac{N}{q_i^{e_i}}})^{k_iq_i^{e_i}}\big)^{c_i} \\
        &= \prod \big((g^{\frac{N}{q_i^{e_i}}})^{y_i}\big)^{c_i} \\
        &= \prod h_i^{c_i} \\
        &= \prod (h^{\frac{N}{q_i^{e_i}}})^{c_i} \\
        &= h^{\sum c_i\frac{N}{q_i^{e_i}}} \\
        &= h^1 \\
        &= h.
\end{align*}
$$


