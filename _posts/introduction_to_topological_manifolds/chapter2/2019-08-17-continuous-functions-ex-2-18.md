---
layout: post
title:  "Some elementary continuous functions"
date:   2019-08-17
author: Hidenori
---

# Proposition
Let $X, Y$ be topological spaces.

1. Every constant map $f: X \rightarrow Y$ is continuous.
1. The identity map $\text{Id}_X: X \rightarrow X$ is continuous.
1. If $f: X \rightarrow Y$ is continuous, so is the restriction of $f$ to any open subset of $X$.

# Solution
## 1
Let $f: X \rightarrow Y$ be a constant map.
Let $y$ be the constant to which $f$ maps every element of $X$.
Let $V \subset Y$ be an open subset.

* If $y \in V$, then $f^{-1}(V) = X$, and $X$ is open in $X$.
* If $y \notin V$, then $f^{-1}(V) = \emptyset$, and $\emptyset$ is open in $X$.

Therefore, $f$ is continuous.

## 2
Let $f: X \rightarrow X$ be the identity map.
Let $U \subset X$ be an open subset.
Then $f^{-1}(U) = U$, so $f^{-1}(U)$ is open.
Therefore, $f$ is continuous.

## 3
Let $A$ be any subset of $X$.

Consider $f_A: A \rightarrow f(A)$.
Let $U \subset f(A)$ be an open subset.
Then $U = V \cap f(A)$ for some $V$ that is open in $Y$.

$f_A^{-1}(U) = f^{-1}(U) \cap A = f^{-1}(V \cap f(A)) \cap A = f^{-1}(V) \cap f^{-1}(f(A)) \cap A$.

* $f^{-1}(V)$ is open in $X$ because $f$ is continuous.
* $A \subset f^{-1}(f(A))$, so $f^{-1}(f(A)) \cap A = A$.

Therefore, $f_A^{-1}(U) = f^{-1}(V) \cap A$, so it is open in $A$.
Hence, $f_A$ is continuous.
