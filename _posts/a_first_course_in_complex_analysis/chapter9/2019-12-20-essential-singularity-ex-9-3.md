---
layout: post
title:  "If $f$ has an essential singularity at $z_0$, then so does $1/f$"
date:   2019-12-20
author: Hidenori
---

# Proposition
Show that if $f$ has an essential singularity at $z_0$ then $\frac{1}{f}$ also has an essential singularity at $z_0$.

# Solution

Suppose $1/f$ does not have an essential singularity at $z_0$.
Since $f$ has an isolated singularity at $z_0$, $1/f$ has an isolated singularity at $z_0$.
By Proposition 9.5[a first course in complex analysis], $\lim_{z \rightarrow z_0} (z - z_0)^nf(z) \ne 0$ for any $n \in \mathbb{N}$.
Moreover, this is a necessary and sufficient condition to having an essential singularity.
Thus if $1/f$ does not have an essential singularity at $z_0$, then $\lim_{z \rightarrow z_0} (z - z_0)^n/f(z) = 0$ for some $n \in \mathbb{N}$.

Let $n \in \mathbb{N}$ be given.
For any $r > 0$, there exists $z'$ in the punctured disk $D[z_0, r] \setminus \\{ z_0 \\}$ such that $\abs{0 - f(z)} < r^n$ by [Casorati-Weierstrass](https://en.wikipedia.org/wiki/Casorati–Weierstrass_theorem).
This implies that $\lim_{z \rightarrow z_0} (z - z_0)^n/f(z) \ne 0$.
Therefore, $1/f$ has an essential singularity at $z_0$.
