---
layout: post
title:  "Path integrals"
date:   2019-11-27
author: Hidenori
---

# Proposition
Evaluate the integrals $\int_{\gamma} xdz, \int_{\gamma} ydz, \int_{\gamma}zdz$ and $\int_{\gamma}\overline{z}dz$ along each of the following paths.

1. $\gamma$ is the line segment from $0$ to $1 - i$.
1. $\gamma = C[0, 1]$.
1. $\gamma = C[a, r]$ for some $a \in \mathbb{C}$.

# Solution
## 1

$\gamma(t) = t - it$ with $0 \leq t \leq 1$.
Then $\gamma'(t) = 1 - i$.

* $\int_{\gamma} xdz = \int_{0}^{1} x(\gamma(t))\gamma'(t)dt = \int_{0}^{1} t(1 - i)dt = (1 - i)t^2/2 \vert^{1}_0 = (1 - i)/2$.
* $\int_{\gamma} ydz = \int_{0}^{1} y(\gamma(t))\gamma'(t)dt = \int_{0}^{1} (-t)(1 - i)dt = (i - 1)t^2/2 \vert_0^1= (i - 1)/2$.
* $\int_{\gamma} zdz = ((1 - i) + i(1 - i)) / 2 = 1$.
* $\int_{\gamma} \overline{z}dz = ((1 - i) - i(1 - i)) / 2 = -i$.

## 2
It suffices to solve 3.

## 3

Let $a = (x_0, y_0$.
$\gamma(t) = a + re^{it} = (x_0 + r\cos t) + i(y_0 + r\sin t)$, and $\gamma'(t) = -r\sin t + ir \cos t$.

$$
\begin{align*}
  \int_{\gamma} xdz
    &= \int_{0}^{2\pi} (x_0 + r\cos t)(-r\sin t)dt \\
    &= \int_{0}^{2\pi} -rx_0\sin t - r^2\sin t \cos t dt \\
    &= \int_{0}^{2\pi} -rx_0\sin t - \frac{r^2\sin 2t}{2} t dt \\
    &= rx_0\cos t + r^2\frac{\cos2t}{4} \big\vert_0^{2\pi} \\
    &= 0.
\end{align*}
$$

On the other hand,

$\int_{\gamma} zdz = \int_{0}^{2\pi} (a + re^{it})(rie^{it}) dt = are^{it} + r^2e^{2it}/2 \big\vert^{2\pi}_0 = 0$.

Therefore, $\int_{\gamma} ydz = \int_{\gamma} \overline{z}dz = 0$.
