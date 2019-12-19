---
layout: post
title:  "Polynomial rings of prime and maximal ideals"
date:   2019-12-19
author: Hidenori
---

# Proposition
Let $p$ be a prime ideal in $A$.
Show that $p[x]$ is a prime ideal in $A[x]$.
If $m$ is a maximal ideal in $A$, is $m[x]$ a maximal ideal in $A[x]$?

# Solution
Let $a(x) = a_nx^n + \cdots + a_0, b(x) = b_mx^m + \cdots + b_0 \in A[x]$.
Suppose $a(x)b(x) \in p[x]$.
If $a(x) \in p[x]$ or $b(x) \in p[x]$, we are done.
Suppose $a(x) \notin p[x]$ and $b(x) \notin p[x]$.
Let $k, l$ be smallest integers such that $a_{n - k} \notin p$ and $b_{m - l} \notin p$.

Then the coefficient of $x^{n + m - (k + l)}$ is $\sum_{i=0}^{k + l} a_{n - i}b_{m  - (k + l - i)}$.
(Some of the indices may be negative, and they should simply be ignored.)

* When $i < k$, $a_{n - i}b_{m - (k + l - i)} \in p$ because $a_{n - i} \in p$.
* When $i > k$, $a_{n - i}b_{m - (k + l - i)} \in p$ because $b_{m - (k + l - i)} \in p$.

Since $p$ is closed under addition and subtraction, $a_{n - k}b_{m - l} \in p$.
Since $p$ is a prime ideal, $a_{n - k} \in p$ or $b_{m - l} \in p$, which is a contradiction.

Let $m = (2) \subset \mathbb{Z} = A$.
Then $m$ is a maximal ideal in $\mathbb{Z}$.
However, $m[x]$ is not a maximal ideal in $A[x]$ because $m[x] \subsetneq (x, 2) \subsetneq \mathbb{Z}[x]$.
