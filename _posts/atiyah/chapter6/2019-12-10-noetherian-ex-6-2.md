---
layout: post
title:  "If every non-empty set of finitely generated submodules of $M$ has a maximal element, then $M$ is Noetherian"
date:   2019-12-10
author: Hidenori
---

# Proposition
Let $M$ be an $A$-module.
If every non-empty set of finitely generated submodules of $M$ has a maximal element, then $M$ is Noetherian.

# Solution
By Proposition 6.2[Atiyah], it suffices to show that every submodule of $M$ is finitely generated.

Let $N$ be a submodule of $M$.
If $N = \\{ 0 \\}$, then we are done.
Suppose otherwise.
Let $x_1 \in N \setminus \\{ 0 \\}$.
If $N = \\{ x_1 \\}$, then we are done.

Having picked $x_1, \cdots, x_n$ for some $n \in \mathbb{N}$, we pick $x_{n + 1}$ to be an element in $N \setminus \ev{x_1, \cdots, x_n}$ if possible.

Then $S = \\{ \ev{x_1}, \ev{x_1, x_2}, \cdots \\}$ is a (possibly infinite) nonempty set of finitely generated submodules of $M$.
We are given that $S$ must have a maximal element $\ev{x_1, \cdots, x_k}$ for some $k$.
The obvious inclusion relation $\ev{x_1} \subsetneq \ev{x_1, x_2}, \cdots$ implies that $S$ must be finite because otherwise $\ev{x_1, \cdots, x_k} \subsetneq \ev{x_1, \cdots, x_{k + 1}}$ which is a contradiction. 
Therefore, $N = \ev{x_1, \cdots, x_k}$, so $N$ is finitely generated.

By Proposition 6.2[Aityah], $M$ is Noetherian.

