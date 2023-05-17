---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Intersections of lines and conics"
date:   2023-05-17
author: Hidenori
---

Exercise from P.40 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> In how many points can two arbitrary lines (in the plane) intersect?

For each $i = 1, 2$, let $f_i(x, y) = a_ix + b_iy + c_i$.

Then $f_1, f_2$ intersect at $(x_0, y_0)$ if and only if

$$
\begin{align*}
  \begin{bmatrix}
    a_1 & b_1 & c_1 \\
    a_2 & b_2 & c_2
  \end{bmatrix}
  \begin{bmatrix}
    x_0 \\ y_0 \\ 1
  \end{bmatrix} = 0
\end{align*}
$$

Notice that the condition stays equivalent if we replace the coefficient matrix with its row reduced echelon form through elementary operations.

Suppose the following is the row reduced echelon form.

$$
\begin{align*}
  \begin{bmatrix}
    a_1' & b_1' & c_1' \\
    a_2' & b_2' & c_2'
  \end{bmatrix}
\end{align*}
$$

There are a few cases:

- Case 1: $a_1' = 1$
    - Case 1.1: $b_2' = 1$. Then this uniquely determines $x_0, y_0$, so there is only one intersection.
    - Case 1.2: $b_2' = 0$.
        - Case 1.2.1: $c_2' = 1$. Since $a_2' = b_2' = 0$, there is no solution.
        - Case 1.2.2: $c_2' = 0$.
          Then the solution is equivalent to the zero set of $a_1'x + b_1'y + c_1'$.
          In other words, there's infinitely many solutions.
- Case 2: $a_1' = 0$
    - Case 2.1: $b_1' = 1$.
        - Case 2.1.1: $c_2' = 1$. Since $a_2' = b_2' = 0$, there is no solution.
        - Case 2.1.2: $c_2' = 0$.
          Then the solution is equivalent to the zero set of $a_1'x + b_1'y + c_1'$.
          In other words, there's infinitely many solutions.
    - Case 2.2: $b_1' = 0$.
        - This case is not possible if some of $a_1, a_2, b_1, b_2$ are non zero, which it should be.

Therefore, we proved that the number of intersections must be either 0, 1, or infinite.
