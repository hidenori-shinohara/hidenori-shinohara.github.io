---
layout: post
title:  "Special continuous functions"
date:   2019-09-05
author: Hidenori
---

# Proposition
Let $X, Y$, and $Z$ be topological spaces.

1. Every constant map $f: X \rightarrow Y$ is continuous.
1. The identity map $\Id_X: X \rightarrow X$ is continuous.
1. If $f: X \rightarrow Y$ is continuous, so is the restriction of $f$ to any open subset of $X$.

# Solution

## 1
Let $V \subset Y$ be an open subset.
Then $f^{-1}(V)$ is either the empty set or $X$ depending on $V$ contains the point to which $f$ maps every element of $X$.
in each case, $f^{-1}(V)$ is open in $X$.

## 2
For any open $U \subset X$, $\Id_X^{-1}(U) = U$, which is open in $X$.

## 3
Let $X'$ be a subset of $X$ and let $f'$ denote the restriction of $f$ to $X'$.

Let $V \subset Y$.
Then $f'^{-1}(V) = f^{-1}(V) \cap X'$.
Then $f^{-1}(V) \cap X'$ is open in $X'$ because $f^{-1}(V)$ is open in $X$.
