---
layout: post
title:  "Basic properties of quorums"
date:   2020-05-16
author: Hidenori
---

# Proposition 1
In an FBAS $(V, Q)$, the union of two quorums is a quorum.

## Proof
Let $U_1, U_2$ be two quorums.
Let $v \in U_1 \cup U_2$.
Then $v \in U_i$ for $i = 1$ or $i = 2$.
Then $q \subset U_i$ for some $q \in Q(v)$.
Therefore, $q \subset U_1 \cup U_2$, so $U_1 \cup U_2$ is indeed a quorum.

# Proposition 2
In an FBAS $(V, Q)$, the intersection of two quorums is not necessarily a quorum.

## Proof
Let $V = \\{ v_1, \cdots, v_4 \\}$ and
* $Q(v_1) = \\{ \\{ v_1, v_2, v_3 \\}, \\{ v_1, v_2, v_4 \\}, \\{ v_1, v_3, v_4 \\} \\}$,
* $\vdots$
* $Q(v_4) = \\{ \\{ v_1, v_2, v_4 \\}, \\{ v_1, v_3, v_4 \\}, \\{ v_2, v_3, v_4 \\} \\}$.

In other words, $Q(v_i) = \\{ \\{ v_i, v_j, v_k \\} \mid i \ne j, j \ne k, i \ne k \\}$.

Then $U_1 = \\{ v_1, v_2, v_3 \\}$ is a quorum, and $U_2 = \\{ v_2, v_3, v_4 \\}$ is a quorum.
However, $U_1 \cap U_2 = \\{ v_2, v_3 \\}$ is not a quorum because the size of any quorum slice is 3.

# Proposition 3
In an FBAS $(V, Q)$, $V$ is a quorum.

## Proof
For any $v \in V$, for any $q \in Q(v)$, $q \subset V$.
Therefore, $V$ is indeed a quorum.
