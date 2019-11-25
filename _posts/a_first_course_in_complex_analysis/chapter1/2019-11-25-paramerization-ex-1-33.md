---
layout: post
title:  "Parametrization for paths in the complex plane"
date:   2019-11-25
author: Hidenori
---

# Proposition
Find a parametrization for each of the following paths:
1. The circle $C[1 + i, 1]$, oriented counter-clockwise.
1. The line segment from $-1 - i$ from $2i$.
1. The top half of the circle $C[0, 34]$, oriented clockwise.
1. The rectangle with vertices $\pm 1 \pm 2i$, oriented counter-clockwise.
1. The ellipse $\\{ z \in \mathbb{C}: \abs{z - 1} + \abs{z + 1} = 4 \\}$, oriented counter-clockwise.

# Solution
## 1
$\gamma(t) = 1 + i + e^{2\pi it}$ with $0 \leq t \leq 1$.

## 2
$\gamma(t) = t + (3t + 2)i$ with $-1 \leq t \leq 0$.

## 3
$\gamma(t) = 34e^{-2\pi it}$ with $1/2 \leq t \leq 1$.

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

## 5

$\gamma(t) = 2\cos(t) + i\sqrt{3}\sin(t)$.

Justification:

$$
\begin{align*}
  \abs{\gamma(t) - 1} + \abs{\gamma(t) + 1}
    &= \sqrt{(2\cos t - 1)^2 + 3\sin^2t} + \sqrt{(2\cos t - 1)^2 + 3\sin^2t} \\
    &= \sqrt{\cos^2 t - 4\cos t + 4} + \sqrt{\cos^2 t + 4\cos t + 4} \\
    &= \abs{\cos t - 2} + \abs{\cos t + 2} \\
    &= 2 - \cos t + \cos t + 2 \\
    &= 4.
\end{align*}
$$
