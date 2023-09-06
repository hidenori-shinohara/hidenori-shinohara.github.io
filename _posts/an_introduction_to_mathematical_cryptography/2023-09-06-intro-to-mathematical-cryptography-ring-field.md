---
layout: post
title:  "A finite, commutative ring with multiplicative identity and no zero divisors is a field"
date:   2023-09-06
author: Hidenori
---

Let $R = \\{ b_0, b_1, \cdots, b_n \\}$ be such a ring where $b_0 = 0$ and $b_1 = 1$.

If $n = 1$, we are done.

Suppose otherwise.
All we need to show that each $b_i$ has a multiplicative inverse.


Let $i = 2, \cdots, n$ be given.

Set $f_i: b_j \mapsto b_i b_j$.

Suppose that for some $j, k = 1, \cdots, n$, $b_ib_j = b_ib_k$.
This implies $b_i(b_j - b_k) = 0$, so $b_j - b_k = 0$.

Therefore, $f_i$ maps $\\{ b_1, \cdots, b_n \\}$ into itself.

This implies that $b_i b_j = b_1 = 1$ for some $j$.
We were able to find the multiplicative inverse for any arbitrary non-zero element.
Therefore, $R$ is indeed a field.

