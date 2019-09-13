---
layout: post
title:  "A restriction of a homeomorphism by an open set is a homeomorphism"
date:   2019-09-10
author: Hidenori
---

# Proposition
Suppose $f: X \rightarrow Y$ is a homeomorphism and $U \subset X$ is an open subset.
Show that $f(U)$ is open in $Y$ and the restriction $f\mid_U$ is a homeomorphism from $U$ to $f(U)$.

# Solution
* By [this post]({% post_url introduction_to_topological_manifolds/chapter2/2019-09-06-continuous-maps-ex-2-18 %}), $f\mid_U$ is continuous.
* $f \mid_U: U \rightarrow f(U)$ is surjective.
* $f \mid U$ is injective since $f$ is injective.
* Let $V \cap f(U) \subset Y \cap f(U)$ be an open set in $Y \cap U$ where $V$ is an open subset of $Y$.
  By the definition of a subspace topology, every open set can be expressed in this form.
  $f\mid_U^{-1}(V \cap f(U)) = U \cap f^{-1}(V \cap f(U)) = U \cap f^{-1}(V) \cap U = U \cap f^{-1}(V)$.
  Since $V$ is open in $Y$ and $f$ is continuous, $f^{-1}(V)$ is open in $X$.
  Therefore, $f^{-1}(V) \cap U$ is open in $U$.

Hence, $f\mid_U$ is a homeomorphism.
