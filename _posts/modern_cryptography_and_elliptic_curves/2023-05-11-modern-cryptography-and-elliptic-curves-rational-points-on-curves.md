---
layout: post
title:  "Rational Points on $x^n + y^n = 1$"
date:   2023-05-11
author: Hidenori
---

Exercise from P.28 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Find all of the rational points on the curve $x^n + y^n = 1 $ where $n$ is an integer, $n > 2$.

It is obvious that $(\pm 1, 0), (0, \pm 1)$ are solutions when $n$ is even and $(1, 0), (0, 1)$ are solutions when $n$ is odd.
We claim that finding non-trivial solutions is equivalent to Fermat's Last Theorem.

Any counterexample to Fermat's Last Theorem $(a, b, c, n)$ with $n > 2$ would produce a rational point $(a / c, b / c)$ to the curve $x^n + y^n = 1$.


On the other hand, suppose we have a non-trivial rational point.

Then $x, y$ can be expressed in the form of $a / c, b / c$ where $a, b, c \in \mathbb{Z}$ with $a, b \ne 0, c > 0$.

Then $a^n + b^n = c^n$.

If $n$ is even, then $(\abs{a}, \abs{b}, \abs{c}, n)$ would be a counterexample to Fermat's Last Theorem.
Suppose $n$ is odd.
If $a, b$ are both positive, then that would be a counterexample.
If $a < 0$ and $b > 0$, then $b^n = c^n + (-a)^n$, so we have a counterexample as well.
The case that $a > 0$ and $b < 0$ is similar.

Therefore, non-trivial rational points exist if and only if Fermat's Last Theorem was wrong.

Since Fermat's Last Theorem has been proven, non-trivial rational points don't exist, and also there is no elementary way to prove this.
