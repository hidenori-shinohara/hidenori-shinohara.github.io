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

Corollary 2.5 states

> Let $M$ be a finitely generated $A$-module and let $a$ be an ideal of $A$ such that $aM = M$.
> Then there exists $x \equiv 1 \pmod a$ such that $xM = 0$.

Let $S = 1 + a$.
Since $aM = M$, we have $(S^{-1}a)(S^{-1}M) = S^{-1}M$.

* $S^{-1}a$ is an ideal of $S^{-1}A$ such that it is contained in the Jacobson radical of $S^{-1}A$ as shown above.
* $S^{-1}M$ is a finitely generated $S^{-1}A$-module.
    * Let $\\{ x_1, \cdots, x_n \\} \subset M$ be a set of generators of $M$ as an $A$-module.
      Then $\\{ \frac{x_1}{1}, \cdots, \frac{x_n}{1} \\}$ generates $S^{-1}M$ as an $S^{-1}A$-module.


By Nakayama's Lemma (Proposition 2.6, Atiyah), $S^{-1}M = 0$.
[As shown before](/2019/11/23/fraction-0-ex-3-1.html), this implies that there exists $1 + x \in S = 1 + a$ such that $(1 + x)M = 0$.
Clearly, $1 + x \equiv 1 \pmod a$.
