---
layout: post
title:  "Integral over a circle"
date:   2019-11-26
author: Hidenori
---

# Proposition
Integrate the following functions over the circle $C[0, 2]$:
1. $f(z) = z + \overline{z}$.
1. $f(z) = \frac{1}{z^4}$.
1. $f(z) = z^2 - 2z + 3$.
1. $f(z) = xy$.

# Solution
The circle can be parametrized as $\gamma(t) = 2\exp(it) = 2\cos(t) + 2i\sin(t)$.
Then $\gamma'(t) = 2i\exp(it) = -2\sin(t) + 2i\cos(t)$.

## 1

$$
\begin{align*}
  \int_{0}^{2\pi} f(\gamma(t))\gamma'(t)dt
    &= \int_{0}^{2\pi} -8\sin t \cos t + 8i \cos^2(t) dt \\
    &= \int_{0}^{2\pi} -4\sin 2t + 4i (\cos(2t) + 1) dt \\
    &= 2\cos(2t) + 2i\sin(2t) + 4ti \Big\vert^{2\pi}_0 \\
    &= 8\pi i.
\end{align*}
$$

## 2

$$
\begin{align*}
  \int_{0}^{2\pi} f(\gamma(t))\gamma'(t)dt
    &= \int_{0}^{2\pi} \frac{2i}{16e^{3it}} dt \\
    &= \frac{ie^{-3it}}{-24i}\Big\vert^{2\pi}_0 \\
    &= 0.
\end{align*}
$$

##  3

$$
\begin{align*}
  \int_{0}^{2\pi} f(\gamma(t))\gamma'(t)dt
    &= \int_{0}^{2\pi} (4e^{2it} - 4e^{it} + 3)2ie^{it} dt \\
    &= \int_{0}^{2\pi} 8ie^{3it} - 8ie^{2it} + 6ie^{it} dt \\
    &= 2e^{4it} - 4e^{2it} + 6e^{it} \Big\vert^{2\pi}_0 = 0.
\end{align*}
$$

##  4

$$
\begin{align*}
  \int_{0}^{2\pi} f(\gamma(t))\gamma'(t)dt
    &= 2\int_{0}^{2\pi} - \cos t \sin^2t + i\cos^2 t \sin t dt \\
    &= 2(-\frac{\sin^3t}{3}\Big\vert^{2\pi}_0 + i\frac{\cos^3t}{-3}\Big\vert^{2\pi}_0) \\
    &= 2 \cdot 0 = 0.
\end{align*}
$$
