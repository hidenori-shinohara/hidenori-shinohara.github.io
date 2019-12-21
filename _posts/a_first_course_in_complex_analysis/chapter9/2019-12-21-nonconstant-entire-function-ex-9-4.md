---
layout: post
title:  "An complex number is arbitrarily closed to a number in $f(\\mathbb{C})$ if $f$ is nonconstant and entire"
date:   2019-12-21
author: Hidenori
---

# Proposition
Suppose $f$ is a nonconstant entire function.
Prove that any complex number is arbitrarily close to a number in $f(\mathbb{C})$.

# Solution
Let $z_0 \in \mathbb{C}$ and $r > 0$.
Suppose that $\abs{f(z) - z_0)} \geq r$ for all $z \in \mathbb{C}$.
Then the function $g(z) = \frac{1}{f(z) - z_0}$ is a bounded entire function.
By [Liouville's Theorem](https://en.wikipedia.org/wiki/Liouville%27s_theorem_(complex_analysis)), $g(z)$ is constant.
However, this implies that $f(z)$ is constant, thus this is a contradiction.
Therefore, there exists a $z \in \mathbb{C}$ such that $\abs{f(z) - z_0} < r$.
In other words, any complex number is arbitrarily closed to a number in $f(\mathbb{C})$.
