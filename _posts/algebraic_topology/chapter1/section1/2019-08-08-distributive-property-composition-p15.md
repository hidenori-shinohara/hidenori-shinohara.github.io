---
layout: post
title:  "Given a map $f: X \\rightarrow Y$ and a path $h: I \\rightarrow X$ from $x_0$ to $x_1$, show that $f_*\\beta_h = \\beta_{fh}f_*$."
date:   2019-08-08
author: Hidenori
---

# Proposition
Given a map $f: X \rightarrow Y$ and a path $h: I \rightarrow X$ from $x_0$ to $x_1$, show that $$f_*\beta_h = \beta_{fh}f_*$$.

# Solution

Let $[g] \in \pi_1(X, x_1)$ be given.
Then $g$ is a loop in $X$ based at $x_1$.

$$
\begin{align*}
  f_*\beta_h([g])
    &= f_*([h \cdot g \cdot \overline{h}]) \\
    &= [f \circ (h \cdot g \cdot \overline{h})]. \\
  \\
  \beta_{fh}f_*([g])
    &= \beta_{fh}([f \circ g]) \\
    &= [(f \circ h) \cdot (f \circ g) \cdot \overline{f \circ h}].
\end{align*}
$$

We claim that $f \circ (h \cdot g \cdot \overline{h})$ and $(f \circ h) \cdot (f \circ g) \cdot \overline{f \circ h}$ are the same loop.
Let $t \in [0, 1]$ be given.

$$
\begin{align*}
  (f \circ (h \cdot g \cdot \overline{h}))(t)
    &= f((h \cdot g \cdot \overline{h})(t)) \\
    &= \begin{cases}
      f(h(3t)) & (t \in [0, 1/3]) \\
      f(g(3t - 1)) & (t \in [1/3, 2/3]) \\
      f(\overline{h}(3t - 2)) & (t \in [2/3, 1]).
    \end{cases} \\ \\
  ((f \circ h) \cdot (f \circ g) \cdot (f \circ h))(t)
    &= \begin{cases}
      f(h(3t)) & (t \in [0, 1/3]) \\
      f(g(3t - 1)) & (t \in [1/3, 2/3]) \\
      \overline{(f \circ h)}(3t - 2) & (t \in [2/3, 1]).
    \end{cases}.
\end{align*}
$$

$\overline{(f \circ h)}(3t - 2) = (f \circ h)(1 - (3t - 2)) = (f \circ h)(3 - 3t) = f(h(3 - 3t)) = f(\overline{h}(3 t - 2))$.

Thus those two loops are identical, so $$f_*\beta_h = \beta_{fh}f_*$$.
