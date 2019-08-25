---
layout: post
title:  "Properties of Saturated Sets"
date:   2019-08-25
author: Hidenori
---

# Proposition
Let $q: X \rightarrow Y$ be any map.
For a subset $U \subset X$, show that the following are equivalent:

1. $U$ is saturated.
1. $U = q^{-1}(q(U))$.
1. $U$ is a union of fibers.
1. If $x \in U$, then every point $x' \in X$ such that $q(x) = q(x')$ is also in $U$.

# Solution

## $1 \implies 2$

* $U \subset q^{-1}(q(U))$?
    * For any $x \in U$, $q(x) \in q(U)$, so $x \in q^{-1}(\\{ q(x) \\}) \subset q^{-1}(q(U))$.
* $q^{-1}(q(U)) \subset U$?
    * Since $U$ is saturated, there exists a subset $V \subset Y$ such that $U = q^{-1}(V)$.
      Then $q(U) = q(q^{-1}(V)) \subset V$.
      Therefore, $q^{-1}(q(U)) \subset q^{-1}(V) = U$.

Therefore, $U = q^{-1}(q(U))$.

## $2 \implies 3$

$$
\begin{align*}
  U &= q^{-1}(q(U)) \\
    &= q^{-1}(\bigcup_{y \in q(U)} \{ y \}) \\
    &= \bigcup_{y \in q(U)} q^{-1}(\{ y \}).
\end{align*}
$$

Thus $U$ is indeed a union of fibers.

## $3 \implies 4$

Suppose $U$ is a union of fibers.
Then there exists $V \subset Y$ such that $U = \bigcup_{y \in V} q^{-1}(y)$.

Let $x \in U$.
Then $x \in q^{-1}(y)$ for some $y \in V$.
Let $x' \in X$ such that $q(x) = q(x')$.
Then $q(x') = y$, so $x' \in q^{-1}(u) \subset U$.

## $4 \implies 1$
We will show that $U = q^{-1}(q(U))$.
By the property of the inverse image, we know that $U \subset q^{-1}(q(U))$.
Let $x \in q^{-1}(q(U))$.
Then $q(x) \in q(U)$.
Therefore, there exists a point $x' \in U$ such that $q(x) = q(x')$, so $x \in U$.
Hence, $U = q^{-1}(q(U))$, so $U$ is saturated.
