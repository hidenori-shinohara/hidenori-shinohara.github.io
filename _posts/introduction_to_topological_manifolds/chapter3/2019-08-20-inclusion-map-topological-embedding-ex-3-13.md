---
layout: post
title:  "The inclusion map is a topological embedding."
date:   2019-08-20
author: Hidenori
---

# Proposition
Let $X$ be a topological space and let $S$ be a subspace of $X$.
Show that the inclusion map $S \rightarrow X$ is a topological embedding.

# Solution
Let $i_S$ denote the inclusion map.

* Injective?
    * $i_S(a) = i_S(b) \implies a = b$.
* Continuous?
    * Let $U \subset X$.
      Then $i_S^{-1}(U) = S \cap U$, and $S \cap U$ is open in the subspace topology $S$.
* Homeomorphism?
    * $i_S$ maps $S$ into $i_S(S) = S$.
      $i_S$ is the identity map when restricted to $S$.
      Therefore, it is a homeomorphism between $S$ and $S$.

Therefore, $i_S$ is a topological embedding.
