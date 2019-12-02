---
layout: post
title:  "Integration by parts"
date:   2019-12-02
author: Hidenori
---

# Proposition
Prove the following integration by parts statement:
Let $f$ and $g$ be holomorphic in $G$ and suppose $\gamma \subset G$ is a piecewise smooth path from $\gamma(a)$ to $\gamma(b)$.
Then

$$
\begin{align*}
  \int_{\gamma} fg' = f(\gamma(b))g(\gamma(b)) - f(\gamma(a))g(\gamma(a)) - \int_{\gamma} f'g.
\end{align*}
$$

# Solution

$$
\begin{align*}
  \int_{\gamma} (fg)'
    &= \int_{\gamma} f'g + fg' \\
    &= \int_{a}^{b} (f'g + fg')(\gamma(t))\gamma'(t) dt \\
    &= \int_{a}^{b} (f'g)(\gamma(t))\gamma'(t) dt + \int_{a}^{b} (fg')(\gamma(t))\gamma'(t) dt \\
    &= \int_{\gamma} f'g + \int_{\gamma} fg'.
\end{align*}
$$

On the other hand, $(fg) \circ \gamma$ is a function whose derivative is $((fg)' \circ \gamma) \cdot \gamma'$.

Therefore, $\int_{\gamma} (fg)' = \int_{a}^{b} (fg)'(\gamma(t))\gamma'(t) dt = ((fg) \circ \gamma)(b) - ((fg) \circ \gamma)(a) = f(\gamma(b))g(\gamma(b)) - f(\gamma(a))g(\gamma(a))$.

By putting them together, we obtain
$$
\begin{align*}
  \int_{\gamma} fg' = f(\gamma(b))g(\gamma(b)) - f(\gamma(a))g(\gamma(a)) - \int_{\gamma} f'g.
\end{align*}
$$
