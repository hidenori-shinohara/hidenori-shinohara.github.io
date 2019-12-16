---
layout: post
title:  "The matrix representation of a Mobius transformation"
date:   2019-12-16
author: Hidenori
---

# Proposition
Suppose

$$
\begin{align*}
  A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
\end{align*}
$$

is a $2 \times 2$ matrix of complex numbers whose determinant $ad - bc$ is nonzero.
Then we can define a corresponding Mobius transformation on $\hat{\mathbb{C}}$ by $T_A(z) = \frac{az + b}{cz + d}$.
Show that $T_A \circ T_B = T_{A \cdot B}$, where $\circ$ denotes composition and $\cdot$ denotes matrix multiplication.

# Solution

Let

$$
\begin{align*}
  A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}, B = \begin{bmatrix} e & f \\ g & h \end{bmatrix}.
\end{align*}
$$

Then

$$
\begin{align*}
  T_A \circ T_B
    &= \frac{aT_B(z) + b}{cT_B(z) + d} \\
    &= \frac{a(ez + f) + b(gz + h)}{c(ez + f) + d(gz + h)} \\
    &= \frac{(ae + bg)z + (af + bh)}{(ce + dg)z + (cf + dh)}.
\end{align*}
$$

Since

$$
\begin{align*}
  A \cdot B
    &= \begin{bmatrix}
      ae + bg & af + bh \\
      ce + dg & cf + dh
    \end{bmatrix},
\end{align*}
$$

$T_A \circ T_B = T_{A \cdot B}$.
