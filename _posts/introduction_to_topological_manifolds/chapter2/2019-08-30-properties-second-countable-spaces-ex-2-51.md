---
layout: post
title:  "Property of Second Countable Spaces"
date:   2019-08-30
author: Hidenori
---

# Proposition
Suppose $X$ is a second countable space.
Then $X$ contains a countable dense subset.

# Solution
Let $\mathcal{B}$ be a countable basis for $X$.
For each nonempty $B \in \mathcal{B}$, we will pick a point $x_B \in B$ arbitrarily.
We claim that $A = \\{ x_B \mid B \in \mathcal{B}, B \ne \emptyset \\}$ is a countable dense subset.

* $A$ is countable because the map $x_B \mapsto B$ is an injection from $A$ into $\mathcal{B}$.
* We will show that $A$ is dense.
  Let $x \in X$.
  If $x \in \overline{A}$, we are done.
  Suppose otherwise.
  Since $\overline{A}$ is the intersection of all closed subsets of $X$ containing $A$, this implies the existence of a closed set $C \subset X$ such that $x \notin C$ and $A \subset C$.
  Since $C$ is closed, $C^c$ is open.
  Moreover, $C^c$ is an open neighborhood of $x$.
  Since $C^c$ is an open set and $x \in C^c$, there must exist a basis element $B \in \mathcal{B}$ such that $x \in B \subset C^c$.
  Then $x_B \in C^c$.
  However, this is impossible because $x_B \in A \subset C$.
  Therefore, $x$ must be in $\overline{A}$, so $A$ is indeed dense.

Therefore, we showed the existence of a countable dense subset of $X$.
