---
layout: post
title:  "Homeomorphism between a line and a line in a space"
date:   2019-08-26
author: Hidenori
---

# Proposition
$\mathbb{R}^{n - 1}$ is homeomorphic to $\partial \mathbb{H}^n$.

# Solution
Let $f: \mathbb{R}^{n - 1} \rightarrow \partial \mathbb{H}^n$ be defined such that $f(x_1, \cdots, x_{n - 1}) = (x_1, \cdots, x_{n - 1}, 0)$.

* Injective?
    * $f(x) = f(y)$ implies that $(x, 0) = (y, 0)$, so $x = y$.
* Surjective?
    * For any $(x_1, \cdots, x_{n - 1}, 0 \in \mathbb{H}^n$, $f(x_1, \cdots, x_{n - 1}) = (x_1, \cdots, x_{n - 1}, 0)$.
* Continuous?
    * Each $(x_1, \cdots, x_{n - 1}) \mapsto x_i$ is a [canonical projection]({% post_url /introduction_to_topological_manifolds/chapter3/2019-08-24-canonical-projection-continuous-ex-3-29 %}), so it is continuous.
      $(x_1, \cdots, x_{n - 1}) \mapsto 0$ is a constant function, so it is continuous.
      Since each component function of $f$ is continuous, $f$ is continuous.
* Open?
    * Let $U \subset \mathbb{R}^{n - 1}$ be open.
      Then $f(U) = U \times \\{ 0 \\} = (U \times \mathbb{R}) \cap \partial \mathbb{H}^n$.
      $U \times \mathbb{R}$ is open in $\mathbb{R}^n$, so $(U \times \mathbb{R}) \cap \partial \mathbb{H}^n$ is open in $\partial \mathbb{H}^n$.

Therefore, $f$ is a homeomorphism.
