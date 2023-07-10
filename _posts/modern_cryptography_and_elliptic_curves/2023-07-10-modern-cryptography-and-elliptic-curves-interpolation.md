---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Interpolation"
date:   2023-07-10
author: Hidenori
---

Exercise from P.170 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Show that in contrast to the uniqueness result which Lagrange interpolation provides, there are an infinite number of polynomials of degree $n + 1$ which pass through the $n + 1$ given points.

Let $p(x)$ be the polynomial of degree $n$ that passes through all the $n + 1$ points.
Then for any nonzero $c \in \mathbb{R}$, $p(x) + c\Pi_{i}(x - a_i)$ is a polynomial of degree $n + 1$ that passes through the $n + 1$ given points.


