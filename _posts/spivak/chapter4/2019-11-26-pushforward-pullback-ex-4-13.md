---
layout: post
title:  "Basic properties of push-forward and pullback"
date:   2019-11-26
author: Hidenori
---

# Proposition
1. If $f: \mathbb{R}^n \rightarrow \mathbb{R}^m$ and $g: \mathbb{R}^m \rightarrow \mathbb{R}^p$, show that $(g \circ f)_{\ast} = g_{\ast} \circ f_{\ast}$ and $(g \circ f)^{\ast} = f^{\ast} \circ g^{\ast}$.
1. If $f, g: \mathbb{R}^n \rightarrow \mathbb{R}$, show that $d(f \cdot g) = f \cdot dg + g \cdot df$.

# Solution

## 1
Let $k \in \mathbb{N}$ be given.
Let $\omega \in \mathcal{T}^k(\mathbb{R}^p)$ be given.

$$
\begin{align*}
  (g \circ f)^{\ast}(\omega)(v_1, \cdots, v_k)
    &= \omega((g \circ f)(v_1), \cdots, (g \circ f)(v_k)) \\
    &= \omega(g(f(v_1)), \cdots, g(f(v_k))) \\
    &= (g^{\ast} \omega)(f(v_1), \cdots, f(v_k)) \\
    &= (f^{\ast} (g^{\ast} \omega))(v_1, \cdots, v_k) \\
    &= ((f^{\ast} \circ g^{\ast})(\omega))(v_1, \cdots, v_k).
\end{align*}
$$

Therefore, $(g \circ f)^{\ast} = f^{\ast} \circ g^{\ast}$.

TODO

## 2
TODO
