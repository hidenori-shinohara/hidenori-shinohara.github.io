---
layout: post
title:  "A symmetric polynomial in 3 variables"
date:   2019-11-12
author: Hidenori
---

# Proposition
Prove that $f \in k[x, y, z]$ is symmetric if and only if $f(x, y, z) = f(y, x, z) = f(y, z, x)$.

# Solution
Consider $S \subset S_3$ be the set of all permutations under which $f$ is invariant.
It suffices to show $S = S_3$.
Since $S$ has to be a subgroup of $S_3$, $\abs{S} \mid 6$.
$f(x, y, z) = f(y, x, z) = f(y, z, x)$ implies that $S$ contains two nontrivial elements, which are not the inverse of each other.
Therefore, $S$ contains at least three nontrivial elements with the identity element so $S = S_3$.
