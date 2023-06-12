---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Chinese Remainder Theorem ($r = 2$)"
date:   2023-06-12
author: Hidenori
---

Exercise from P.71 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Let $m, n > 1$ be coprime integers, and let $a, b$ be arbitrary integers.
  Then the following system of congruences has a unique solution modulo $mn$.

$$
 \begin{align*}
    x &\equiv a \pmod m \\
    x &\equiv b \pmod n
 \end{align*}
$$

First, we will show that, if there exist solutions, it will be unique up to modulo $mn$.
Let $k, l$ be such solutions.
Then $k \equiv l \pmod n$, so $m \mid (k - l)$.
Similarly, $n \mid (k - l)$.
Since $m$ and $n$ are coprime, $mn \mid (k - l)$.
In other words, $k \equiv l \pmod{mn}$.

Now, we will show the existence of a solution.
Since $\gcd(m, n) = 1$, $pm + qn = 1$ for some $p, q$.
We claim that $bpm + aqn$ is a solution.
$bpm + aqn \equiv aqn \equiv a(1 - pm) \equiv a \pmod m$.
The same argument can be applied for $\pmod n$.

