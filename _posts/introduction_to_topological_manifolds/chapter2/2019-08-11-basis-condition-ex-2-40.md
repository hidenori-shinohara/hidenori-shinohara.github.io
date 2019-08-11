---
layout: post
title:  "Basis criterion"
date:   2019-08-11
author: Hidenori
---

# Proposition

Suppose $X$ is a topological space, and $\mathcal{B}$ is a basis for its topology.
Show that a subset $U \subset X$ is open if and only if it satisfies the following conditions:

$$
\begin{align*}
  \forall p \in U, \exists B \in \mathcal{B}, p \in B \subset U.
\end{align*}
$$

# Solution

Suppose that $U$ is open.
Since $\mathcal{B}$ is a basis, there exist $\\{ B_{\alpha} \\} \subset \mathcal{B}$ such that $U = \bigcup B_{\alpha}$.
Then for each $p \in U$, there must exist a $B_{\alpha}$ such that $p \in B_{\alpha} \subset U$.

On the other hand, suppose that $\forall p \in U, \exists B \in \mathcal{B}, p \in B \subset U$.
For each $p \in U$, let $B_p$ denote a basis element such that $p \in B_p \subset U$.
In case there are more than one, we will pick one arbitrarily.
Then $\bigcup_{p \in U} B_p = U$, so $U$ is open.
