---
layout: post
title:  "A prime ideal that contains the intersection of $n$ ideals"
date:   2019-11-18
author: Hidenori
---

# Proposition
Let $I_1, \cdots, I_n$ be ideals and $P$ a prime ideal containing $\cap_{i=1}^{n} I_i$.
Then prove that $P \supset I_i$ for some $i$.
Further, if $P = \cap_{i=1}^{n} I_i$, show that $P = I_i$ for some $i$.

# Solution
Suppose $n = 2$.
Then we want to show that $I_1 \cap I_2 \subset P$ implies $I_1 \subset P$ or $I_2 \subset P$.
Suppose otherwise.
Let $x \in I_1 \setminus P$ and $y \in I_2 \setminus P$.
Then $xy \in I_1 \cap I_2$ because $I_1, I_2$ are ideals.
This implies that $xy \in P$ but $x \notin P$ and $y \notin P$.
This is a contradiction.

Suppose that we have proved the proposition for $n \geq 2$.
We will prove the case with $n + 1$ ideals.

Then $\cap_{i=1}^{n + 1} = (\cap_{i=1}^{n} I_i) \cap I_{n + 1}$.
Since the intersection of $n$ ideals is also an ideal, $\cap_{i=1}^{n} I_i \subset P$ or $I_{n + 1} \subset P$ by the argument for $n = 2$.
If $I_{n + 1} \subset P$, we are done.
If $\cap_{i=1}^{n} I_i \subset P$, then by the inductive hypothesis, $I_i \subset P$ for some $1 \leq i \leq n$.

By mathematical induction, the proposition is true for all $n \geq 2$.

TODO(Second part)
