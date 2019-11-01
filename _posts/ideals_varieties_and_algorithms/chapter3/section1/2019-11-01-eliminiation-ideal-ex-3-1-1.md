---
layout: post
title:  "Basic property of an elimination ideal"
date:   2019-11-01
author: Hidenori
---

# Proposition
Let $I \subset k[x_1, \cdots, x_n]$ be an ideal.
1. Prove that $I_l = I \cap k[x_{l + 1}, \cdots, x_n]$ is an ideal of $k[x_{l + 1}, \cdots, x_n]$.
1. Prove that the ideal $I_{l + 1} \subset k[x_{l + 2}, \cdots, x_n]$ is the first elimination ideal of $I_l \subset k[x_{l + 1}, \cdots, x_n]$.

# Solution

## 1

* $0 \in I_l$, so $I_l$ is nonempty.
* Let $a, b \in I_l$.
  Then $a - b \in I$ because $I$ is an ideal, and $a - b \in k[x_{l + 1}, \cdots, x_n]$.
  Therefore, $a - b \in I_l$.
* $f \in I_l, g \in k[x_{l + 1}, \cdots, x_n]$.
  Then $gf \in k[x_{l + 1}, \cdots, x_n]$ and $gf \in I$.
  Thus $gf \in I_l$.

Hence, $I_l$ is an ideal of $k[x_{l + 1}, \cdots, x_n]$.

## 2

$$
\begin{align*}
  I_{l + 1}
    &= I \cap k[x_{l + 1}, \cdots, x_n] \\
    &= I \cap k[x_{l}, \cdots, x_n] \cap k[x_{l + 1}, \cdots, x_n] \\
    &= I_l \cap k[x_{l + 1}, \cdots, x_n].
\end{align*}
$$
