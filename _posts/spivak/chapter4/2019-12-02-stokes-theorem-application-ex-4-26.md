---
layout: post
title:  "A simple application of Stokes' theorem"
date:   2019-12-02
author: Hidenori
---

# Proposition
Show that $\int_{C_{R, n}} d\theta = 2\pi n$, and use Stokes' theorem to conclude that $C_{R, n} \ne \partial c$ for any 2-chain $c$ in $\mathbb{R}^2 - 0$.

# Solution

$$
\begin{align*}
  \int_{C_{R, n}} d\theta
    &= \int_{C_{R, n}} \frac{-y}{x^2 + y^2}dx + \frac{x}{x^2 + y^2} dy & \text{(P.93, Spivak)} \\
    &= \int_{[0, 1]} C^*_{R, n}(\frac{-y}{x^2 + y^2}dx + \frac{x}{x^2 + y^2} dy) & \text{(P.101, Spivak)}  \\
    &= \int_{[0, 1]} (h_1 \circ C_{R, n})\frac{\partial C_{R, n}^1}{\partial t} dt + (h_2 \circ C_{R, n})\frac{\partial C_{R, n}^2}{\partial t} dt \\
    &= \int_{[0, 1]} 2\pi n(\sin^2(2\pi nt) + \cos^2(2\pi nt)) dt \\
    &= \int_{[0, 1]} 2\pi n dt = 2\pi n
\end{align*}
$$

where $h_1(x, y) = \frac{-y}{x^2 + y^2}$ and $h_2 (x, y)= \frac{x}{x^2 + y^2}$.

Suppose $\partial c = C_{R, n}$ for some 2-chain $c$.

$$
\begin{align*}
  2\pi n = \int_{C_{R, n}} d\theta = \int_{\partial c} d\theta = \int_{c} d^2\theta = \int_c 0 = 0.
\end{align*}
$$

This is a contradiction, so there is no such 2-chain.

