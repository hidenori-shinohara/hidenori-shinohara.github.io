---
layout: post
title:  "Parametrization and integral"
date:   2019-12-06
author: Hidenori
---

# Proposition
Let $c$ be a singular $k$-cube and $p:[0, 1]^k \rightarrow [0, 1]^k$ a 1-1 function such that $p([0, 1]^k) = [0, 1]^k$ and $\det(p'(x)) \geq 0$ for $x \in [0, 1]^k$.
If $\omega$ is a $k$-form, show that

$$
\begin{align*}
  \int_{c} \omega = \int_{c \circ p} \omega.
\end{align*}
$$

# Solution
Let $\omega_{i_1, \cdots, i_k}$ be chosen such that $c^*\omega = \sum_{i_1 < \cdots < i_k} \omega_{i_1, \cdots, i_k} dx^{i_1} \wedge \cdots \wedge dx^{i_k}$.

$$
\begin{align*}
  \int_{c \circ p} \omega
    &= \int_{[0, 1]^k} (c \circ p)^*\omega \\
    &= \int_{[0, 1]^k} p^*(c^*\omega) \\
    &= \int_{[0, 1]^k} p^*(\sum_{i_1 < \cdots < i_k} \omega_{i_1, \cdots, i_k} dx^{i_1} \wedge \cdots \wedge dx^{i_k}) \\
    &= \int_{[0, 1]^k} p^*(\sum_{i_1 < \cdots < i_k} \omega_{i_1, \cdots, i_k} dx^{i_1} \wedge \cdots \wedge dx^{i_k}) \\
    &= \sum_{i_1 < \cdots < i_k} \int_{[0, 1]^k} p^*(\omega_{i_1, \cdots, i_k} dx^{i_1} \wedge \cdots \wedge dx^{i_k}) & \text{(Theorem 4.8(2)[Spivak])} \\
    &= \sum_{i_1 < \cdots < i_k} \int_{[0, 1]^k} (\omega_{i_1, \cdots, i_k} \circ p) (\det p') dx^{i_1} \wedge \cdots \wedge dx^{i_k} & \text{(Theorem 4.9[Spivak])} \\
    &= \sum_{i_1 < \cdots < i_k} \int_{[0, 1]^k} (\omega_{i_1, \cdots, i_k} \circ p) \abs{\det p'} dx^{i_1} \wedge \cdots \wedge dx^{i_k} & (\det p' > 0) \\
    &= \sum_{i_1 < \cdots < i_k} \int_{[0, 1]^k} \omega_{i_1, \cdots, i_k} dx^{i_1} \wedge \cdots \wedge dx^{i_k} & \text{(Theorem 3-13)} \\
    &= \int_{[0, 1]^k} c^*\omega \\
    &= \int_{c} \omega.
\end{align*}
$$
