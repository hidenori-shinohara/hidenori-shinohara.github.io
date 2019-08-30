---
layout: post
title:  "Second countability and open covers"
date:   2019-08-30
author: Hidenori
---

# Proposition
Let $X$ be a topological space and let $\mathscr{U}$ be an open cover of $X$.

1. Suppose we are given a basis for each $U \in \mathscr{U}$ (when considered as a topological space in its own right).
   Show that the union of all those bases is a basis for $X$.
1. Show that if $\mathscr{U}$ is countable and each $U \in \mathscr{U}$ is second countable, then $X$ is second countable.

# Solution
## 1
For each $U \in \mathscr{U}$, let $\mathcal{B}_U$ denote a basis for $U$.
Let $$\mathcal{B} = \bigcup_{U \in \mathscr{U}} \mathcal{B}_U$$.
We will show that $\mathcal{B}$ is a basis for $X$.

* Every element in $\mathcal{B}$ is an open subset of some $U \in \mathscr{U}$.
  $\mathscr{U}$ is a collection of open subsets of $X$.
  Thus each element in $\mathcal{B}$ is an open subset of open subset of $X$.
  [We have shown that this implies that each element in $\mathcal{B}$ is open in $X$]({% post_url /introduction_to_topological_manifolds/chapter3/2019-08-27-subspace-open-closed-ex-3-6 %})
* Let $V \subset X$ be open and $x \in V$.
  Then $x \in U$ for some $U \in \mathscr{U}$.
  Then $x \in U \cap V$.
  Since $U \cap V$ is an open subset of $U$, $x \in B \subset U \cap V$ for some $B \in \mathcal{B}_U$.
  Moreover, such a $B$ is in $\mathcal{B}$.

Therefore, $\mathcal{B}$ is a basis for $X$.
(See Lemma 13.2 of Munkres)

## 2
For each $U \in \mathscr{U}$, let $\mathcal{B}_U$ denote a countable basis.
The existence of such a basis is guaranteed because each $U \in \mathscr{U}$ is second countable.
As shown above, the union of $\mathcal{B}_U$'s forms a basis for $X$.
Since $\mathscr{U}$ is countable, it is the countable union of countable sets, so it is countable.
