---
layout: post
title:  "Any monic polynomial over a ring is not a zero divisor"
date:   2019-10-09
author: Hidenori
---

# Proposition
Let $A$ be any ring, and consider the polynomial ring $A[T]$.
Prove that $T$ is not a zero divisor in $A[T]$.
Generalize the argument to prove that a monic polynomial

$$
\begin{align*}
  f = T^n + a_{n - 1}T^{n - 1} + \cdots + a_0
\end{align*}
$$

is not a zero divisor in $A[T]$.

# Solution
We will only prove the second part because the first part is implied by the second part.

Let $g = b_mT^m + b_{m - 1}T^{m - 1} + \cdots + b_0 \in A[t]$ be given.
Suppose $g \ne 0$.
Without loss of generality, we will assume that $b_m \ne 0$.

Then $fg = b_mT^{n + m} + (a_{n - 1}b_m + b_{m - 1})T^{n + m - 1} + \cdots + a_0b_0$.
Since the coefficient of $T^{n + m}$ is $b_m$ and $b_m \ne 0$, $fg \ne 0$.
Therefore, $f$ is not a zero divisor.
