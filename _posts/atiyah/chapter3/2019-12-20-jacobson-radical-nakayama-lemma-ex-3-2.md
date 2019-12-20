---
layout: post
title:  "The Jacobson radical and Nakayama's lemma(WIP)"
date:   2019-12-20
author: Hidenori
---

# Proposition
Let $a$ be an ideal of a ring $A$, and let $S = 1 + a$.
Show that $S^{-1}a$ is contained in the Jacobson radical of $S^{-1}A$.

Use this result and Nakayama's lemma to give a proof of (2.5)[Atiyah] which does not depend on determinants.

# Solution
* $0 \in a$, so $1 = 1 + 0 \in 1 + a = S$.
* For any $1 + x, 1 + y \in 1 + a, (1 + x)(1 + y) = 1 + (x + y + xy) \in 1 + a$.
Therefore, $S$ is multiplicatively closed, so it makes sense to discuss $S^{-1}a$ and $S^{-1}A$.

Let $\frac{x}{1 + y} \in S^{-1}a, \frac{z}{1 + w}$ be given where $x, y, w \in a$ and $z \in A$.

$$
\begin{align*}
  1 - \frac{x}{1 + y} \cdot \frac{z}{1 + w}
    &= \frac{1 + y + w + yw - xz}{(1 + y)(1 + w)}
\end{align*}
$$

Moreover, $x, y, w \in a$, so $y + w + yw - xz \in a$.
Therefore, $1 + y + w + yw - xz \in S$, so $1 - \frac{x}{1 + y} \cdot \frac{z}{1 + w}$ is a unit in $S^{-1}A$.
By Proposition 1.9[Atiyah], every element in $S^{-1}a$ is in the Jacobson radical of $S^{-1}A$.

TODO(Solve the second part.)
