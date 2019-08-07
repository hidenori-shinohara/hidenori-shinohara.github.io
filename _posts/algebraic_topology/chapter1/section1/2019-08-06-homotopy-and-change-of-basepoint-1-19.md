---
layout: post
title:  "Connection between homotopies and change-of-basepoint map"
date:   2019-08-06
author: Hidenori
---

# Proposition
Let $\phi_t: X \rightarrow Y$ is a homotopy and $h$ is the path $\phi_t(x_0)$ formed by the images of a basepoint $x_0 \in X$.
Then $$\phi_{0*} = \beta_h \phi_{1*}$$.

# Solution

Let $[f] \in \pi_1(X, x_0)$.
We claim that $$\phi_{0*}([f]) = \beta_h(\phi_{1*}([f])$$.

Let $F(x, t) = \phi_t(x)$ be the associated map of $\phi_t$'s.
Then $F$ is continuous since $\phi_t$ is a homotopy.

$h$ is defined to be $h(t) = \phi_t(x_0)$.
Define $H(s, t) = h(ts)$.
Then $H$ maps $I \times I \rightarrow Y$.
Then $H$ is a composition of $F$ and $(x, t) \mapsto (x_0, t)$.
The latter is a continuous function because each coordinate function is continuous, so $H$ is continuous.

Consider $G: I \times I \rightarrow Y$ such that

$$
\begin{align*}
  G(s, t)
    &= \begin{cases}
      H(3s, t) & (s \in [0, 1/3]) \\
      F(f(3s - 1), t) & (s \in [1/3, 2/3]) \\
      H(3 - 3s, t) & (s \in [2/3, 1]).
    \end{cases}
\end{align*}
$$

This is well-defined because:

* $H(3(1/3), t) = H(1, t) = h(t) = \phi_t(x_0) = \phi_t(f(0)) = F(f(0), t) = F(f(3(1/3) - 1), t)$.
* $F(f(3(2/3) - 1), t) = F(f(1), t) = F(x_0, t) = \phi_t(x_0) = h(t) = H(1, t) = H(3 - 3(2/3), t)$.

Moreover, $G$ is continuous in each $[0, 1/3], [1/3, 2/3]$, and $[2/3, 1]$ since each $H, F, f$ are continuous.
By the [pasting lemma](https://en.wikipedia.org/wiki/Pasting_lemma), $G$ is continuous.

We claim that $g_t(s) = G(s, t)$ is a homotopy from $\phi_0 \circ f$ to $h \cdot (\phi_1 \circ f) \cdot \overline{h}$.

* $g_0(s) = G(s, 0)$ is homotopic to $\phi_0 \circ f$.
* $g_1(s) = G(s, 1)$ is homotopic to $h \cdot (\phi_1 \circ f) \cdot \overline{h}$.
* $g_t(0) = G(0, t) = H(0, t) = h(0) = \phi_0(x_0)$.
* $g_t(1) = G(1, t) = H(3 - 3, t) = h(0) = \phi_0(x_0)$.

Therefore, $G$ is indeed a homotopy, so $$[\phi_0 \circ f] = [h \cdot (\phi_1 \circ f) \cdot \overline{h}] = \beta_{h*}([\phi_1 \circ f])$$.
Thus $$\phi_{0*}([f]) = \beta_{h*}(\phi_{1*}([f])) = (\beta_{h*} \circ \phi_{1*})([f])$$.
