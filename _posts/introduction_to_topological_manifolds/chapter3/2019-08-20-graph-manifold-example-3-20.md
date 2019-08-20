---
layout: post
title:  "Manifolds constructed from graphs"
date:   2019-08-20
author: Hidenori
---

# Proposition
Let $U \subset \mathbb{R}^n$ be an open subset.
Let $f = (f_1, \cdots, f_k): U \rightarrow \mathbb{R}^k$ be any continuous map.
Then $M = \\{ (x_1, \cdots, x_n, f_1(x), \cdots, f_k(x)) \mid x = (x_1, \cdots, x_n) \in U \\}$ is an $n$-manifold in $\mathbb{R}^{n + k}$.

# Solution
Let $F: U \rightarrow M$ denote the mapping $(x_1, \cdots, x_n) \mapsto (x_1, \cdots, x_n, f_1(x), \cdots, f_k(x))$.
We claim that $F$ is a homeomorphism from $U$ into $M$.

* Continuous?
    * Each component function is continuous, so $F$ is continuous.
* Injective?
    * If $f(x_1, \cdots, x_n) = f(y_1, \cdots, y_n)$, then $(x_1, \cdots, x_n) = (y_1, \cdots, y_n)$.
* Surjective?
    * $M = F(U)$, so $F$ is surjective.
* Continuous inverse?
    * The inverse is $m \mapsto (\pi_1(m), \pi_2(m), \cdots, \pi_n(m))$ where each $\pi_i$ is the projection of the $i$th coordinate.
      Since each component function is continuous, the inverse is continuous.

Therefore, $F$ is indeed a homeomorphism.

Since $M$ is a subspace of $\mathbb{R}^{n + k}$, it is Hausdorff and second countable.
Let $x \in M$.
Then $M$ is a neighborhood of $x$ that is homeomorphic to $U$, an open subset of $\mathbb{R}^n$.
Therefore, $M$ is locally Euclidean.

Hence, $M$ is an $n$-manifold.
