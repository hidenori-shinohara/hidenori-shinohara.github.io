---
layout: post
title:  "The set of all multiplicatively closed subsets without 0(WIP)"
date:   2019-12-24
author: Hidenori
---

# Proposition
Let $A$ be a ring $\ne 0$ and let $\Simga$ be the set of all multiplicatively closed subsets $S$ of $A$ such that $0 \notin S$.
Show that $\Sigma$ has maximal elements, and that $S \in \Sigma$ is maximal if and only if $A \setminus S$ is a minimal prime ideal of $A$.

# Solution
Let $S_1 \subset S_2 \subset \cdots$ be elements of $\Sigma$.
Let $S = \bigcup_{i \in \mathbb{N}} S_i$.
Then $S$ is multiplicatively closed and $0 \notin S$.
Therefore, $S \in \Sigma$ and $S$ is an upper bound of the chain.
By Zorn's Lemma, $\Sigma$ contains a maximal element.

TODO(Finish the second part)
