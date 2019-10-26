---
layout: post
title:  "Parametrization of linear equations"
date:   2019-10-26
author: Hidenori
---

# Proposition

Parametrize all solutions to the linear equations

$$
\begin{align*}
  x + 2y - 2z + w &= -1, \\
  x + y + z - w &= 2.
\end{align*}
$$

# Solution

From

$$
\begin{align*}
  \begin{bmatrix}
    1 & 2 & -2 & 1 \\
    1 & 1 & 1 & -1
  \end{bmatrix}
  \begin{bmatrix}
    x \\ y \\ z \\ w
  \end{bmatrix}
  = \begin{bmatrix}
    -1 \\ 2
  \end{bmatrix},
\end{align*}
$$

we get $(x, y, z, w) = (-4t + 3s, 3t - 2s, t, s)$.
