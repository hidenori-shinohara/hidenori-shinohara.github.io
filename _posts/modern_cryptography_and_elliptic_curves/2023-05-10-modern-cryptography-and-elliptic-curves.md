---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Rational Points on $x^2 + y^2 = 3$"
date:   2023-05-10
author: Hidenori
---

Exercise from P.16 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Show that $x^2 + y^2 = 3$ has no rational solutions.


Assume there is.
Then there must exist $(x, y) = (a/c, b/c)$ where $a, b, c \in \mathbb{N}$ and $\text{gcd}(a, b, c) = 1$.

Then $a^2 + b^2 = 3c^2$.

By examining the remainder of squares of integers, it is clear that $a$ and $b$ are both divisible by 3.

However, that implies $a^2 + b^2$ is divisible by 9, which implies $c^2$ must be divisible by $9 / 3 = 3$.

Then this contradicts $\text{gcd}(a, b, c) = 1$.

