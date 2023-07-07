---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Curve with no rational point"
date:   2023-07-07
author: Hidenori
---

Exercise from P.164 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Show that $x^2 + y^2 = 3$ has no rational points, even in $\mathbb{P}^2(\mathbb{Q})$.

Suppose there is.
Let $(a / b, c / d)$ with $\gcd(a, b) = \gcd(c, d) = 1$ be a point on it.
Without loss of generality, $b, d \geq 1$.
Then $(ad)^2 + (bc)^2 = 3(bd)^2$.

Then $d \mid bc$, so $d \mid b$. Similarly, $b \mid d$.
Therefore, $b = d = 1$.

Let us re-write the notation such that the solution is $(a / c, b / c)$ with $\gcd(a, b) = \gcd(a, c) = 1$.

Then we have $a^2 + b^2 = 3c^2$.

As squares of integers are congruent to 0 or 1 modular 3, both $a$ and $b$ must be divisible by 3.
This means the left hand side is divisible by 9, so $c$ must be divisible by 3 also.
This contradicts $\gcd(a, b) = 1$.
