---
layout: post
title:  "Open and closed subspaces"
date:   2019-08-27
author: Hidenori
---

# Proposition
Suppose $S$ is a subspace of the topological space $X$.

1. If $U \subset S \subset X$, $U$ is open in $S$, and $S$ is open in $X$, then $U$ is open in $X$.
   The same is true with "closed" in place of "open."
1. If $U$ is a subset of $S$ that is either open or closed in $X$, then it is also open or closed in $S$, respectively.

# Solution

## 1
If $U$ is open in $S$, then $U = S \cap V$ for some $V \subset X$ that is open in $X$ by the definition of a subspace topology.
Since the intersection of two open sets is open, $U = S \cap V$ is open in $X$.

Suppose that $C$ is closed in $S$ and $S$ is closed in $X$.
Then $S \setminus C$ is open in $S$.
Therefore, $S \setminus C = S \cap U$ for some set $U \subset X$ that is open in $X$.
Then $C = S \setminus (S \setminus C) = S \setminus (S \cap U) = S \setminus U = S \cap (X \setminus U)$.
Then $S$ is a closed subset of $X$ and $X \setminus U$ is closed in $X$.
Since the intersection of closed subsets is closed, $C = S \cap (X \setminus U)$ is closed in $X$.

## 2
Let $U \subset S$.
Suppose $U$ is open in $X$.
Then $U = S \cap U$, so $U$ is open in $S$.

Let $C \subset S$.
Suppose $C$ is closed in $X$.
Then $X \setminus C$ is open in $X$.
Thus $S \cap (X \setminus C)$ is open in $S$.
$S \cap (X \setminus C) = S \setminus C$ because $S \subset X$.
Then $S \setminus C$ is open in $S$.
Thus $C$ is closed in $S$.

