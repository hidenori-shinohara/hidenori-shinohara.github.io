---
layout: post
title:  "Integration over paths"
date:   2019-11-26
author: Hidenori
---

# Proposition
Integrate the function $f(z) = \overline{z}$ over the following paths:

1. $\gamma(t) = t + it (0 \leq t \leq 1)$.
1. $\gamma(t) = t + it^2 (0 \leq t \leq 1)$.
1. $\gamma_1(t) = t$ with $0 \leq t \leq 1$, and $\gamma_2(t) = 1 + it$ with $0 \leq t \leq 1$.

# Solution
## 1

$$
\begin{align*}
  \int_{0}^{1} f(\gamma(t))\gamma'(t) dt
    &= \int_{0}^{1} (t - it)(1 + i) dt \\
    &= \int_{0}^{1} (1 + 1)t dt \\
    &= 1.
\end{align*}
$$

## 2

$$
\begin{align*}
  \int_{0}^{1} f(\gamma(t))\gamma'(t) dt
    &= \int_{0}^{1} (t - it^2)(1 + 2it) dt \\
    &= \int_{0}^{1} t + it^2 + 2t^3 dt \\
    &= 1 + i/3.
\end{align*}
$$

## 3

$$
\begin{align*}
  \int_{0}^{1} f(\gamma_1(t))\gamma_1'(t) dt + \int_{0}^{1} f(\gamma_2(t))\gamma_1'(t) dt
    &= \int_{0}^{1} t dt + \int_{0}^{1} (-i) \cdot i dt \\
    &= 1/2 + 1 = 3/2.
\end{align*}
$$
