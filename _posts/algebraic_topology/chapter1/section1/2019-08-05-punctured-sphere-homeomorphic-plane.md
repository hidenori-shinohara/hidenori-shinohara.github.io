---
layout: post
title:  "$S^n$ with a hole is homeomorphic to $\\mathbb{R}^{n}$"
date:   2019-08-05
author: Hidenori
---

# Proposition
For any $n \in \mathbb{N}$, $S^n \setminus \\{ (0, 0, \cdots, 0, 1) \\}$ is homeomorphic to $\mathbb{R}^{n}$.

# Solution
Let $p = (0, 0, \cdots, 0, 1)$.
We define two functions:

* $f: S^n \setminus p \rightarrow \mathbb{R}^n$ such that $(x_1, \cdots, x_n, x_{n + 1}) \mapsto (x_1 / (1 - x_{n + 1}), \cdots, x_n / (1 - x_{n + 1}))$.
* $g: \mathbb{R}^n \rightarrow S^n \setminus p$ such that $(y_1, \cdots, y_n) \mapsto (y_1t, \cdots, y_nt, 1 - t)$ where $t = 2 / (1 + y_1^2 + \cdots + y_n^2)$.

We claim that $f, g$ are well-defined.

* $x_{n + 1} \ne 0$ because $(x_1, \cdots, x_n, x_{n + 1}) \in S^n \setminus p$, so $f$ is well-defined.
* $(y_1t)^2 + \cdots + (y_nt)^2 + (1 - t)^2 = (y_1^2 + \cdots + y_n^2 + 1)t^2 + 1 - 2t = 2t + 1 - 2t = 1$.
  Moreover, $1 - t \ne 1$ for any $(y_1, \cdots, y_n)$, so $g$ is well-defined.

Since each component function of $f$ and $g$ is continuous, they are both continuous.
We claim that $f$ and $g$ are the inverse of each other.
We will show that by showing $f \circ g$ and $g \circ f$ are both the identity function.

* Is $f \circ g$ the identity function on $\mathbb{R}^n$?
    * Let $(y_1, \cdots, y_n) \in \mathbb{R}^n$ be given.

      $$
      \begin{align*}
        (f \circ g)(y_1, \cdots, y_n)
          &= f(y_1t, \cdots, y_nt, 1 - t) \\
          &= (y_1t / (1 - (1 - t)), \cdots, y_nt / (1 - (1 - t))) \\
          &= (y_1, \cdots, y_n).
      \end{align*}
      $$
* Is $g \circ f$ the identity function on $S^n \setminus p$?
    * Let $(x_1, \cdots, x_n, x_{n + 1}) \in \mathbb{S}^n \setminus p$ be given.

      $$
      \begin{align*}
        (g \circ f)(x_1, \cdots, x_n, x_{n + 1})
          &= g(x_1 / (1 - x_{n + 1}), \cdots, x_n / (1 - x_{n + 1})) \\
          &= (tx_1 / (1 - x_{n + 1}), \cdots, tx_n / (1 - x_{n + 1}), 1 - t).
      \end{align*}
      $$

      where $t = 1 - x_{n + 1}$ because

      $$
      \begin{align*}
        t &= \frac{2}{1 + x_1^2 / (1 - x_{n + 1})^2 + \cdots + x_n^2 / (1 - x_{n + 1})^2} \\
          &= \frac{2}{1 + (1 - x_{n + 1}^2) / (1 - x_{n + 1})^2} \\
          &= \frac{2}{1 + (1 + x_{n + 1}) / (1 - x_{n + 1})} \\
          &= 1 - x_{n + 1}.
      \end{align*}
      $$

      Thus $(g \circ f)(x) = x$.

Therefore, $f$ is a homeomorphism, and thus $S^n \setminus p$ is homeomorphic to $\mathbb{R}^n$.
