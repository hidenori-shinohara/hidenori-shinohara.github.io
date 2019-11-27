---
layout: post
title:  "Change of variables"
date:   2019-11-27
author: Hidenori
---

# Proposition
Prove Proposition 4.2 (A first course in complex analysis) and the fact that the length of $\gamma$ does not change under reparametrization.


# Solution
Let $\tau:[c, d] \rightarrow [a, b]$ be given such that $\sigma = \gamma \circ \tau$.

$$
\begin{align*}
  \int_{c}^{d} f(\sigma(t))\sigma'(t) dt
    &= \int_{c}^{d} f((\gamma \circ \tau)(t))(\gamma \circ \tau)'(t) dt \\
    &= \int_{c}^{d} ((f \circ \gamma) \cdot \gamma')(\tau(t))\tau'(t) dt \\
    &= \int_{a}^{b} ((f \circ \gamma) \cdot \gamma')(t) dt & \text{(Theorem A.6)} \\
    &= \int_{a}^{b} f(\gamma(t))\gamma'(t) dt.
\end{align*}
$$
