---
layout: post
title:  "Laurent series for $\\frac{1}{z(z - 2)^2}$"
date:   2019-12-22
author: Hidenori
---

# Proposition
Find a Laurent series for

$$
\begin{align*}
  \frac{1}{z(z - 2)^2}
\end{align*}
$$

centered at $z = 2$ and specify the region in which it converges.

# Solution

$$
\begin{align*}
  \frac{1}{z(z - 2)^2}
    &= \frac{1}{(z - 2 + 2)(z - 2)^2} \\
    &= \frac{1}{(z - 2)^3 + 2(z - 2)^2} \\
    &= \frac{1}{2(z - 2)^2}\frac{1}{1 + \frac{z - 2}{2}} \\
    &= \frac{1}{2(z - 2)^2}\sum_{i=0}^{\infty} \Big(\frac{z - 2}{-2}\Big)^i \\
    &= \frac{1}{8}\sum_{i=0}^{\infty} \Big(\frac{z - 2}{-2}\Big)^{i - 2} \\
    &= \sum_{i=0}^{\infty} \frac{-1}{(-2)^{i + 3}} (z - 2)^i.
\end{align*}
$$

Since a geometric series converges if and only if the absolute value of the common ratio is less than 1, the series converges if and only if $\abs{z - 2} < 2$.
