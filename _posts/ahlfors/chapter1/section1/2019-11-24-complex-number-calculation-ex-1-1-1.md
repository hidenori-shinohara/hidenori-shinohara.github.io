---
layout: post
title:  "Calculation of complex numbers"
date:   2019-11-24
author: Hidenori
---

# Proposition
Find the values of
1. $(1 + 2i)^3$.
1. $\frac{5}{-3 + 4i}$.
1. $\big(\frac{2 + i}{3 - 2i}\big)^2$.
1. $(1 + i)^n + (1 - i)^n$.

# Solution

1. $(1 + 2i)^3 = 1 + 3 \cdot 2i + 3 \cdot (2i)^2 + (2i)^3 = -11 - 2i$.
1. $5 / (-3 + 4i) = 5(3 + 4i) / (-9 - 16) = (3 + 4i) / -5$.
1. $$
   \begin{align*}
     \Big(\frac{2 + i}{3 - 2i}\Big)^2
       &= \Big(\frac{(2 + i)(3 + 2i)}{9 + 4}\Big)^2 \\
       &= \Big(\frac{4 + 7i}{13}\Big)^2 \\
       &= \frac{-33 + 56i}{169}.
   \end{align*}
   $$
1. $$
   \begin{align*}
     (1 + i)^n + (1 - i)^n
      &= \sum_{k=0}^{n} \binom{n}{k} (i^k + (-1)^k) \\
      &= 2\sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} i^{2k} \\
      &= 2\sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} (-1)^k.
   \end{align*}
   $$



