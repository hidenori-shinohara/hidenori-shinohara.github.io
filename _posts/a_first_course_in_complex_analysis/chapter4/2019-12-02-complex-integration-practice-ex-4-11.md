---
layout: post
title:  "Complex integration examples"
date:   2019-12-02
author: Hidenori
---

# Proposition
Let $I(k) = \frac{1}{2\pi} \int_{0}^{2\pi} e^{ikt} dt$.

1. Show that $I(0) = 1$.
1. Show that $I(k) = 0$ if $k$ is a nonzero integer.
1. What is $I(1/2)$?

# Solution

## 1
$I(0) = \frac{1}{2\pi}\int_{0}^{2\pi} 1dt = 1$.

## 2

$$
\begin{align*}
  I(k)
    &= \frac{1}{2\pi} \int_{0}^{2\pi} e^{ikt} dt \\
    &= \frac{1}{2\pi} \int_{0}^{2\pi} \cos(kt) + i\sin(kt) dt \\
    &= \frac{1}{2\pi} [\int_{0}^{2\pi} \cos(kt) dt + i\int_0^{2\pi} \sin(kt) dt] \\
    &= \frac{1}{2\pi} [\frac{\sin(kt)}{k} \Big\vert^{2\pi}_0 - i\frac{\cos(kt)}{k} \Big\vert^{2\pi}_0] \\
    &= \frac{1}{2\pi} \cdot 0 \\
    &= 0.
\end{align*}
$$

This argument does not work when $k = 0$ because $\frac{1}{0}$ does not make sense.

## 3
By the argument above, it suffices to calculate $\sin(t/2)\Big\vert^{2\pi}_0 - i\cos(t/2)\Big\vert^{2\pi}_0$.
Since it equals $2i$, the answer is $2i/\pi$.
