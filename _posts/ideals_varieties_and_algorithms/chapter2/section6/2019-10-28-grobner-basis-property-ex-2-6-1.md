---
layout: post
title:  "Basic property of a Grobner basis"
date:   2019-10-28
author: Hidenori
---

# Proposition
Fix a monomial ordering and let $I \subset k[x_1, \cdots, x_n]$.
Suppose that $f \in k[x_1, \cdots, x_n]$.

1. Show that $f$ can be written in the form $f = g + r$ where $g \in I$ and no term of $r$ is divisible by any element of $\LT(I)$.
1. Given two expressions $f = g + r = g' + r'$ as in part (1), prove that $r = r'$.
   Thus, $r$ and $g$ are uniquely determined.

# Solution

## 1

By Proposition 1 on P.83 of Ideals, Varieties and Algorithms, we know the existence of $g \in I, r$ such that

* $g \in I$.
* $f = g + r$.
* No term of $r$ is divisible by any of $\LT(g_i)$.

Let $t$ be a term of $r$.
Let $h \in \LT(I)$.
Then $h$ is a monomial in $\ev{ \LT(g_1), \cdots, \LT(g_n) }$, so $h = c\LT(g_i)$ for some nonzero $c \in k$ and some $i$.
Since $\LT(g_i)$ does not divide $t$, neither does $h$.
Therefore, no term of $r$ is divisible by any element of $\LT(I)$.

## 2

Let $f = g + r = g' + r'$ as in Part 1.
Then no term of $r, r'$ is divisible by any of $\LT(g_1), \cdots, \LT(g_n)$.
Thus $r = r'$ by the same proposition.
