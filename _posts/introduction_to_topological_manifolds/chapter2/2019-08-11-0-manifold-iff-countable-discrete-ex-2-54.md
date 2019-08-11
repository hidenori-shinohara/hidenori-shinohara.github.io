---
layout: post
title:  "A topological space is a $0$-manifold if and only if it is a countable discrete space."
date:   2019-08-11
author: Hidenori
---

# Proposition
Show that a topological space is a $0$-manifold if and only if it is a countable discrete space.

# Solution
Suppose that $X$ is $0$-manifold.
Since it is a $0$-manifold, for each $x \in X$, there must exist a neighborhood $U$ that is homeomorphic to an open set in $\mathbb{R}^0$.
The only open sets in $\mathbb{R}^0$ are $\emptyset$ and $\\{ 0 \\}$.
Since a nonempty set cannot be mapped into the empty set, $U$ must be homeomorphic to $\\{ 0 \\}$.
If $U$ contains more than $1$ element, then any map from $U$ into $\\{ 0 \\}$ is not injective.
Thus $U$ must only contain $x$.

This shows that $\\{ x \\}$ is open for every $x \in X$, so $X$ has a discrete topology.

Let $\mathcal{B}$ be a countable basis of $X$.
Let $x \in x$ be given.
Then $\\{ x \\}$ is the union of elements of $\mathcal{B}$ by definition.
This implies that $\\{ x \\} \in \mathcal{B}$.

Since $\mathcal{B}$ contains all singletons and $\mathcal{B}$ is countable, there are at most countably many singletons.
In other words, $X$ must be countable.

Therefore, $X$ is a countable discrete space.

On the other hand, suppose that $X$ is a countable discrete space.

* $\\{ \\{ x \\} \mid x \in X \\}$ is a countable basis.
* $X$ is Hausdorff since any $x \ne y$ can be separated by $\\{ x \\}$ and $\\{ y \\}$.
* For every point $x \in X$, $\\{ x \\}$ is a neighborhood of $x$ that is locally homeomorphic to $\mathbb{R}^0$.

Thus $X$ is a $0$-manifold.
