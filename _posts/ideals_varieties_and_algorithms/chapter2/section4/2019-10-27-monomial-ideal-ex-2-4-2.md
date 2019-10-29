---
layout: post
title:  "Basic property of a monomial ideal"
date:   2019-10-29
author: Hidenori
---

# Proposition
Let $I$ be a monomial ideal and $f \in k[x_1, \cdots, x_n]$.
If $f \in I$, then every term of $f$ lies in $I$.

# Solution
By the definition of a monomial ideal, there is a subset $A \subset \mathbb{Z}^n_{\geq 0}$ such that $I$ consists of all polynomials which are finite sums of the form $\sum_{\alpha \in A} h_{\alpha} x^{\alpha}$, where $h_{\alpha} \in k[x_1, \cdots, x_n]$.

Thus $f = h_{\alpha_1}x^{\alpha_1} + \cdots + h_{\alpha_n}x^{\alpha_n}$ for some $\alpha_i, h_{\alpha_i}$.
For each $i$, $\sum_{\alpha \in A} g_{\alpha}x^{\alpha} \in I$ where $g_{\alpha_i} = h_{\alpha_i}$ and $g_{\alpha} = 0$ when $\alpha \ne \alpha_i$.
Therefore, each term of $f$ lies in $I$.
