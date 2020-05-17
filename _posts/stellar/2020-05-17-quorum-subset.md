---
layout: post
title:  "A quorum is a quorum in a projected system"
date:   2020-05-17
author: Hidenori
---

# Proposition
Let $U$ be a quorum in FBAS $\ev{V, Q}$, let $B \subset V$ be a set of nodes, and let $U' = U \setminus B$.
If $U' \ne \emptyset$, then $U'$ is a quorum in $\ev{V, Q}^B$.

# Solution
Since $U' \ne \emptyset$, it suffices to show that $\forall v \in U', \exists q \in Q^B(v), q \subset U'$.
Let $v \in U'$.
Then $v \in U$.
Since $U$ is a quorum in $\ev{V, Q}$, we can find $q \in Q(v)$ such that $q \subset U$.
Then $q' = q \setminus B \in Q^B(v)$, and $q' = q \setminus B \subset U \setminus B = U'$.
Therefore, $U'$ is a quorum in $\ev{V, Q}^B$.

