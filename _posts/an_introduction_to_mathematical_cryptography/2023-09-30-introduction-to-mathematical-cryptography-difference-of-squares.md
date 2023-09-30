---
layout: post
title:  "An Introduction to Mathematical Cryptography: Factorization via difference of squares"
date:   2023-09-30
author: Hidenori
---

This is my notes for Section 3.6 in _An Introduction to Mathematical Cryptography_.

# Underlying idea

Let $N \in \mathbb{N}$ be a large, composite number.
We can tell that it is not prime from a probabilistic primality test such as Miller-Rabin.
We would like to find a prime factor efficiently.

As everyone knows, $a^2 - b^2 = (a + b)(a - b)$.
Therefore, given a large $N$, _if_ we can find two integers $a, b$ such that $a^2 - b^2$, both $a + b$ and $a - b$ are nontrivial factors of $N$.

However, of course, randomly selecting $a, b$ until they satisfy $a^2 - b^2 = N$ is not efficient.
So, we need something better.

Furthermore, we assume $a > b$.


# Modular arithmetics

Instead of $a^2 - b^2 = N$, we will consider $a^2 - b^2 \equiv 0 \pmod N$.
Then we have $(a + b)(a - b) = kN$ for some $k \in \mathbb{Z}$.
If $N \mid a + b$ or $N \mid a - b$, we are out of luck.
We just found a multiple of $N$.
However, if $N \not\mid a + b$ and $N \not\mid a - b$, then both $\gcd(a + b, N)$ and $\gcd(a - b, N)$ will give us a nontrivial factor.

However, a very similar problem remains.
Randomly selecting $a, b$ is not going to be efficient.

# Relation building
We will perform a bunch of calculations and create a pair $(a, b)$.

Specifically, we will follow these steps:

1. Pick $a_1, a_2, \cdots$. Each of them must be in $(\sqrt{N}, N)$.
2. Let $c_i \equiv a_i^2 (\pmod N)$ for each $i$.
3. For each $i$, check if $c_i$ is a product of small primes.

So, this deserves some clarification.

First, each $a_i$ is larger than $\sqrt{N}$.
This is necessary since otherwise $c_i = a_i^2$ and that is not very interesting.

Second, it might seem counterproductive to factor many $c_i$'s so we can eventually factor $N$.
However, we are not trying to factor all $c_i$'s.
We are trying to factor only the $c_i$'s that only consist of small prime factors.
This can be done by, for instance, creating a list of primes less than a predefined threshold $Y$ and checking if $c_i$ is divisible by any of them.
Therefore, this process is easy.
We will later specify:

- How we pick $a_i$'s.
- What we mean by "small" prime factors.


TODO: Finish this article



