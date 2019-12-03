---
layout: post
title:  "Application of Cauchy's theorem"
date:   2019-12-03
author: Hidenori
---

# Proposition
Compute the following integrals, where $\gamma$ is the boundary of the square with vertices at $\pm 4 \pm 4i$, positively oriented:

1. $\int_{\gamma}\frac{\exp(z^2)}{z^3} dz$
1. $\int_{\gamma}\frac{\exp(3z)}{(z - \pi i)^2} dz$
1. $\int_{\gamma}\frac{\sin(2z)}{(z - \pi)^2} dz$
1. $\int_{\gamma}\frac{\exp(z)\cos(z)}{(z - \pi)^3} dz$.

# Solution
## 1
Let $f(z) = \exp(z^2)$.
By Theorem 5.1 [A first course in complex analysis], $f''(0) = \frac{1}{\pi i} \int_{\gamma} \frac{f(z)}{(z - 0)^3} dz$.
Therefore, $\int_{\gamma}\frac{\exp(z^2)}{z^3} dz = \pi i f''(0) = 2$.

## 2
Let $f(z) = \exp(3z)$.
Using the same idea as above, the integral equals $2\pi i f'(\pi i) = 6\pi i\exp(3\pi i)$.

## 3
