---
layout: post
title:  "Laurent series for $\\frac{1}{\\sin^2(z)}$"
date:   2019-12-23
author: Hidenori
---

# Proposition
Find the terms $c_nz^n$ in the Laurent series for $\frac{1}{\sin^2(z)}$ centered at $z = 0$ for $-4 \leq n \leq 4$.

# Solution
Example 8.23 [A first course in complex analysis] has the Laurent series for $\frac{1}{\sin(z)}$.
[By simply squaring it](https://www.wolframalpha.com/input/?i=expand+%281%2Fz+%2B+z%2F6+%2B+7z%5E3+%2F+360+%2B+31z%5E5%2F15120%29%5E2), we obtain

$$
\begin{align*}
  c_i &= \begin{cases}
    1 & (i = -2) \\
    1/3 & (i = 0) \\
    1/15 & (i = 2) \\
    2/189 & (i = 4) \\
    0 & \text{(otherwise)}.
  \end{cases}
\end{align*}
$$
