---
layout: post
title:  "Show that the disjoint union topology is indeed a topology."
date:   2019-08-10
author: Hidenori
---

# Proposition
Show that the disjoint union topology is indeed a topology.

# Solution

Let $$(X_{\alpha})_{\alpha \in A}$$ be an indexed family of nonempty topological spaces.
Let $$\mathscr{T}_{\alpha}$$ be the topology on $X_{\alpha}$ for each $\alpha \in A$.
Let $\mathscr{T}$ denote the disjoint union topology on $\sqcup_{\alpha \in A} X_{\alpha}$.

* $\forall \alpha \in A, \emptyset \cap X_{\alpha} = \emptyset$, so $\emptyset \in \mathscr{T}$.
* $\forall \alpha \in A, (\sqcup_{\alpha \in A} X_{\alpha}) \cap X_{\alpha} = X_{\alpha}$, so $(\sqcup_{\alpha \in A} X_{\alpha}) \in \mathscr{T}$.
* Let $\\{ U_{\beta} \\} \subset \mathscr{T}$ where $B$ is the indexed set.
  Let $\alpha \in A$ be given.
  $\forall \beta, U_{\beta} \cap X_{\alpha} \in T_{\alpha}$.
  Then we have $$(\bigcup_{\beta \in B} U_{\beta}) \cap X_{\alpha} = \bigcup_{\beta \in B} (U_{\beta} \cap X_{\alpha}) \in \mathscr{T}_{\alpha}$$ since $\mathscr{T}_{\alpha}$ must be closed under arbitrary union.
  Since $\alpha$ was chosen arbitrarily, this implies that $$\bigcup_{\beta \in B} U_{\beta} \in \mathscr{T}$$.
* Let $U_{\beta_1}, U_{\beta_2}, \cdots, U_{\beta_n} \in \mathscr{T}$.
  Let $\alpha \in A$ be given.
  $\forall i = 1, \cdots, n, U_{\beta_i} \cap X_{\alpha} \in T_{\alpha}$.
  Then we have $$(\bigcap_{i=1}^n U_{\beta_i}) \cap X_{\alpha} = \bigcap_{i=1}^n (U_{\beta_i} \cap X_{\alpha}) \in \mathscr{T}_{\alpha}$$ since $\mathscr{T}_{\alpha}$ must be closed under finite intersection.
  Since $\alpha$ was chosen arbitrarily, this implies that $$\bigcap_{i=1}^n U_{\beta_i} \in \mathscr{T}$$.

Therefore, $\mathcal{T}$ is indeed a topology.
