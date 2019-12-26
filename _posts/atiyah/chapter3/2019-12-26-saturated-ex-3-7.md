---
layout: post
title:  "Saturated multiplicatively closed subsets(WIP)"
date:   2019-12-26
author: Hidenori
---

# Proposition
A multiplicatively closed subset $S$ of a ring $A$ is said to be saturated if

$$
\begin{align*}
  xy \in S \iff x \in S \text{ and } y \in S.
\end{align*}
$$

Prove that
1. $S$ is saturated $\iff A \setminus S$ is a union of prime ideals.
1. If $S$ is any multiplicatively closed subset of $A$, there is a unique smallest saturated multiplicatively closed subset $\overline{S}$ containing $S$, and that $\overline{S}$ is the complement in $A$ of the union of the prime ideals which do not meet $S$.
1. If $S = 1 + a$ where $a$ is an ideal of $A$, find $\overline{S}$.

# Solution
## 1
Suppose $A \setminus S$ is the union of some prime ideals.
Let $x, y \in A$.
* Suppose $xy \notin S$.
  Then $xy \in A \setminus S$, so $xy \in p$ for some $p \in \Spec(A)$.
  Thus $x \in p$ or $y \in p$, so $x \in A \setminus S$ or $y \in A \setminus S$.
  This implies $x \notin S$ or $y \notin S$.
* Suppose $x \notin S$ or $y \notin S$.
  Then $x \in A \setminus S$ or $y \in A \setminus S$.
  Without loss of generality, $x \in A \setminus S$.
  Then $x \in p$ for some $p \in \Spec(A)$.
  Since $p$ is an ideal, $xy \in p$.
  Thus $xy \notin S$.
Therefore, $xy \notin S \iff (x \notin S \text{ or } y \notin S)$.
In other words, $xy \in S \iff (x \in S \text{ and } y \in S)$.

On the other hand, suppose $S$ is saturated.
Let $a \in A \setminus S$.
Then $(a)$ is an ideal disjoint from $S$ because $xa \in S$ implies $x \in S$ and $a \in S$.

Let $\Sigma$ be the set of ideals of $A$ containing $a$ and disjoint from $S$.
Then $(a) \in \Sigma$, so $\Sigma$ is nonempty.
$\Sigma$ is a partially ordered set by the usual set inclusion.
Let $I_1 \subset I_2 \subset \cdots$ be an ascending chain in $\Sigma$.
Then $I = \cup I_i$ is an ideal of $A$ containing $a$ and disjoint from $S$.
Thus we found an upper bound of the given chain.
By Zorn's Lemma, $\Sigma$ contains a maximal element $m$.

Let $x, y \in A \setminus m$.
Then $m + (x), m + (y) \notin \Sigma$ because $m$ is maximal.
Since $m + (x), m + (y)$ are ideals containing $a$, they cannot be disjoint from $S$.
In other words, there exist $s \in (m + (x)) \cap S$ and $t \in (m + (y)) \cap S$.
Then $st \in S$ because $S$ is multiplicatively closed, so $st \notin m$ because $m$ is disjoint from $S$.
However, $st \in (m + (x))(m + (y)) = m + (xy)$.
Therefore, $xy \notin m$, and thus $m$ is a prime ideal.

The argument above shows that, for every $a \in A \setminus S$, there exists a prime ideal $p \in \Spec(A)$ such that $a \in p \subset A \setminus S$.
Therefore, $A \setminus S$ is the union of such prime ideals.

## 2
Let $T$ be the complement of all prime ideals $p \in \Spec(A)$ such that $p \cap S = \emptyset$.
Then $S \subset T$.
By Part 1, $T$ is saturated.
Let $T'$ be a saturated multiplicatively closed subset such that $T' \subsetneq T$.
By Part 1, $A \setminus T'$ must be a union of some prime ideals.
Since $T' \subsetneq T$, at least one of the prime ideals that make up $A \setminus T'$ cannot be disjoint from $S$.
In other words, $S \not\subset T'$.
Therefore, $T$ is a smallest saturated multiplicatively closed subset.
Since the intersection of two saturated multiplicatively closed subsets is a saturated multiplicatively closed subset, $T$ must be the unique one.

## 3
TODO
