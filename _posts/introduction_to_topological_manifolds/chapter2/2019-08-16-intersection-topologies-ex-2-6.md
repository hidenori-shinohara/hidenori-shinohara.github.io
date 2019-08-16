---
layout: post
title:  "An intersection of topologies is a topology"
date:   2019-08-16
author: Hidenori
---

# Proposition
Le $X$ be a set, and suppose $$\{ \mathscr{T}_{\alpha} \}_{\alpha \in A}$$ is a collection of topologies on $X$.
Show that the intersection $\mathscr{T} = \cap_{\alpha \in A} \mathscr{T}_{\alpha}$ is a topology on $X$.

# Solution

* Each $\mathscr{T}_{\alpha}$ contains $\emptyset$ and $X$ because it is a topology.
  Thus the intersection must contain $\emptyset$ and $X$.
* Let $S \subset \mathscr{T}$.
  Then $S \subset \mathscr{T}_{\alpha}$ for each $\alpha$.
  Then $$\bigcup_{U \in S} U \in \mathscr{T}_{\alpha}$$ for each $\alpha$.
  Therefore, $$\bigcup_{U \in S} U \in \mathscr{T}$$.
* Let $$U_{\alpha_1}, \cdots, U_{\alpha_n} \subset \mathscr{T}$$.
  Then $$U_{\alpha_1}, \cdots, U_{\alpha_n} \subset \mathscr{T}_{\alpha}$$ for each $\alpha$.
  Then $$U_{\alpha_1} \cap \cdots \cap U_{\alpha_n}  \in \mathscr{T}_{\alpha}$$ for each $\alpha$.
  Therefore, $$U_{\alpha_1} \cap \cdots \cap U_{\alpha_n} \in \mathscr{T}$$.

Therefore, $\mathscr{T}$ is a topology on $X$.
