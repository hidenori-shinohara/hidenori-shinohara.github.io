---
layout: post
title:  "The set of all multiplicatively closed subsets without 0"
date:   2019-12-24
author: Hidenori
---

# Proposition
Let $A$ be a ring $\ne 0$ and let $\Sigma$ be the set of all multiplicatively closed subsets $S$ of $A$ such that $0 \notin S$.
Show that $\Sigma$ has maximal elements, and that $S \in \Sigma$ is maximal if and only if $A \setminus S$ is a minimal prime ideal of $A$.

# Solution
Let $S_1 \subset S_2 \subset \cdots$ be elements of $\Sigma$.
Let $S = \bigcup_{i \in \mathbb{N}} S_i$.
Then $S$ is multiplicatively closed and $0 \notin S$.
Therefore, $S \in \Sigma$ and $S$ is an upper bound of the chain.
By Zorn's Lemma, $\Sigma$ contains a maximal element.

Let $S \in \Sigma$.
Since $0 \notin S$, $S^{-1}A \ne 0$.
By Theorem 1.3[Atiyah], $S^{-1}A$ contains at least one maximal ideal $\overline{m}$.
By Proposition 3.11(iv)[Atiyah], $\overline{m} = S^{-1}p$ for some $p \in \Spec(A)$ and $p \subset A \setminus S$.
This implies that $S \subset A \setminus p$.
Therefore, we showed that $\forall S \in \Sigma$, there exists $p \in \Spec(A)$ such that $S \subset A \setminus p$.

Let $S \in \Sigma$ be a maximal element.
Let $p$ be a prime ideal such that $S \subset A \setminus p$.
Since $A \setminus p \in \Sigma$ and $S$ is maximal, $S = A \setminus p$.
If there exists a prime $p' \subsetneq p$, then $S \subsetneq A \setminus p' \in \Sigma$, which is a contradiction.
Therefore, $A \setminus S = p$ is a minimal prime ideal.

Let $S, T \in \Sigma$ such that $S \subsetneq T$.
Then $S \subset A \setminus p$ and $T \subset A \setminus q$ for some $p, q \in \Spec(A)$.
Since $S \subsetneq T$, $S \subsetneq A \setminus q$.
In other words, $q \subsetneq A \setminus S$, so $A \setminus S$ is not a minimal prime ideal.
