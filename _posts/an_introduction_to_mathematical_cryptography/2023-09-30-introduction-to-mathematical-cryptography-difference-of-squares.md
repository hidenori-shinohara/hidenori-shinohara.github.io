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

# Time Complexity Analysis (Step 1)

There are a few assumptions that we make implicitly.
We mentioned earlier that we want numbers with only small prime factors.
They're called [$B$-smooth numbers](https://en.wikipedia.org/wiki/Smooth_number).
Let $B$ be chosen.

1. We assume that, given $i$, the probability that $c_i$ is a $B$-smooth number is $\psi(N, B) / N$.
   I believe that this is a rough estimate and this could use a careful analysis.
   For instance, each $c_i$ is a quadratic residue, and the book says nothing about the connection between quadratic residues and $B$-smooth numbers.
   Maybe we're being hopeful.
   Or maybe the topic is too advanced to cover in this book.
1. We need $\pi(B) + 1$ $c_i$'s to find a perfect square.
   As discussed in the book, $c_i$'s form a system of linear equations where the number of rows is the number of $c_i$'s we have and the number of columns corresponds to $\pi(B)$.
   Once we have more rows than columns, we can guarantee that there's a nontrivial linear combination that equals 0.
   For simplicity, we will say that we need $\pi(B)$ $c_i$'s.

How do we choose such $B$?
Let $L(X) = e^{\sqrt{(\ln X)(\ln \ln X)}}$ and $B = L(N)^{1 / \sqrt{2}}$.
TODO: Finish this!

# Time Complexity Analysis (Step 2)
TODO: Finish this!








