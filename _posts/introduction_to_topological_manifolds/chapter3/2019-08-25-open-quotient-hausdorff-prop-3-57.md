---
layout: post
title:  "Open quotient maps and Hausdorff spaces"
date:   2019-08-25
author: Hidenori
---

# Proposition
Suppose $q: X \rightarrow Y$ is an open quotient map.
Then $Y$ is Hausdorff if and only if the set $\mathscr{R} = \\{ (x_1, x_2) \mid q(x_1) = q(x_2) \\}$ is closed in $X \times X$.

# Solution
First, we will suppose that $Y$ is Hausdorff.
We will show that $\mathscr{R}$ is closed in $X \times X$.
Let $(a, b) \in X \times X \setminus \mathscr{R}$.
Then $q(a) \ne q(b)$.

Since $Y$ is Hausdorff, there must exist disjoint neighborhoods $U, V$ of $q(a), q(b)$, respectively.
Then $a \in q^{-1}(U), b \in q^{-1}(V)$.
$q$ is a quotient map, so $q^{-1}(U)$ and $q^{-1}(V)$ are both open.
Thus $q^{-1}(U) \times q^{-1}(V)$ is a neighborhood of $(a, b)$.
We claim that this neighborhood is contained in $X \times X \setminus \mathscr{R}$.
Let $(c, d) \in q^{-1}(U) \times q^{-1}(V)$.

* $q(c) \in q(q^{-1}(U)) = U$ because $q$ is surjective.
* $q(d) \in q(q^{-1}(V)) = V$ because $q$ is surjective.

Since $U \cap V = \emptyset$, $q(c) \ne q(d)$.
Therefore, $(c, d) \in X \times X \setminus \mathscr{R}$.
Thus $X \times X \setminus \mathscr{R}$ is open, so $\mathscr{R}$ is closed.

TODO

