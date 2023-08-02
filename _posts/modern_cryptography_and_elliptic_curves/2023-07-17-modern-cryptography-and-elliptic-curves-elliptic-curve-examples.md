---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Simple Examples of Elliptic Curve Group"
date:   2023-07-17
author: Hidenori
---

Exercise from P.185 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Calculate the elliptic curve group generated by $y^2 = x^3 + 3x + 6$ over $\mathbb{F}_7$.

By substituting all possible points, it is easy to determine that $[0, 1, 0], [3, 0, 1], [6, 3, 1]$ and $[6, 4, 1]$ are the elements of the group.
Since it is a group of order 4, it must be either the Klein-4 group or $\mathbb{Z}_4$.
Since $[6, 3, 1]$ and $[6, 4, 1]$ are inverses of each other, this must be the cycic group of order 4, and $[6, 3, 1]$ is a generator.

As an example, $[3, 0, 1] \oplus [6, 3, 1] = [6, 4, 1]$ by following the formula in the textbook

