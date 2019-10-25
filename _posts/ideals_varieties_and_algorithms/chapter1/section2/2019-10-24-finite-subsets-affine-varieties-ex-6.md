---
layout: post
title:  "All finite subsets of $k^n$ are affine varieties"
date:   2019-10-24
author: Hidenori
---

# Proposition
All finite subsets of $k^n$ are affine varieties.

1. Prove that a single point $(a_1, \cdots, a_n) \in k^n$ is an affine variety.
1. Prove that every finite subset of $k^n$ is an affine variety.

# Solution

## 1
Let $(a_1, \cdots, a_n) \in k^n$ be given.
Let $S = V(x_1 - a_1, \cdots, x_n - a_n)$.
Then $S = \{ (a_1, \cdots, a_n) \}$.
Thus every singleton is an affine variety.

## 2
Lemma 2 (P.11, *Ideals, Varieties and Algorithms*) states that the union of two affine varieties is an affine variety.

By mathematical induction, for any $m \in \mathbb{N}$, a finite subset of $k^n$ with $m$ points is an affine variety.
