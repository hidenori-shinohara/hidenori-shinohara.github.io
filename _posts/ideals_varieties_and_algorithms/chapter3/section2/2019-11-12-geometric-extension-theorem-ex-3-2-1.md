---
layout: post
title:  "Proof of the geometric extension theorem"
date:   2019-11-12
author: Hidenori
---

# Proposition
Prove the Geometric Extension Theorem using the Extension Theorem and Lemma 1. (Ideals, Varieties, and Algorithms)

# Solution
First, we will show that $\pi_1(V) \cup (V(c_1, \cdots, c_s) \cap V(I_1)) \subset V(I_1)$.

* $\pi_1(V) \subset V(I_1)$.
    * Lemma 1 on P.129 (Ideals, Varieties, and Algorithms)
* $(V(c_1, \cdots, c_s) \cap V(I_1)) \subset V(I_1)$.
    * This is trivial.

Next, we will show that $V(I_1) \subset \pi_1(V) \cup (V(c_1, \cdots, c_s) \cap V(I_1))$.
Let $(a_2, \cdots, a_n) \in V(I_1) \setminus \pi_1(V)$.
If no such element exists, we are done.
Since $(a_2, \cdots, a_n) \in V(I_1)$, $(a_2, \cdots, a_n)$ is a partial solution.
Since $(a_2, \cdots, a_n) \notin \pi_1(V)$, $\forall a_1 \in k, (a_1, \cdots, a_n) \notin V$.
By taking the contrapositive of the Extension Theorem, $(a_2, \cdots, a_n) \in V(c_1, \cdots, c_n)$.
