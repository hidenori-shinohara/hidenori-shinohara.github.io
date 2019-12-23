---
layout: post
title:  "$\\frac{z - 1}{z - 2} = \\sum_{k \\geq 0} \\frac{1}{(z - 1)^k}$"
date:   2019-12-23
author: Hidenori
---

# Proposition
Show that

$$
\begin{align*}
  \frac{z - 1}{z - 2} = \sum_{k \geq 0}\frac{1}{(z - 1)^k}
\end{align*}
$$

for $\abs{z - 1} > 1$.

# Solution

Suppose $\abs{z - 1} > 1$.

$$
\begin{align*}
  \frac{z - 1}{z - 2}
    &= \frac{z - 1}{(z - 1) - 1} \\
    &= \frac{1}{1 - \frac{1}{z - 1}} \\
    &= \sum_{k \geq 0} \frac{1}{(z - 1)^k}.
\end{align*}
$$
