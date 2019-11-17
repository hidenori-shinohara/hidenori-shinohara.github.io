---
layout: post
title:  "An ideal contained in the radical of another ideal"
date:   2019-11-17
author: Hidenori
---

# Proposition
Let $I, J$ be ideals in $k[x_1, \cdots, x_n]$ and suppose that $I \subset \sqrt{J}$.
Show that $I^m \subset J$ for some integer $m > 0$.

# Solution
By the Hilbert Basis Theorem, $I = \ev{f_1, \cdots, f_l}$ for some $f_i$.
Since $I \subset \sqrt{J}$, we have $m_i \geq 1$ such that $f_i^{m_i} \in J$ for each $i$.
Let $m = (\sum m_i) - l + 1$.
We claim that $I^m \subset J$.

$I^m = \ev{f_{i_1} \cdots f_{i_m} \mid i_1, \cdots, i_m \in \\{ 1, \cdots, l \\}}$.
Let $f = f_{i_1} \cdots f_{i_m} \in I^m$ be given.
Suppose that $\forall i$, the number of $f_i$ in $f$ is $\leq m_i - 1$.
Then $f$ is the product of at most $\sum (m_i - 1) = m - 1$ generators, which is a contradiction because $f$ must be the product of exactly $m$ generators.

Thus there exists $i$ such that $f$ contains at least $m_i$ $f_i$'s.
Since $f_i^{m_i} \in J$, $f \in J$.
Therefore, $I^m \subset J$ with $m \geq 1$.

