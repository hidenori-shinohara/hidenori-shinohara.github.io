---
layout: post
title:  "Basis for a product topology"
date:   2019-08-11
author: Hidenori
---

# Proposition
Let $(X_1, \mathscr{T}_1), \cdots, (X_n, \mathscr{T}_n)$ be topological spaces.
Let $\mathscr{B} = \mathscr{T}_1 \times \cdots \mathscr{T}_n$.

Prove that $\mathscr{B}$ is a basis for a topology.

# Solution
* $X_1 \times \cdots \times X_n \in \mathscr{B}$, so $\bigcup_{B \in \mathscr{B}} B = X_1 \times \cdots \times X_n$.
* Let $U_1 \times \cdots \times U_n, V_1 \times \cdots \times V_n \in \mathscr{B}$.
  Then $U_1 \times \cdots \times U_n \cap V_1 \times \cdots \times V_n = (U_1 \cap V_1) \times \cdots \times (U_n \cap V_n)$.
  Since $U_i \cap V_i \in \mathscr{T}_i$ for each $i$, $U_1 \times \cdots \times U_n \cap V_1 \times \cdots \times V_n$ is in $\mathscr{B}$.

By Proposition 2.44 on P.34 (Introduction to Topological Manifolds), $\mathscr{B}$ is a basis.
