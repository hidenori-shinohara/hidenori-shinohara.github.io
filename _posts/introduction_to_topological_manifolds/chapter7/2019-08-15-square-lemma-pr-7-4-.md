---
layout: post
title:  "Square Lemma"
date:   2019-08-15
author: Hidenori
---

# Proposition
Let $F: I \times I \rightarrow X$ be a continuous map, and let $f, g, h$, and $k$ be the paths in $X$ defined by

$$
\begin{align*}
  f(s) &= F(s, 0); \\
  g(s) &= F(1, s); \\
  h(s) &= F(0, s); \\
  k(s) &= F(s, 1).
\end{align*}
$$

Then $f \cdot g \sim h \cdot k$.

# Solution

It makes sense to consider $f \cdot g \sim h \cdot k$ because:
* $f \cdot g$ is well-defined because $f(1) = F(1, 0) = g(0)$.
* $h \cdot k$ is well-defined because $h(1) = F(0, 1) = k(0)$.
* $(f \cdot g)(0) = F(0, 0) = (h \cdot k)(0)$.
* $(f \cdot g)(1) = F(1, 1) = (h \cdot k)(1)$.

Let $G: I \times I \rightarrow X$ be defined such that

$$
\begin{align*}
  G(s, t) &= \begin{cases}
    F(2s(1 - t), 2st) & (s \in [0, 1/2]) \\
    F(1 - 2(1 - s)t, 1 - 2(1 - s)(1 - t)) & (s \in [1/2, 1]).
  \end{cases}
\end{align*}
$$

This formula can be derived by comparing squares.
Yes, it was rather tedious.

![Squares](/assets/introduction_to_topological_manifolds/chapter7/square-lemma.jpeg)

$G$ is well-defined because:

* Let $s \in [0, 1/2], t \in I$.
    * $2s(1 - t) \in I$ because $2s \in I$ and $1 - t \in I$.
* Let $s \in [1/2, 1], t \in I$.
    * $2(1 - s) \in I$ and $t \in I$, so $2(1 - s)t \in I$.
      Thus $1 - 2(1 - s)t \in I$.
    * $2(1 - s) \in I$ and $1 - t \in I$.
      Thus $2(1 - s)(1 - t) \in I$, so $1 - 2(1 - s)(1 - t) \in I$.
* Let $s = 1/2, t \in I$.
    * $F(2s(1 - t), 2st) = F(1 - t, t)$.
    * $F(1 - 2(1 - s)t, 1 - 2(1 - s)(1 - t)) = F(1 - t, 1 - (1 - t)) = F(1 - t, t)$.
      

Each of $2s(1 - t), 2st, 1 - 2(1 - s)t, 1 - 2(1 - s)(1 - t)$ is continuous.
Compositions of continuous functions are continuous, so $F(2s(1 - t), 2st)$ and $F(1 - 2(1 - s)t, 1 - 2(1 - s)(1 - t))$ are continuous.
By the pasting lemma, $G$ is continuous.

We claim that $G$ is a path homotopy from $f \cdot g$ to $h \cdot k$.

* Let $t = 0$.
    * Let $s \in [0, 1/2]$.
        * $G(s, t) = F(2s(1 - t), 2st) = F(2s, 0) = f(2s) = (f \cdot g)(s)$.
    * Let $s \in [1/2, 1]$.
        * $G(s, t) = F(1 - 2(1 - s)t, 1 - 2(1 - s)(1 - t)) = F(1, 2s - 1) = g(2s - 1) = (f \cdot g)(s)$.
* Let $t = 1$.
    * Let $s \in [0, 1/2]$.
        * $G(s, t) = F(2s(1 - t), 2st) = F(0, 2s) = h(2s) = (h \cdot k)(s)$.
    * Let $s \in [1/2, 1]$.
        * $G(s, t) = F(1 - 2(1 - s)t, 1 - 2(1 - s)(1 - t)) = F(2s - 1, 1) = k(2s - 1) = (h \cdot k)(s)$.
* Let $s = 0$.
    * For any $t \in I$, $G(s, t) = F(0, 0)$.
* Let $s = 1$.
    * For any $t \in I$, $G(s, t) = F(1, 1)$.

Therefore, $G$ is indeed a path homotopy from $f \cdot g$ to $h \cdot k$.

