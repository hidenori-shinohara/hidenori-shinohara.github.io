---
layout: post
title:  "Irreducible components(WIP)"
date:   2019-12-27
author: Hidenori
---

# Proposition
Let $X$ be a topological space.
1. If $Y$ is an irreducible subspace of $X$, then the closure $\overline{Y}$ of $Y$ in $X$ is irreducible.
1. TODO
1. TODO
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
TODO

## 3
TODO

## 4
TODO
