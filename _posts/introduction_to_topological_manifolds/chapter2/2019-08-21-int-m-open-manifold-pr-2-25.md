---
layout: post
title:  "If $M$ is an $n$-dimensional manifold with boundary, then $\\Int{M}$ is an open subset of $M$, which is itself an $n$-dimensional manifold without boundary."
date:   2019-08-21
author: Hidenori
---

# Proposition
If $M$ is an $n$-dimensional manifold with boundary, then $\Int{M}$ is an open subset of $M$, which is itself an $n$-dimensional manifold without boundary.

# Solution
The [manifold interior](https://en.wikipedia.org/wiki/Manifold#Boundary_and_interior) is defined differently from the topological interior.

Let $x \in \Int{M}$.
Then $x$ has a neighborhood $U$ that homeomorphic to an open subset $V$ of $\mathbb{R}^n$.
Then for any $y \in U$, $U$ is a neighborhood of $x$ that is homeomorphic to $V$.
Thus $U \subset \Int{M}$.
This implies that $\Int{M}$ is an open subset of $M$.

$\Int{M}$ is a subspace of $M$, so it is Hausdorff and second countable because $M$ is an $n$-dimensional manifold with boundary.
Let $x \in \Int{M}$.
Then there exists an open set $U \subset M$ that is homeomorphic to an open subset $V \subset \mathbb{R}^n$.
As shown above, $U \subset \Int{M}$.
Therefore, $x$ has a neighborhood in $\Int{M}$ that is homeomorphic to an open subset in $\mathbb{R}^n$.
Therefore, $\Int{M}$ is indeed an $n$-dimensional manifold without boundary.

