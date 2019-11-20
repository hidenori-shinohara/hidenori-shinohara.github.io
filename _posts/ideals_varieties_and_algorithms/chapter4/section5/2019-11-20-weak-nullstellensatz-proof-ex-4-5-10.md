---
layout: post
title:  "Proof of the Weak Nullstellensatz"
date:   2019-11-20
author: Hidenori
---

# Proposition
Theorem: if $k$ is an algebraically closed field, then every maximal ideal of $k[x_1, \cdots, x_n]$ is of the form $\ev{x_1 - a_1, \cdots, x_n - a_n}$ for some $a_1, \cdots, a_n \in k$.
Prove that the theorem above implies that the Weak Nullstellensatz.

# Solution
Let $I \ne k[x_1, \cdots, x_n]$ be an ideal.
$I \subset \ev{x_1 - a_1, \cdots, x_n - a_n}$ would imply that $(a_1, \cdots, a_n) \subset V(I)$, so $V(I) \ne \emptyset$.
Therefore, it suffices to show that $I$ is contained in a maximal ideal.

Let $I_0 = I$.

Suppose that we have constructed $I_{k - 1}$ for some $k \in \mathbb{N}$.
Then construct $I_{k}$ as following:

Choose an element $x \in k[x_1, \cdots, x_n] \setminus I_{k - 1}$ such that the smallest ideal containing $I_{k - 1}$ and $x$ is not equal to $k[x_1, \cdots, x_n]$.
If no such element exists, $I_{k - 1}$ is a maximal ideal, and we are done.
Suppose that there exits such an element $x$.
Then let $I_k$ be the smallest ideal containing $I_{k - 1}$ and $x$.
(It does not matter which $x$ we choose in case there are more than one such $x$.)

This process generates a strictly ascending chain of ideals $I_0 \subsetneq I_1 \subsetneq I_2 \subsetneq$.
By the ascending chain condition, it is impossible that we obtain an infinite chain.
Therefore, this process must terminate after a finite number of steps.
Hence, we must be able to find a maximal ideal containing $I$.
