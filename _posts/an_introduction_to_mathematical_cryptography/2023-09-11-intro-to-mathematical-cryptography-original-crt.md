---
layout: post
title:  "Original Chinese Remainder Theorem"
date:   2023-09-11
author: Hidenori
---

> There are certain things whose number is unknown. If we count them by threes, we have two left over; by fives, we have three left over; and by sevens, two are left over. How many things are there?

We need to solve the following system of equations:

$$
\begin{align*}
    x &\equiv 2 &\pmod 3 \\
    x &\equiv 3 &\pmod 5 \\
    x &\equiv 2 &\pmod 7
\end{align*}
$$

This should be possible as 3, 5, and 7 are relatively prime to each other.

Since $x \equiv 2 \pmod 3$, $x = 3k + 2$ for some $k$.
We have $3k + 2 \equiv 3 \pmod 5$, so $3k \equiv 1 \pmod 5$.
It is easy to see that 2 is the inverse of 3 in $\mathbb{Z}_5$, so $k = 2$.
In other words, $8 + 15l$ is an answer to the first two equations for any $l$.

Similarly, we have $8 + 15l \equiv 2 \pmod 7$.
This implies $l \equiv 1 \pmod 7$.

Therefore, we obtain the answer $23 + 105m$ where $m$ can be any integer.
