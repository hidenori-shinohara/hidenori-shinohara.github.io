---
layout: post
title:  "Basic properties of manifolds(WIP)"
date:   2019-12-10
author: Hidenori
---

# Proposition
1. if $M$ is a $k$-dimensional manifold in $\mathbb{R}^n$ and $k < n$, show that $M$ has measure 0.
1. If $M$ is a closed $n$-dimensional manifold-with-boundary in $\mathbb{R}^n$, show that the boundary of $M$ is $\partial M$.
Give a counterexample if $M$ is not closed.
1. If $M$ is a compact $n$-dimensional manifold-with-boundary in $\mathbb{R}^n$, show that $M$ is Jordan-measurable.

# Solution

## 1
Let $x \in M$ be given and let $h: U \rightarrow V$ be the diffeomorphism.
If $U$ is not bounded, take the intersection of $U$ and an open ball and update $V$ appropriately.
Similarly, we can assume $V$ is bounded.

Let $\epsilon > 0$ be given.
Let $V_{\epsilon} = V \cap (\mathbb{R}^k \times (-\epsilon, \epsilon) \times \cdots \times (-\epsilon, \epsilon))$.
Then $V_{\epsilon}$ is a subset of $V$ and $V_{\epsilon} \cap (\mathbb{R}^k \times \\{ 0 \\}) = V \cap (\mathbb{R}^k \times \\{ 0 \\})$.

Let $U_{\epsilon} = h^{-1}(V_{\epsilon})$.
We claim that $U_{\epsilon} \cap M = U \cap M$.
Since $V_{\epsilon} \subset V$, $U_{\epsilon} \subset U$, so $U_{\epsilon} \cap M \subset U \cap M$.
Let $y \in U \cap M$.
Then $h(y) \in V \cap (\mathbb{R}^k \times \\{ 0 \\}) = V_{\epsilon} \cap (\mathbb{R}^k \times \\{ 0 \\}) \subset V_{\epsilon}$.
Then $y \in h^{-1}(V_{\epsilon}) = U_{\epsilon}$.
Therefore, $U_{\epsilon} \cap M = U \cap M$.

Hence, $h$ is a diffeomorphism from an open set $U_{\epsilon}$ to an open set $V_{\epsilon}$ such that $h(U_{\epsilon} \cap M) = V_{\epsilon} \cap (\mathbb{R}^k \times \\{ 0 \\})$.
By Theorem 3-13, we can find an $\epsilon > 0$ that makes the area of $U_{\epsilon}$ arbitrarily small while covering $U \cap M$.

The argument above works for any $x \in M$, and for each $x$, we obtain an open set $U$ containing $x$.
Since $M \subset \mathbb{R}^n$, there exists a countable open cover of $M$ formed by such $U$'s.
Let $x_1, \cdots$ and $U_1, \cdots$ denote them.
Let $\delta > 0$ be given.
Then using the argument above, find $U_{\epsilon_i}$ such that

* $U_{\epsilon_i}$ is open and $U_{\epsilon_i} \cap M = U_i \cap M$.
* $h_i\vert_{U_{\epsilon}}$ is a diffeomorphism.
* The volume of $U_{\epsilon_i}$ is less than $\delta / 2^i$.

Then $U_{\epsilon_1}, \cdots$ cover $M$ and the total area is less than $\delta$, an arbitrarily chosen positive number.
Therefore, $M$ has measure 0.

## 2

Let $x \in \bd M$.
Then $x \in M$ because $M$ is closed.
Suppose $x \notin \partial M$.
By Theorem 5-2[Spivak],  there exists an open set $U$ around $x$ and an open set $W$ in $\mathbb{R}^k$ such that 1-1 differentiable function $f: W \rightarrow U$ such that

* $f(W) = M \cap U$,
* $f^{-1}: M \cap U \rightarrow W$ is continuous.

This implies that $M \cap U$ is an open subset of $\mathbb{R}^n$.
However, there cannot be an open neighborhood of $x$ that is contained in $M$ because $x$ is a boundary point.
Therefore, $x \in \partial M$.

Let $x \in \partial M$.
We will show that $x \in \bd M$.
TODO(Finish this!)



Let $M = [0, 1)$.
Then $M$ is a 1-dimensional manifold-with-boundary and its point-set-topology-boundary is $\\{ 0, 1 \\}$.
However, the boundary of $M$ (as a manifold) is $\\{ 0 \\}$.

## 3
TODO
