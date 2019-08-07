---
layout: post
title:  "A change-of-basepoint map is an isomorphism."
date:   2019-08-07
author: Hidenori
---

# Proposition
The map $\beta_h: \pi_1(X, x_1) \rightarrow \pi_1(X, x_0)$ is an isomorphism.

# Solution
Let $h$ be a path from $x_0$ to $x_1$.
Define $\beta_h: \pi_1(X, x_1) \rightarrow \pi_1(X, x_0)$ such that $\beta_h([f]) = [h \cdot f \cdot \overline{h}]$.

* $\beta_h$ is well-defined because $h \cdot f \cdot \overline{h}$ is a loop based at $x_0$ for any $[f] \in \pi_1(X, x_1)$.
* $\beta_h$ is a homomorphism because

  $$
  \begin{align*}
    \beta_h([f] \cdot [g])
      &= \beta_h([f \cdot g]) \\
      &= [h \cdot f \cdot g \cdot \overline{h}] \\
      &= [h \cdot f \cdot \overline{h} \cdot h \cdot g \cdot \overline{h}] \\
      &= [h \cdot f \cdot \overline{h}] \cdot [h \cdot g \cdot \overline{h}] \\
      &= \beta_h([f]) \cdot \beta_h([g]).
  \end{align*}
  $$

* $\beta_h(\beta_{\overline{h}}([f])) = [h \cdot \overline{h} \cdot f \cdot h \overline{h}] = [f]$.
* $\beta_{\overline{h}}(\beta_{h}([f])) = [\overline{h} \cdot h \cdot f \cdot \overline{h} \cdot h] = [f]$.

Therefore, $\beta_h$ is an isomorphism.
