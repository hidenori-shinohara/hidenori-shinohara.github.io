---
layout: post
title:  "Cauchy integral formula"
date:   2019-11-26
author: Hidenori
---

# Proposition
compute $\int_{\gamma} \frac{dz}{z}$ where $\gamma$ is the unit circle, oriented counterclockwise.
More generally, show that for any $w \in \mathbb{C}$ and $r > 0$,

$$
\begin{align*}
  \int_{C[w, r]} \frac{dz}{z - w} = 2\pi i.
\end{align*}
$$

# Solution
It suffices to prove the second statement.
Let $w \in \mathbb{C}$ and $r > 0$ be given.
Let $f(z) = 1$.
Then $f(z)$ is holomorphic on $\mathbb{C}$, which is an open set containing $\overline{D}[w, r]$.
By Theorem 4.24, $f(w) = \frac{1}{2\pi i}\int_{C[w, r]}\frac{f(z)}{z - w}dz$.
This implies $\int_{C[w, r]} \frac{dz}{z - w} = 2\pi i$.
