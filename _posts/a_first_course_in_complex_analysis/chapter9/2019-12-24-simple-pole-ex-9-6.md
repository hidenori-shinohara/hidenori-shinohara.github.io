---
layout: post
title:  "Simple pole and a product of functions"
date:   2019-12-24
author: Hidenori
---

# Proposition
Suppose $f$ has a simple pole at $z_0$ and $g$ is holomorphic at $z_0$.
Prove that

$$
\begin{align*}
  \Res_{z = z_0}(f(z)g(z)) = g(z_0)\Res_{z = z_0}(f(z)).
\end{align*}
$$

# Solution
By Corollary 9.6[A first course in complex analysis], $f(z) = \tilde{f}(z)/(z - z_0)$ for some $\tilde{f}$ that is holomorphic in an open disk around $z_0$.

Then $fg = g\tilde{f}/(z - z_0)$ where $g\tilde{f}$ is holomorphic at $z_0$.
Thus $fg$ has a simple pole at $z_0$.
By Proposition 9.11(b)[A first course in complex analysis],

$$
\begin{align*}
  \Res_{z = z_0}(fg)
    &= \lim_{z \rightarrow z_0} (z - z_0)fg \\
    &= \lim_{z \rightarrow z_0} g\tilde{f} \\
    &= g(z_0)\tilde{f}(z_0) \\
    &= g(z_0)\lim_{z \rightarrow z_0}(z - z_0)f(z) \\
    &= g(z_0)\Res_{z = z_0}(f(z)).
\end{align*}
$$

