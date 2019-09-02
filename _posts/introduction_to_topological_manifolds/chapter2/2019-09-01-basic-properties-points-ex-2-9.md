---
layout: post
title:  "Basic properties of the interior, exterior, and boundary of a topological space"
date:   2019-09-01
author: Hidenori
---

# Proposition
Let $X$ be a topological space and let $A \subset X$ be any subset.

1. A point is in $\Int{A}$ if and only if it has a neighborhood contained in $A$.

# Solution
## 1
Let $x \in X$.

Suppose $x \in \Int{A}$.
Since $\Int{A}$ is the union of all open subsets of $X$ that are contained in $A$, there must exist an open $U \subset X$ such that $x \in U \subset A$.
Then $U$ is a neighborhood of $x$ contained in $A$.

On the other hand, suppose that $x$ has a neighborhood contained in $A$.
Let $U$ denote such a neighborhood.
Then $U$ is an open subset of $X$ contained in $A$, so $U \subset \Int{A}$.
Therefore, $x \in \Int{A}$.


