---
layout: post
title:  "An example of a congruent number"
date:   2023-05-10
author: Hidenori
---

Exercise from P.26 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Find a square-free congruent number not in the list above, and show all the work to obtain it.

Based on the discussion in the book, we know that all primitive congruent numbers can be obtained by using relatively prime $m, n$ in $(A, B, C) = (n^2 - m^2, 2mn, n^2 + m^2)$.
I picked $(m, n) = (7, 9)$ arbitrarily.

This gives us a Pythagorean triplet $(32, 126, 130)$.
Or alternatively, $(16, 63, 65)$.

Therefore, $16 \cdot 63 / 2 = 504 = 6^2 \cdot 14$.

Indeed, 14 is a square-free congruent number as the triangle $(16 / 6, 63 / 6, 65 / 6)$ has the area of $(16 / 6) \cdot (63 / 6) / 2 = 14$.
