---
layout: post
title:  "The relation of homotopy on paths with fixed end points is an equivalence relation."
date:   2019-08-03
author: Hidenori
---

# Proposition
Let $x_0, x_1 \in X$ be given.
Then the relation of homotopy on paths from $x_0$ to $x_1$ is an equivalence relation.

# Solution
Let $f$ be a path from $x_0$ to $x_1$.

Consider $f_t(s) = f(s)$.

* $f_0 = f_1 = f$.
* For any $t \in [0, 1]$, $f_t(0) = f(0) = x_0$ and $f_t(1) = f(1) = x_1$. 
* Let $F(s, t) = f_t(s)$.
  Then $F = f \circ \pi_1$.
  Since a composition of two continuous functions is continuous, $F$ is continuous.

Therefore, $\\{ f_t \mid t \in I \\}$ is a homotopy, and thus $f \simeq f$.

Let $f_0, f_1$ be paths from $x_0$ to $x_1$.
Suppose that $f_0 \simeq f_1$.
Let $\\{ f_t \mid t \in I \\}$ be a homotopy from $f_0$ to $f_1$.

Let $g_t = f_{1 - t}$.
Then we claim that $\\{ g_t \mid t \in I \\}$ is a homotopy from $f_1$ to $f_0$.

* $g_0 = f_1$ and $g_1 = f_0$.
* Let $t \in [0, 1]$ be given.
  Then $g_t(0) = f_{1 - t}(0) = x_0$, and $g_t(1) = f_{1 - t}(1) = x_1$.
* Let $G(s, t) = g_t(s), F(s, t) = f_t(s)$.
  Then $G(s, t) = g_t(s) = f_{1 - t}(s) = F(s, 1 - t)$.
  The mapping $t \mapsto 1 - t$ is continuous, so $s \times t \mapsto s \times 1 - t$ is also continuous.
  Since a composition of two continuous functions is continuous, $G$ is continuous.

Thus $g_t$ is a homotopy, so $f_1 \simeq f_0$.
This proves the reflexivity.

Let $f_0, f_1, f_2$ be paths from $x_0$ to $x_1$.
Suppose that $f_0 \simeq f_1, f_1 \simeq f_2$.

Let $g_t, h_t$ be homotopies of $f_0, f_1$ and $f_1, f_2$, respectively.

For each $t \in I$, define $f_t: I \rightarrow X$ such that

$$
\begin{align*}
  f_t(s) = \begin{cases}
    g_{2t}(s) & (t \leq 1 / 2) \\
    h_{2t - 1}(s) & (t \geq 1 / 2).
  \end{cases}
\end{align*}
$$

* $f_t(s)$ is well-defined because $g_1(s) = f_1(s) = h_0(s)$.
* Let $t \in I$ be given.
    * If $t \leq 1 / 2$, then $f_t(0) = g_{2t}(0) = x_0$ and $f_t(1) = g_{2t}(1) = x_1$.
    * If $t \geq 1 / 2$, then $f_t(0) = h_{2t - 1}(0) = x_0$ and $f_t(1) = h_{2t - 1}(1) = x_1$.
* Let $F(s, t) = f_t(s)$.
    * $t \mapsto 2t$ is continuous, so $s \times t \mapsto s \times 2t$ is continuous.
      Then $F$ is continuous on $I \times [0, 1/2]$ because $F$ is a composition of continuous functions.
    * Similarly, $F$ is continuous on $I \times [1/2, 1]$ because $F$ is a composition of continuous functions.
    * By the pasting lemma, $F$ is continuous on $I \times I$.

Therefore, $f_0 \simeq f_2$.


Hence, $\simeq$ is an equivalence relation.
