---
layout: post
title:  "Basic properties of a manifold(WIP)"
date:   2019-12-21
author: Hidenori
---

# Proposition
1. Let $A \subset \mathbb{R}^n$ be an open set such that boundary $A$ is an $(n - 1)$-dimensional manifold.
   Show that $N = A \cup \text{boundary} A$ is an $n$-dimensional manifold-with-boundary.
1. Prove a similar assertion for an open subset of an $n$-dimensional manifold.

# Solution
## 1
Let $x \in N$.

* Case 1: $x$ is an interior point of $N$.
    * Let $U$ be a neighborhood of $x$ contained in $N$.
      Then $\Id_U$ is a diffeomorphism from $U$ to $U$.
      Thus $x$ satisfies the condition (M) in [Spivak].
* Case 2: $x$ is a boundary point of $N$.

Then $x$ is a boundary point of $A$.
* For every open neighborhood $U$ of $x$, $U \cap A^c \supset U \cap N^c \ne \emptyset$.
* Let $U$ be an open neighborhood of $x$.
  Then $U \cap N \ne \emptyset$.
  Let $y \in U \cap N$.
  If $y \in A$, then $U \cap A \ne \emptyset$.
  If $y \notin A$, then $y \in \bd(A)$, so $U \cap A \ne \emptyset$.

Therefore, $x$ is part of the $(n - 1)$-dimensional manifold.

TODO (Finish this proof)

## 2
TODO (Finish this)
