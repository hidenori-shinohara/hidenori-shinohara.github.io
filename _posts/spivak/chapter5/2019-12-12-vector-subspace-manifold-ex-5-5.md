---
layout: post
title:  "A $k$-dimensional vector subspace of $\\mathbb{R}^n$ is a $k$-dimensional manifold"
date:   2019-12-12
author: Hidenori
---

# Proposition
Prove that a $k$-dimensional (vector) subspace of $\mathbb{R}^n$ is a $k$-dimensional manifold.

# Solution
Let $V$ denote the subspace and $v_1, \cdots, v_k$ denote a basis of $V$.
We can extend it to a basis of $V$.
Then $A = \begin{bmatrix} v_1 & \cdots & v_n \end{bmatrix}$ is a invertible matrix.
(Each $v_1, \cdots, v_n$ is a column vector with $n$ entries.)

Let $x = (x_1, \cdots, x_n) = a_1v_1 + \cdots + a_kv_k \in V$ be given.
Then

$$
\begin{align*}
  \begin{bmatrix} v_1 & \cdots & v_n \end{bmatrix}
  \begin{bmatrix} a_1 \\ \vdots \\ a_k \\ 0 \\ \vdots \\ 0 \end{bmatrix}
  &= \begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix}.
\end{align*}
$$

By multiplying $A^{-1}$ from left, we obtain

$$
\begin{align*}
  \begin{bmatrix} a_1 \\ \vdots \\ a_k \\ 0 \\ \vdots \\ 0 \end{bmatrix}
  &= A^{-1}\begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix}.
\end{align*}
$$

Therefore, $A^{-1}$ maps $V$ into a subspace of $\mathbb{R}^n$ whose $k + 1, \cdots, n$th coordinates are all 0 bijectively.
Hence, a $k$-dimensional vector subspace of $\mathbb{R}^n$ is a $k$-dimensional manifold.
