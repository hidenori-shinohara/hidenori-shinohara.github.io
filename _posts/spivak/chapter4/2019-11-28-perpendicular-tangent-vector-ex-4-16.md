---
layout: post
title:  "Perpendicular tangent vector"
date:   2019-11-28
author: Hidenori
---

# Proposition
Let $c:[0,1] \rightarrow \mathbb{R}^n$ be a curve such that $\abs{c(t)} = 1$ for all $t$.
Show that $c(t)_{c(t)}$ and the tangent vector to $c$ at $t$ are perpendicular.

# Solution

$$
\begin{align*}
  \ev{(c^1(t), \cdots, c^n(t))_{c(t)}, ((c^1)'(t), \cdots, (c^n)'(t))_{c(t)}}
    &= \ev{(c^1(t), \cdots, c^n(t)), ((c^1)'(t), \cdots, (c^n)'(t))} \\
    &= c^1(t)(c^1)'(t) + \cdots + c^n(t)(c^n)'(t) \\
    &= D(c^1)^2(t) + \cdots + D(c^n)^2(t) \\
    &= D((c^1)^2 + \cdots + (c^n)^2)(t) \\
    &= 0.
\end{align*}
$$
