---
layout: post
title:  "Tangent vector"
date:   2019-11-27
author: Hidenori
---

# Proposition
Let $c$ be a differentiable curve in $\mathbb{R}^n$, that is, a differentiable function $c:[0, 1] \rightarrow \mathbb{R}^n$.
Define the tangent vector $v$ of $c$ at $t$ as $$c_{\ast}((e_1)_t) = ((c^1)'(t), \cdots, (c^n)'(t))_{c(t)}$$.
If $f: \mathbb{R}^n \rightarrow \mathbb{R}^m$, show that the tangent vector to $f \circ c$ at $t$ is $f_{\ast}(v)$.

# Solution

$$
\begin{align*}
  c_{\ast}((e_1)_t)
    &= ((c^1)'(t), \cdots, (c^n)'(t))_{c(t)} \\
    &= (Dc^1(t), \cdots, Dc^n(t))_{c(t)} \\
      &= (Dc(t))_{c(t)} & \text{(Theorem 2-3-(3) [Spivak])}.
\end{align*}
$$

Therefore,

$$
\begin{align*}
  (f \circ c)_{\ast}((e_1)_t)
    &= (((f \circ c)^1)'(t), \cdots, ((f \circ c)^m)'(t))_{(f \circ c)(t)} \\
    &= (D(f \circ c)^1(t), \cdots, D(f \circ c)^m(t))_{(f \circ c)(t)} \\
    &= (D(f \circ c)(t))_{f(c(t))} & \text{(Theorem 2-3-(3) [Spivak])} \\
    &= (Df(c(t))Dc(t))_{f(c(t))} & \text{(Theorem 2-2[Spivak])} \\
    &= f_{\ast}((Dc(t))_{c(t)}) \\
    &= f_{\ast}(v).
\end{align*}
$$
