---
layout: post
title:  "Mobius transformations"
date:   2019-12-18
author: Hidenori
---

# Proposition
Find each Mobius transformation $f$:
1. $f$ maps $0 \rightarrow 1, 1 \rightarrow \infty, \infty \rightarrow 0$.
1. $f$ maps $1 \rightarrow 1, -1 \rightarrow i, -i \rightarrow -1$.
1. $f$ maps the $x$-axis to $y = x$, the $y$-axis to $y = -x$, and the unit circle to itself.

# Solution
We will use the cross-ratio formula, which is

$$
\begin{align*}
  \frac{(z - z_1)(z_2 - z_3)}{(z - z_3)(z_2 - z_1)}
\end{align*}
$$

sends $(z_1, z_2, z_3)$ to $(0, 1, \infty)$.

## 1
By setting $z_1 = \infty, z_2 = 0, z_3 = 1$,

$$
\begin{align*}
  \frac{(z - \infty)(0 - 1)}{(z - 1)(0 - \infty)}
    &= \frac{(z / \infty - 1)(0 - 1)}{(z - 1)(0 - 1)} \\
    &= \frac{(0 - 1)(0 - 1)}{(z - 1)(0 - 1)} \\
    &= \frac{1}{1 - z}.
\end{align*}
$$

Dividing $\infty$ by $\infty$ is not exactly rigorous, but it is easy to show that this map satisfies the requirements.

## 2
We will construct two Mobius transformation:

* A Mobius transformation $f_1$ that maps $(1, -1, -i)$ to $(0, 1, \infty)$,
* A Mobius transformation $f_2$ that maps $(1, i, -1)$ to $(0, 1, \infty)$,

By using the cross ratio formula,

$$
\begin{align*}
  f_1(z) &= \frac{(i - 1)z + (1 - i)}{-2z - 2i}, \\
  f_2(z) &= \frac{-iz + i}{z + 1} \\
\end{align*}
$$

$f_2^{-1} \cdot f_1$ is the desired Mobius transformation.

[By using the connection between matrices and Mobius transformations](/2019/12/16/mobius-transformation-matrix-ex-3-10.html),

$$
\begin{align*}
  \begin{bmatrix}
    -i & i \\
    1 & 1
  \end{bmatrix}^{-1}
  \begin{bmatrix}
    (i - 1) & (1 - i) \\
    -2 & -2i
  \end{bmatrix}
  &= \begin{bmatrix}
    1 & -i \\
    -1 & -i
  \end{bmatrix}
  \begin{bmatrix}
    (i - 1) & (1 - i) \\
    -2 & -2i
  \end{bmatrix} \\
  &= \begin{bmatrix}
    3i - 1 & -1 - i \\
    i + 1 & i - 3
  \end{bmatrix}.
\end{align*}
$$

Thus the desired Mobius transformation is

$$
\begin{align*}
  \frac{(3i - 1)z - (1 + i)}{(i + 1)z + (i - 3)}.
\end{align*}
$$

## 3
$f$ simply rotates the complex plane by 45 degrees.
Thus $f(z) = e^{\pi i / 2}z = z(1 + i) / \sqrt{2}$.
