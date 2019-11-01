---
layout: post
title:  "Basic properties of ideals"
date:   2019-11-01
author: Hidenori
---

# Proposition
Let $I$ be an ideal in $k[x_1, \cdots, x_n]$.
1. Prove that $1 \in I$ if and only if $I = k[x_1, \cdots, x_n]$.
1. More generally, prove that $I$ contains a nonzero constant if and only if $I = k[x_1, \cdots, x_n]$.
1. Suppose $f, g \in k[x_1, \cdots, x_n]$ satisfy $f^2, g^2 \in I$.
   Prove that $(f + g)^3 \in I$.
1. Now suppose $f, g \in k[x_1, \cdots, x_n]$ satisfy $f^r, g^s \in I$.
   Prove that $(f + g)^{r + s - 1} \in I$.

# Solution

## 1
If $1 \in I$, then $\forall f \in k[x_1, \cdots, x_n], f = f \cdot 1 \in I$.
If $I = k[x_1, \cdots, x_n]$, then $1 \in k[x_1, \cdots, x_n] = I$.

## 2
Let $a$ be a nonzero constant.
If $a \in I$, then $1 = (1/a) \cdot a \in I$, so $I = k[x_1, \cdots, x_n]$ by 1.

If $I = k[x_1, \cdots, x_n]$, then $1 \in I$ by 1.

## 3
$(f + g)^3 = f^3 + 3f^2g + 3fg^2 + g^3 = f \cdot f^2 + (3g)f^2 + (3f)g^2 + g(g^2)$.
Each term is in $I$, so $(f + g)^3 \in I$.

## 4
$(f + g)^{r + s - 1} = \sum_{i=0}^{r + s - 1}f^ig^{r + s - 1 - i}$.
For any $i$, $i \geq r$ or $r + s - 1 - i \geq s$ because if $i < r$ and $r + s - 1 - i < s$, then $i < r < i + 1$, which is impossible because $r, i, i + 1$ are integers.
