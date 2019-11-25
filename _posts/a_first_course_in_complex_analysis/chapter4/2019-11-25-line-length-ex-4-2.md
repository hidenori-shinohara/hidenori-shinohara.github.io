---
layout: post
title:  "Line length calculation"
date:   2019-11-25
author: Hidenori
---

# Proposition
Compute the lengths of the paths [from this post](/2019/11/25/paramerization-ex-1-33):

1. The circle $C[1 + i, 1]$, oriented counter-clockwise.
1. The line segment from $-1 - i$ from $2i$.
1. The top half of the circle $C[0, 34]$, oriented clockwise.
1. The rectangle with vertices $\pm 1 \pm 2i$, oriented counter-clockwise.

# Solution
## 1
$\gamma(t) = 1 + i + e^{2\pi it}$ with $0 \leq t \leq 1$.

$\int_{0}^{1} \abs{\gamma'(t)} dt = 2\pi \int_0^1 1 dt = 2\pi$.

## 2
$\gamma(t) = t + (3t + 2)i$ with $-1 \leq t \leq 0$.
$\int_{-1}^{0} \abs{\gamma'(t)} dt = \int_{-1}^{0} \sqrt{1 + 9}dt = \sqrt{10}$.

## 3
$\gamma(t) = 34e^{-2\pi it}$ with $1/2 \leq t \leq 1$.
$\int_{1/2}^{1} \abs{34e^{-2\pi it} \cdot -2\pi i} dt = 68\pi / 2 = 34\pi$.

## 4

$$
\begin{align*}
  \gamma(t)
    &= \begin{cases}
      1 + (t - 2)i & (0 \leq t \leq 4) \\
      1 - (t - 4) + 2i & (4 \leq t \leq 6) \\
      -1 + (2 - (t - 6))i & (6 \leq t \leq 10) \\
      -1 + (t - 10) - 2i & (10 \leq t \leq 12).
    \end{cases}
\end{align*}
$$

$\int_{0}^{4} \abs{i} dt + \int_{4}^{6} \abs{-1} dt + \int_{6}^{10} \abs{-i} dt + \int_{10}^{12} \abs{1} dt = 12$
