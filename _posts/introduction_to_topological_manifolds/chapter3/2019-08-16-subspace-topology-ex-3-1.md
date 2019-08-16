---
layout: post
title:  "A subspace topology is indeed a topology"
date:   2019-08-16
author: Hidenori
---

# Proposition
Let $S \subset X$ and $\mathscr{T}_S = \\{ S \cap U \mid U \in \mathscr{T} \\}$.
Then $\mathscr{T}_S$ is a topology on $S$.

# Solution

* $\emptyset$ is in $\mathscr{T}$, so $S \cap \emptyset = \emptyset \in \mathscr{T}_S$.
* $X$ is in $\mathscr{T}$, so $S \cap X = S \in \mathscr{T}_S$.
* Let $$\{ S \cap U_{\alpha} \} \subset \mathscr{T}_S$$.
  Then $$\bigcup (S \cap U_{\alpha}) = S \cap (\bigcup U_{\alpha})$$.
  $\bigcup U_{\alpha} \in \mathscr{T}$, so $S \cap (\bigcup U_{\alpha}) \in \mathscr{T}_S$.
* Let $$\{ S \cap U_1, \cdots, S \cap U_n \} \subset \mathscr{T}_S$$.
  Then $\bigcap (S \cap U_{k}) = S \cap (\bigcap U_{k})$.
  $\bigcap U_{k} \in \mathscr{T}$, so $S \cap (\bigcap U_{k}) \in \mathscr{T}_S$.

Therefore, $\mathscr{T}_S$ is a topology on $S$.
