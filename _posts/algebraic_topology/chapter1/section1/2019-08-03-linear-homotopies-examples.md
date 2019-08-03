---
layout: post
title:  "Linear homotopies in $\\mathbb{R}^n$"
date:   2019-08-03
author: Hidenori
---

# Proposition
Let $x_0, x_1 \in \mathbb{R}^n$ be given.
Let $f_0, f_1$ be two paths from $x_0$ to $x_1$ in $\mathbb{R}^n$.
Then $f_0$ and $f_1$ are homotopic.

# Solution

Consider the family of functions $f_t(s) = (1 - t)f_0(s) + tf_1(s)$.
We claim that it is a homotopy of $f_0$ and $f_1$.

* Let $t \in [0, 1]$.
    * $f_t(0) = (1 - t)f_0(0) + tf_1(0) = (1 - t)x_0 + tx_0 = x_0$.
    * $f_t(1) = (1 - t)f_0(1) + tf_1(1) = (1 - t)x_1 + tx_1 = x_0$.

  Thus the end points $f_t(0) = x_0$ and $f_t(1) = x_1$ are independent of $t$.
* Define $F(s, t) = f_t(s)$.
  We will show that it is continuous.
  Let $(f_{0, 1}, \cdots, f_{0, n}), (f_{1, 1}, \cdots, f_{1, n})$ be the component functions of $f_0, f_1$, respectively.
  By Theorem 18.4 from Munkres, each component function is continuous.
  Each component function of $F(s, t)$ is $(1 - t)f_{0, k}(s) + tf_{1, k}(s)$ for each $k$.
  By Theorem 21.5 from Munkres, the addition, subtraction, and multiplication of real continuous functions is continuous.
  Then each component function of $F(s, t)$ is continuous, $F(s, t)$ is continuous by Theorem 18.4 from Munkres.

Thus $f_0$ and $f_1$ are homotopic.
