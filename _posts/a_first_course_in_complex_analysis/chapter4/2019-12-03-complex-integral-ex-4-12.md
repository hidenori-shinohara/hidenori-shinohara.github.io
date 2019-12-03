---
layout: post
title:  "Complex integral"
date:   2019-12-03
author: Hidenori
---

# Proposition
Compute $\int_{C[0, 2]} z^{1/2} dz$.

# Solution
$\gamma(t) = 2\exp(it)$ is a parametrization of $C[0, 2]$ where $0 \leq t \leq 2\pi$.

$$
\begin{align*}
  \int_{\gamma} z^{1/2} dz
    &= \int_{0}^{2\pi} (2e^{it})^{1/2} (2ie^{it}) dt \\
    &= 2^{3/2}i\int_{0}^{2\pi} e^{3it/2} dt \\
    &= 2^{3/2}i\frac{2}{3i}e^{3it/2} \Big\vert^{2\pi}_0 \\
    &= \frac{2^{5/2}}{3}(e^{3\pi i} - 1) \\
    &= \frac{-2^{7/2}}{3}.
\end{align*}
$$
