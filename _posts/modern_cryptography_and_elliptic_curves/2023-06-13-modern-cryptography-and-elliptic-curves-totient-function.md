---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Special cases of Euler's totient function"
date:   2023-06-13
author: Hidenori
---

Exercise from P.93 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Find the formula for $\phi(p^r)$ for prime $p$ and $r \geq 1$.

Let $a$ be an integer between 1 and $p^r$ such that $\gcd(a, p^r) \ne 1$.

$\gcd(a, p^r) \mid p^r$, so $\gcd(a, p^r) = p^k$ for some $k = 1, \cdots, r$.

In other words, $a$ is divisible by $p$.
On other hand, any number divisible by $p$ is not relatively prime to $p^r$ obviously.
Therefore, the set of positive integers not relatively prime to $p^r$ is exactly the set of multiples of $p$.

For this purpose, we only care about $\\{ p, 2p, \cdots, p^r \\} = \\{ 1 \cdot p, 2 \cdot p, \cdots, p^{r - 1} \cdot p \\}$.
Therefore, it is easy to see that $\phi(p^r) = p^r - p^{r - 1}$.

