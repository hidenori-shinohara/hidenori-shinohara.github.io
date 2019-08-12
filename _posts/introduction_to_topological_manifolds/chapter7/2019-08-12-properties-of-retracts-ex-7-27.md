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
Let $A$ be a retract of $X$.
Let $K = \\{ U_{\alpha} \\}$ be an open cover of $A$.
Let $r: X \rightarrow A$ be a retraction.
Since $r$ is a retraction, $r^{-1}(U_{\alpha})$ is an open set for each $\alpha$.
Since $X = r^{-1}(A)$, $\\{ r^{-1}(U_{\alpha}) \\}$ is an open cover of $X$.
Since $X$ is compact, there exists $r^{-1}(U_{\alpha_1}), \cdots, r^{-1}(U_{\alpha_n})$ that cover $X$.

We claim that $U_{\alpha_1}, \cdots, U_{\alpha_n}$ covers $A$.
Let $a \in A$.
Then $a \in X$, so $a \in r^{-1}(U_{\alpha_k})$ for some $k \in \\{ 1, 2, \cdots, n \\}$.
Since $r$ is surjective, $r(r^{-1}(U_{\alpha_k}) = U_{\alpha_k}$.
Since $r \circ i_A$ is the identity map on $A$, $r(a) = a$.
Therefore, $a = r(a) \in r(r^{-1}(U_{\alpha_k})) = U_{\alpha_k}$.

We found a finite subcover of $K$, so $A$ is compact.

## 3
Let $A \subset B \subset X$ where $A$ is a retract of $B$, and $B$ is a retract of $X$.
Let $r_1, r_2$ denote retractions of $X$ onto $B$ and $B$ onto $A$, respectively.
Let $r = r_2 \circ r_1$.

* $r$ is continuous since it is a composition of two continuous functions.
* Let $a \in A$.
  $r(a) = r_2(r_1(a))$.
  $r_1(a) = a$ because $r_1$ is the identity map when restricted to $B$ and $a \in B$.
  $r_2(a) = a$ because $r_2$ is the identity map when restricted to $A$.
  Therefore, $r(a) = a$.

Therefore, $r$ is a retraction of $X$ onto $A$, so $A$ is a retract of $X$.
