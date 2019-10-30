---
layout: post
title:  "Any real variety can be defined by a single equation"
date:   2019-10-30
author: Hidenori
---

# Proposition
$\mathbf{V}(y - x^2, z - x^3)$ is the twisted cubic in $\mathbb{R}^3$.

1. Show that $\mathbf{V}((y - x^2)^2 + (z - x^3)^2)$ is also the twisted cubic.
1. Show that any variety $\mathbf{V}(I) \subset \mathbb{R}^n, I \subset \mathbb{R}[x_1, \cdots, x_n]$, can be defined by a single equation.

# Solution

## 1
A point $(x, y, z) \in \mathbb{R}^3$ vanishes on $\\{ y - x^2, z - x^3 \\}$ if and only if it vanishes on $\\{ (y - x^2)^2 + (z - x^3)^2 \\}$.
Thus $\mathbf{V}((y - x^2)^2 + (z - x^3)^2)$ is also the twisted cubic.

## 2
By Theorem 4 (Hilbert Basis Theorem) (P.77, Ideals, Varieties and Algorithms), $I$ has a finite generating set $\\{ g_1, \cdots, g_k \\}$.
Then $\mathbf{V}(I) = \mathbf{V}(g_1^2 + \cdots + g_k^2)$ for the same reason as 1.
