---
layout: post
title:  "Plot of the set of exponent vectors of monomials"
date:   2019-10-29
author: Hidenori
---

# Proposition
Let $I = \ev{ x^6, x^2y^3, xy^7 } \subset k[x, y]$.

1. In the $(m, n)$-lane, plot the set of exponent vectors $(m, n)$ of monomials $x^my^n$ appearing in elements of $I$.
1. If we apply the division algorithm to an element $f \in k[x, y]$, using the generators of $I$ as divisors, what terms can appear in the remainder?

# Solution
![Plot](/assets/ideals_varieties_and_algorithms/chapter2/section4/ex-2-4-3.jpeg)
Therefore, any monomial $x^my^n$ such that


* $m = 0$, or
* $m = 1$ and $n \leq 6$, or
* $2 \leq m \leq 5$ and $n \leq 2$.

can appear in the remainder.
