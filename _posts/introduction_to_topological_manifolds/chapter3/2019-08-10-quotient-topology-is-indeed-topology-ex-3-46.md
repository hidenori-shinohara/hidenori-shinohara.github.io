---
layout: post
title:  "The quotient topology is indeed a topology."
date:   2019-08-10
author: Hidenori
---

# Proposition
The quotient topology is indeed a topology.

# Solution
Let $(X, \mathcal{T})$ be a topological space, $Y$ be any set, $q: X \rightarrow Y$ be a surjective map.
Let $\mathcal{T}' = \\{ V \subset Y \mid q^{-1}(V) \in \mathcal{T} \\}$.

We claim that $\mathcal{T}'$ is a topology.

* $q^{-1}(\emptyset) = \emptyset$, so $\emptyset \in \mathcal{T}'$.
* $q^{-1}(Y) = X$ because $q$ is surjective.
  Thus $Y \in \mathcal{T}'$.
* Let $\\{ V_{\alpha} \\} \subset \mathcal{T}'$.
  $q^{-1}(\bigcup_{\alpha} V_{\alpha}) = \bigcup_{\alpha} q^{-1}(V_{\alpha})$.
  Then each $q^{-1}(V_{\alpha}) \in \mathcal{T}$, so the union is in $\mathcal{T}$.
  Therefore, $\bigcup_{\alpha} V_{\alpha} \in \mathcal{T}'$.
* Let $V_{\alpha_1}, \cdots, V_{\alpha_n} \in \mathcal{T}'$.
  $q^{-1}(\bigcap_{i=1}^n V_{\alpha_i}) = \bigcap_{i=1}^n q^{-1}(V_{\alpha_i})$.
  Then each $q^{-1}(V_{\alpha_i}) \in \mathcal{T}$, so the finite intersection is in $\mathcal{T}$.
  Therefore, $\bigcap_{i=1}^n V_{\alpha_i} \in \mathcal{T}'$.

Therefore, $\mathcal{T}'$ is a topology.
