---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Integer Solutions to $987654319 = x^2 + y^2 + z^2$"
date:   2023-05-30
author: Hidenori
---

Exercise from P.62 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Are there integer solutions to $987654319 = x^2 + y^2 + z^2$

No.

By checking $(4n + k)^2 \pmod 8$ for each $k = 0, \cdots, 3$, it becomes obvious that $m^2 \equiv 0, 1, 4 \pmod 8$ for any $m \in \mathbb{Z}$.
However, $987654319 \equiv 319 \equiv 7 \pmod 8$.

