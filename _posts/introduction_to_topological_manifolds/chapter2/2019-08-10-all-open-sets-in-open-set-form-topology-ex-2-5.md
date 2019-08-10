---
layout: post
title:  "Show that the collection of all open subsets of $X$ that are contained in open $Y$ is a topology on $Y$."
date:   2019-08-10
author: Hidenori
---

# Proposition
Suppose $X$ is a topological space and $Y$ is an open subset of $X$.
Show that the collection of all open subsets of $X$ that are contained in $Y$ is a topology on $Y$.

# Solution
Let $\mathcal{T}$ be the topology on $X$, and $\mathcal{T}' = \\{ U \in \mathcal{T} \mid U \subset Y \\}$.

* $\emptyset \in \mathcal{T}'$.
* $Y \in \mathcal{T}'$.
* Let $\\{ U_{\alpha} \\} \subset \mathcal{T}'$.
  For all $\alpha$, $U_{\alpha} \in \mathcal{T}$ and $U_{\alpha} \subset Y$.
  Thus $\bigcup_{\alpha} U_{\alpha} \in \mathcal{T}'$.
* Let $U_{\alpha_1}, \cdots, U_{\alpha_n} \in \mathcal{T}'$.
  For all $i = 1, \cdots, n$, $U_{\alpha_i} \in \mathcal{T}$ and $U_{\alpha_i} \subset Y$.
  Thus $\bigcap_{i=1}^n U_{\alpha_i} \in \mathcal{T}'$.

Therefore, $\mathcal{T}'$ is a topology on $Y$.
