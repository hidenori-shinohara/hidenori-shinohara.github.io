---
layout: post
title:  "Weierstrass M-test"
date:   2019-12-24
author: Hidenori
---

# Proposition
Use the Weierstrass M-test to show that each of the following series converges uniformly on the given domain.
1. $\sum_{k \geq 1} \frac{z^k}{k^2}$ on $\overline{D}[0, 1]$.
1. $\sum_{k \geq 0} \frac{1}{z^k}$ on $\\{ z \in \mathbb{C} : \abs{z} \geq 2 \\}$.
1. $\sum_{k \geq 0} \frac{z^k}{z^k + 1}$ on $\overline{D}[0, r]$ where $0 \leq r < 1$.

# Solution
## 1
Let $M_k = 1/k^2$.
Then $\abs{\frac{z^k}{k^2}} \leq M_k$ for all $k$ and $z \in \overline{D}[0, 1]$, and [$\sum M_k$ converges](https://en.wikipedia.org/wiki/Basel_problem).

## 2
Let $M_k = 1/2^k$.
Ten $\abs{\frac{1}{z^k}} \leq M_k$ for all $k$ and $z$ in the specified domain.

## 3
Let $M_k = \frac{r^k}{1 - r}$.

We have $1 = \abs{1 + z^k - z^k} \leq \abs{1 + z^k} + \abs{z^k}$.
Then $1 - \abs{z^k} \leq \abs{1 + z^k}$.
Since $\abs{z^k} = \abs{z}^k \leq r$, $1 - r \leq \abs{1 + z^k}$.

Therefore, $\abs{\frac{z^k}{z^k + 1}} \leq \frac{r^k}{1 - r} = M_k$.
