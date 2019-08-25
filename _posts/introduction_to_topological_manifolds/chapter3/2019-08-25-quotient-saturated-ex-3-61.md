---
layout: post
title:  "Quotient maps and saturated sets"
date:   2019-08-25
author: Hidenori
---

# Proposition
A continuous surjective map $q: X \rightarrow Y$ is a quotient map if and only if it takes saturated open subsets to open subsets, or saturated closed subsets to closed subsets.
# Solution

Suppose $q$ is a quotient map.
Let $U \subset X$ be a saturated open subset.
[As we showed before]({% post_url introduction_to_topological_manifolds/chapter3/2019-08-25-properties-of-saturated-sets-ex-3-59 %}), $U = q^{-1}(q(U))$.
Since $q$ is a quotient map and $U$ is open, $q(U)$ must be open.

Let $C \subset X$ be a saturated closed subset.
Then $C = q^{-1}(q(C))$.
We claim that $q(C)$ is closed in $Y$.
$q^{-1}(Y \setminus q(C)) = q^{-1}(Y) \setminus q^{-1}(q(C)) = X \setminus C$, which is open.
Therefore, $Y \setminus q(C)$ is open, so $q(C)$ is closed.

Suppose that $q$ is a continuous surjective map that takes saturated open subsets to open subsets.
We will show that $q$ is a quotient map.
It suffices to show that if $q^{-1}(V)$ is open, $V$ is open in $Y$.
Let $V \subset Y$ be given such that $q^{-1}(V)$ is open.

Then, $q^{-1}(V)$ is a saturated open subset.
This implies that $q(q^{-1}(V))$ is open since $q$ takes a saturated open subset to an open subset.
Since $q$ is surjective, $q(q^{-1}(V)) = V$.
Therefore, $V$ is open in $Y$.

We have shown that $q^{-1}(V)$ is open if and only if $V$ is open.
Therefore, $q$ is a quotient map.

Suppose that $q$ is a continuous surjective map that takes saturated closed subsets to closed subsets.
We will show that $q$ is a quotient map.
It suffices to show that if $q^{-1}(V)$ is open, $V$ is open in $Y$.
Let $V \subset Y$ be given such that $q^{-1}(V)$ is open.

Then $X \setminus q^{-1}(V)$ is closed.
Moreover, $X \setminus q^{-1}(V) = q^{-1}(Y) \setminus q^{-1}(V) = q^{-1}(Y \setminus V)$.
Therefore, $q^{-1}(Y \setminus V)$ is a saturated closed set.
This implies that $q(q^{-1}(Y \setminus V))$ is closed since $q$ takes a saturated closed subset to a closed subset.
Since $q$ is surjective, $q(q^{-1}(Y \setminus V)) = Y \setminus V$.
Therefore, $Y \setminus V$ is closed in $Y$, so $V$ is open in $Y$.

We have shown that $q^{-1}(V)$ is open if and only if $V$ is open.
Therefore, $q$ is a quotient map.
