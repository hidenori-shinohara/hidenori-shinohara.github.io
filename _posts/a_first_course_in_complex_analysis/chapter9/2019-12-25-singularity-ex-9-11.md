---
layout: post
title:  "Isolated singularities"
date:   2019-12-25
author: Hidenori
---

# Proposition
Suppose $f$ has an isolated singularity at $z_0$.
1. Show that $f'$ has an isolated singularity at $z_0$.
1. Find $\Res_{z = z_0}(f')$.

# Solution

## 1
Since $f$ has an isolated singularity at $z_0$, there exists a punctured disk with the radius $r$ such that $f$ is holomorhpic in it.
Then for every point $z'$ such that $0 < \abs{z_0 - z'} < r$, $f'$ is differentiable at $z'$.
Thus $f'$ has an isolated singularity at $z_0$.

## 2
Let $\sum_{k \in \mathbb{Z}} c_k(z - z_0)^k$ be the Laurent series of $f$.
Then $f' = \sum_{k \in \mathbb{Z}} kc_k(z - z_0)^{k - 1}$.
Thus the coefficient of $1/z$ is $0 \cdot c_0 = 0$.
Thus $\Res_{z = z_0}(f') = 0$.
