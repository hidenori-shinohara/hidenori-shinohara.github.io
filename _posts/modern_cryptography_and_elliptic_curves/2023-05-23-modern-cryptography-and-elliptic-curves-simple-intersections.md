---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Examples of zeros with multiplicity"
date:   2023-05-23
author: Hidenori
---

Exercise from P.44 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Show that the curve $y = (x − a)^k$ intersects the $x$-axis with multiplicity $k$ at $x = a$ and with multiplicity 0 at all other points $x = b$.

The curve is the zero set of $f(x, y) = (x - a)^k - y$, and the $x$ axis is $y = g(x) = 0$.

Then $h(x) = f(x, g(x)) = f(x, 0) = (x - a)^k$.

$h(x)$ has a zero of order $k$ at $x = a$ and a zero of order 0 at $x = b$ for any $b \ne a$.
