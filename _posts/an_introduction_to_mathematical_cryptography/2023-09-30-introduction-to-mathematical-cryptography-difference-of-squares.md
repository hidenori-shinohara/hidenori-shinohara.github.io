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
2. Let $c_i \equiv a_i^2 \pmod N$ for each $i$.
3. For each $i$, check if $c_i$ is a product of small primes.

So, this deserves some clarification.

First, each $a_i$ is larger than $\sqrt{N}$.
This is necessary since otherwise $c_i = a_i^2$ and that is not very interesting.
On the other hand, it doesn't make sense to pick $a_i$'s that are $\geq N$ as it would be the same as picking $a_i \pmod N$.

Second, it might seem counterproductive to factor many $c_i$'s so we can eventually factor $N$.
However, we are not trying to factor all $c_i$'s.
We are trying to factor only the $c_i$'s that only consist of small prime factors.
This can be done by, for instance, creating a list of primes less than a predefined threshold $Y$ and checking if $c_i$ is divisible by any of them.
Therefore, this process is easy.
We will later specify:

- How we pick $a_i$'s.
- What we mean by "small" prime factors.

# Finding a perfect square
Once we find many $c_i$'s, we can start thinking about a product of a subset of $c_i$'s.
More specifically, $c_{i_1} c_{i_2} \cdots c_{i_n}$ for some $i_1 < \cdots < i_n$.
We specifically want a product such that every prime appearing in the product appears to an even power.
Then such a product will be a perfect square.
Let $b$ be chosen such that $b^2 = c_{i_1} c_{i_2} \cdots c_{i_n}$.

We will later specify how many $c_i$'s is enough.

# Finding the other perfect square
This step is easy.
Let $a = a_{i_1} a_{i_2} \cdots a_{i_n}$.
Then we now have $a^2 = b^2 \pmod N$ as $a_{i_j}^2 = c_{i_j}$ for each $j$.

Then we calculate $\gcd(N, a - b)$ and $\gcd(N, a + b)$ and hope one of them will give us a nontrivial factor.

TODO: Add clarification
