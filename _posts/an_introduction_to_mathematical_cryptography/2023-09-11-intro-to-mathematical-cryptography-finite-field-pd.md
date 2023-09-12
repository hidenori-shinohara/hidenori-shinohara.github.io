---
layout: post
title:  "The size of a finite field is always a power of a prime"
date:   2023-09-11
author: Hidenori
---

Let $\mathbb{F}$ be a finite field.

We consider the sequence $0, 1, 1 + 1, 1 + 1 + 1, \cdots$ in $\mathbb{F}$.
Since $\mathbb{F}$ is finite, we eventually have duplicates.
Furthermore, the duplicate must happen in the first $\abs{\mathbb{F}} + 1$ terms.
There are two possibilities:

- $0 = 1 + 1 + \cdots + 1$ where the RHS has at most $\abs{\mathbb{F}}$ summands.
- $1 + \cdots + 1 = 1 + 1 + \cdots + 1$ where each side has at most $\abs{\mathbb{F}}$ summands.

However, the second case implies the first case as we add the right number of $-1$.
Therefore, there exists a positive integer $m \leq \abs{\mathbb{F}}$ such that adding 1 $m$ times equals 0.
Suppose $m$ is the smallest positive integer with the property that adding 1 $m$ times gives 0.

Suppose that $m$ is a composite number such that $m = ab$ where $a$ and $b$ are both integers greater than or equal to 2.

Then $(1 + \cdots + 1)(1 + \cdots + 1) = 0$ where we multiply the sum of $a$ 1's by the sum of $b$ 1's.
By the definition of $m$, we know that adding 1 $a$ times gives a non-zero number.
Similarly, adding 1 $b$ times gives a non-zero number.
This means we found a zero divisor, which should not exist in a field.
Therefore, $m$ must be a prime.
We will call it $p$ to emphasize that it is a prime number.

We will next prove that $\mathbb{F}$ is a vector space over $\mathbb{F}_p$.
Consider $\phi: \mathbb{F}_p \times \mathbb{F} \rightarrow \mathbb{F}$ such that $\phi(a, b) = b + \cdots + b$ where the RHS adds $b$ $a$ times.
It is easy to see that this satisfies all the aximos of a vector space.
Furthermore, since $\mathbb{F}$ obviously spans the whole space, $\mathbb{F}$ is a finite-dimensional vector space.

Let $B = \\{ b_1, \cdots, b_d \\} \subset \mathbb{F}$ be a basis.
Then $\mathbb{F}$ is exactly $\\{ c_1 b_1 + \cdots + c_d b_d \mid c_i \in \mathbb{F}_p \\}$, and that means $\abs{\mathbb{F}} = p^d$.



