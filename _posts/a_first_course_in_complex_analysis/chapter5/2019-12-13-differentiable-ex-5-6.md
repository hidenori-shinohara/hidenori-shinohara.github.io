---
layout: post
title:  "A derivative of a real function is not always continuous"
date:   2019-12-13
author: Hidenori
---

# Proposition
Show that the function $f: \mathbb{R} \rightarrow \mathbb{R}$ given by

$$
\begin{align*}
  f(x) &= \begin{cases}
    x^2\sin(1/x) & (x \ne 0), \\
    0 & (x = 0)
  \end{cases}
\end{align*}
$$

is differentiable in $\mathbb{R}$, yet $f'$ is not even continuous at 0.

# Solution
$f'(x) = 2x\sin(1/x) - \cos(1/x)$ when $x \ne 0$.

$$
\begin{align*}
  \lim_{h \rightarrow 0} \frac{h^2 \sin(1/h) - 0}{h - 0} = 1.
\end{align*}
$$

However, $\lim_{x \rightarrow 0} f'(x) \ne 1$, so $f'(x)$ is not continuous at $0$.
