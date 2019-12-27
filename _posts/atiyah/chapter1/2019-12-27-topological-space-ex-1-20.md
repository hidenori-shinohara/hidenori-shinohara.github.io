---
layout: post
title:  "Irreducible components(WIP)"
date:   2019-12-27
author: Hidenori
---

# Proposition
Let $X$ be a topological space.
1. If $Y$ is an irreducible subspace of $X$, then the closure $\overline{Y}$ of $Y$ in $X$ is irreducible.
1. Every irreducible subspace of $X$ is contained in a maximal irreducible subspace.
1. The maximal irreducible subspaces of $X$ are closed and cover $X$.
   What are the irreducible components of a Hausdorff space?
1. TODO

# Solution
## 1
* Since $Y$ is nonempty, $\overline{Y}$ is nonempty.
* Let $U, V$ be nonempty open subsets of $\overline{Y}$.
  Then $U \cap Y$ and $V \cap Y$ are open subsets of $Y$.
  Suppose $U \cap Y = \emptyset$.
  Then $\overline{Y} \setminus U$ is a closed set containing $Y$.
  This is impossible because $\overline{Y}$ is the smallest closed set containing $Y$.
  Thus $U \cap Y \ne \emptyset$.
  Similarly, $V \cap Y \ne \emptyset$.
  Thus $(U \cap Y) \cap (V \cap Y)$ is nonempty by the irreducibility of $Y$.
  Therefore, $U \cap V \ne \emptyset$.

Therefore, $\overline{Y}$ is irreducible.

## 2
Let $A$ be an irreducible subspace of $X$.
Let $\Sigma$ be the set of all irreducible subspaces of $X$ containing $A$.
Let $Y_1 \subset Y_2 \subset \cdots$ be a chain in $\Sigma$.
Let $Y = \bigcup Y_i$.
We claim that $Y \in \Sigma$.
Let $U, V$ be nonempty open subsets of $Y$.
Let $x \in U, y \in V$.
Then $x \in Y_i$ and $y \in Y_j$ for some $i, j$.
Then $x, y \in Y_k$ where $k = \max(i, j)$.
Then $U \cap Y_k \ne \emptyset$ and $V \cap Y_k \ne \emptyset$.
Since $U \cap Y_k$ and $V \cap Y_k$ are both open in $Y_k$ and $Y_k$ is irreducible, $(U \cap Y_k) \cap (V \cap Y_k) \ne \emptyset$.
Thus $U \cap V \ne \emptyset$.

By Zorn's Lemma, $\Sigma$ contains a maximal element.
In other words, there exists a maximal irreducible subspace of $A$.

## 3
Let $Y$ be a maximal irreducible subspace of $X$.
By 1, $\overline{Y}$ is irreducible.
Since $Y$ is maximal, $Y = \overline{Y}$, so $Y$ is closed.

Every singleton $\\{ x \\} \subset X$ is clearly irreducible.
By 2, every singleton is contained in a maximal irreducible subspace.
Thus the maximal irreducible subspaces cover $X$.

The singletons are the irreducible components of a Hausdorff space.

## 4
TODO
