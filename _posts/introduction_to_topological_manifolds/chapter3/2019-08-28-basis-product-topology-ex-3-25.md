---
layout: post
title:  "Basis for a product topology"
date:   2019-08-28
author: Hidenori
---

# Proposition

Let $X_1, \cdots, X_n$ be topological spaces.

Let $\mathcal{B} = \\{ U_1 \times \cdots \times U_n \mid \text{$U_i$ is an open subset of $X_i$, $i = 1, \cdots, n$} \\}$.

Then $\mathcal{B}$ is a basis for $X_1 \times \cdots \times X_n$.

# Solution

Since $X_1 \times \cdots \times X_n \in \mathcal{B}$, the union of all elements in $\mathcal{B}$ is $X_1 \times \cdots \times X_n$.

Let $U_1 \times \cdots \times U_n, V_1 \times \cdots \times V_n \in \mathcal{B}$.
Let $x_1 \times \cdots \times x_n \in (U_1 \times \cdots \times U_n) \cap (V_1 \times \cdots \times V_n)$.
(We are done if the intersection is empty.)
Then, for each $i$, $x_i \in U_i \cap V_i$, and $U_i \cap V_i$ is an open set in $X_i$.
Therefore, $(U_1 \cap V_1) \times \cdots \times (U_n \cap V_n) \in \mathcal{B}$.

Hence, $\mathcal{B}$ is a basis.
