---
layout: post
title:  "A basic property of an ideal of a polynomial ring"
date:   2019-10-28
author: Hidenori
---

# Proposition
Let $I \subset k[x_1, \cdots, x_n]$ be an ideal, and let $f_1, \cdots, f_s \in k[x_1, \cdots, x_n]$.
Prove that the following statements are equivalent:

1. $f_1, \cdots, f_s \in I$.
1. $\ev{ f_1, \cdots, f_s } \subset I$.

# Solution

Since $I$ is closed under addition and closed under multiplication by elements in $k[x_1, \cdots, x_n]$, if $1$ is true, $\sum h_if_i \in I$ for any $h_i$'s.
Thus $1 \implies 2$.

Since $f_i \in \ev{ f_1, \cdots, f_s }$ for each $i$, $2 \implies 1$.
