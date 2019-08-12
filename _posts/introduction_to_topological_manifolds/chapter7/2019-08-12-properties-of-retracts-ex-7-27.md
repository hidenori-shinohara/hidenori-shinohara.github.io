---
layout: post
title:  "Properties of retracts"
date:   2019-08-12
author: Hidenori
---

# Proposition
Prove the following facts about retracts:

1. A retract of a connected space is connected.
1. A retract of a compact space is compact.
1. A retract of a retract is a retract; that is, if $A \subset B \subset X$, $A$ is a retract of $B$, and $B$ is a retract of $X$, then $A$ is a retract of $X$.

# Solution
## 1
Let $A$ be a retract of $X$.
Let $U$ be disjoint open sets in $A$ such that $U \cup V = A$.
Let $r: X \rightarrow A$ be a retraction.

* Then $r$ is continuous, so $r^{-1}(U)$ and $r^{-1}(V)$ are both open in $X$.
* $X = r^{-1}(A) = r^{-1}(U \cup V) = r^{-1}(U) \cup r^{-1}(V)$.
* There exists no $x \in X$ such that $r(x) \in U$ and $r(x) \in V$.
  Thus $r^{-1}(U)$ and $r^{-1}(V)$ are disjoint.

Since $X$ is connected, there exists no separation.
Therefore, either $r^{-1}(U)$ or $r^{-1}(V)$ must be empty.
Without loss of generality, assume that $r^{-1}(U)$ is empty.
Since $r$ is surjective, $U$ must be empty.

Therefore, $A$ has no separation since any pair of disjoint open sets whose union equals $A$ includes the empty set.
Thus $A$ is connected.

## 2
TODO

## 3
TODO
