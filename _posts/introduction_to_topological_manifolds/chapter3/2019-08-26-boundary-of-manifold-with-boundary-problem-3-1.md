---
layout: post
title:  "The boundary of a manifold with boundary is a manifold without boundary"
date:   2019-08-26
author: Hidenori
---

# Proposition
Suppose $M$ is an $n$-dimensional manifold with boundary.
Show that $\partial M$ is an $(n - 1)$-manifold (without boundary) when endowed with the subspace topology.
You may use without proof the fact that $\Int{M}$ and $\partial M$ are disjoint.

# Solution
Let $M$ be an $n$-dimensional manifold with boundary.
We will show that $\partial M$ is an $(n - 1)$-manifold.

Since $M$ is Hausdorff and second countable, $\partial M$ is Hausdorff and second countable.
We will show that $\partial M$ is locally Euclidean.

Let $x \in \partial M$.
Since $x \in \partial M \subset M$, there exists a chart $(U, \phi)$ for $x$.
Since $x$ is a boundary point of $M$, $(U, \phi)$ is a boundary chart and $\phi(x) \in \partial \mathbb{H}^n$.

By the definition of a chart, $\phi(U)$ must be open in $\mathbb{H}^n$.
Thus $\phi(U) \cap \partial \mathbb{H}^n$ is open in $\partial \mathbb{H}^n$.

Let $$\phi' = \phi \mid _{U \cap \partial M}$$.
We claim that $\phi'$ is a homeomorphism between $U \cap \partial M$ and $\phi(U) \cap \partial \mathbb{H}^n$.

* Claim 1: $\phi'(U \cap \partial M) = \phi(U) \cap \partial \mathbb{H}^n$.
    * Let $x \in U \cap \partial M$.
      Then $\phi'(x) = \phi(x) \in \partial \mathbb{H}^n$ because $x$ is a boundary point of $M$.
      Thus $\phi'(x) \in \phi(U) \cap \partial \mathbb{H}^n$.
      Therefore, $\phi'(U \cap \partial M) \subset \phi(U) \cap \partial \mathbb{H}^n$.
    * Let $y \in \phi(U) \cap \partial \mathbb{H}^n$.
      Then $y = \phi(x)$ for some $x \in U$.
      Then $\phi(x) \in \partial \mathbb{H}^n$.
      This implies that $x$ is a boundary point of $M$, so $x \in U \cap \partial M$.
      Therefore, $y = \phi(x) = \phi'(x) \in \phi'(U \cap \partial M)$.
* Claim 2: $\phi'$ is injective.
    * This is true because $\phi$ is injective.
* Claim 3: $\phi'$ is surjective.
    * We showed this in Claim 1.
* Claim 4: $\phi'$ is continuous.
    * A restriction of a continuous function is continuous.
      Since $\phi$ is continuous, $\phi'$ is continuous.
* Claim 5: $\phi'$ is open.
    * By the definition of a subspace topology, every open subset in $U \cap \partial M$ is the intersection of an open subset in $U$ with $\partial M$.
      Let $V \cap \partial M \subset U \cap \partial M$ be an open subset in $U \cap \partial M$ where $V$ is an open subset of $U$.

      $$
      \begin{align*}
       \phi'(V \cap \partial M)
         &= \phi'(V \cap U \cap \partial M) \\
         &= \phi(V \cap U \cap \partial M) \\
         &= \phi(V) \cap \phi(U \cap \partial M) & \text{(because $\phi$ is bijective)} \\
         &= \phi(V) \cap \phi'(U \cap \partial M) \\
         &= \phi(V) \cap \phi(U) \cap \partial \mathbb{H}^n \\
         &= \phi(V) \cap \partial \mathbb{H}^n.
      \end{align*}
      $$

      Since $\phi$ is an open map, $\phi(V)$ is open in $\mathbb{H}^n$.
      Therefore, $\phi(V) \cap \partial \mathbb{H}^n$ is open in $\partial \mathbb{H}^n$.
      Thus $\phi'$ is an open map.

Therefore, $\phi'$ is indeed a homeomorphism.

[We have shown that $\mathbb{R}^{n - 1}$ is homeomorphic to $\partial \mathbb{H}^n$]({% post_url introduction_to_topological_manifolds/chapter3/2019-08-26-homeomorphism-line-line-in-space %})

Therefore, $U \cap \partial M$ is homeomorphic to an open subset in $\mathbb{R}^{n - 1}$, so $\partial{M}$ is locally Euclidean.

Hence, $\partial{M}$ is an $(n - 1)$-manifold.


