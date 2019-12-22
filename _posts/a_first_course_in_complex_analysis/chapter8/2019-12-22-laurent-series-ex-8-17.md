---
layout: post
title:  "Laurent series for $\\frac{1}{(z - 1)(z + 1)}$"
date:   2019-12-22
author: Hidenori
---

# Proposition
Find a Laurent series for

$$
\begin{align*}
  \frac{1}{(z - 1)(z + 1)}
\end{align*}
$$

centered at $z = 1$ and specify the region in which it converges.

# Solution

$$
\begin{align*}
  \frac{1}{(z - 1)(z + 1)}
    &= \frac{1}{(z - 1)(z - 1 + 2)} \\
    &= \frac{1}{(z - 1)^2 + 2(z - 1)} \\
    &= \frac{1}{2(z - 1)}\frac{1}{\frac{z - 1}{2} + 1} \\
    &= \frac{1}{2(z - 1)}\frac{1}{1 - \frac{z - 1}{2}} \\
    &= \frac{1}{2(z - 1)}\sum_{k=0}^{\infty} \Big(\frac{1 - z}{2}\Big)^k \\
    &= \frac{1}{4}\sum_{k=0}^{\infty} \Big(\frac{1 - z}{2}\Big)^{k - 1} \\
    &= \frac{1}{4}\sum_{k=-1}^{\infty} \Big(\frac{1 - z}{2}\Big)^k \\
    &= \frac{1}{4}\sum_{k=-1}^{\infty} \frac{1}{2^k}(1 - z)^k \\
    &= \sum_{k=-1}^{\infty} \frac{1}{2^{k + 2}}(1 - z)^k \\
    &= \sum_{k=-1}^{\infty} \frac{1}{(-2)^{k + 2}}(z - 1)^k.
\end{align*}
$$

From calculus, we know that a geometric series converges if and only if the common ratio is less than 1.
Thus this converges if and only if $\abs{1 - z} < \abs{-2} = 2$.
In other words, the region in which it converges is the interior of the disk with center at 1 and radius 2.
