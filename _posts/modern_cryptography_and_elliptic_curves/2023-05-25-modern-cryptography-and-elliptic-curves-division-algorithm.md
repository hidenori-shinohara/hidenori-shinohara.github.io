---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Division Algorithm"
date:   2023-05-25
author: Hidenori
---

Exercise from P.47 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Let $a, b \in \mathbb{Z}$, $b = 0$. Then there exist unique integers $q$ and $r$ with $a = bq + r$ and $0 \leq r < \abs{b}$, where $\abs{b}$ is the absolute value of $\abs{b}$.

Let $a, b \in \mathbb{Z}, b \ne 0$ be given.

We call $[p\abs{b}, (p + 1)\abs{b})$ the $p$-interval for any value $p \in \mathbb{Z}$.
We first claim that the union of all $p$-intervals over $p \in \mathbb{Z}$ equals $\mathbb{Z}$.

First $k = 0 \in [0 \cdot \abs{b}, (0 + 1) \abs{b})$.
Suppose $k \geq 0$ and $k$ is in the union of all $p$-intervals.
Then $k \in [p'\abs{b}, (p' + 1)\abs{b})$ for some $p'$.
Then $k + 1$ is either in the same $p$-interval or the next one.
By induction, the union of $p$-intervals contains all non-negative numbers, and we can use the same argument to show that it contains all negative numbers.

Now, choose $p \in \mathbb{Z}$ such that $a \in [p\abs{b}, (p + 1)\abs{b})$.

Let $q = \frac{p\abs{b}}{b} = \frac{pb}{\abs{b}}, r = a - qb$.

Then obviously, $a = bq + r$.

Furthermore,

$$
\begin{align*}
    0 \leq r < \abs{b}
    &\iff 0 \leq a - qb < \abs{b} \\
    &\iff qb \leq a < \abs{b} + qb \\
    &\iff p\abs{b} \leq a < \abs{b} + p\abs{b} \\
    &\iff a \in [p\abs{b}, (p + 1)\abs{b}).
\end{align*}
$$


Finally, we claim that such $(q, r)$ is unique.
Let $(q', r')$ be a pair with the same property.


$$
\begin{align*}
    0 \leq r' < \abs{b}
    &\implies 0 \leq a - q'b < \abs{b} \\
    &\implies q'b \leq a < \abs{b} + q'b \\
    &\implies p'b \leq a < (p' + 1)\abs{b}
\end{align*}
$$

with $p' = q'\frac{b}{\abs{b}}$.

$p$-intervals are clearly disjoint for different $p$ values, so $q = q'$.
This implies $r = r'$, so such a pair must be unique.

