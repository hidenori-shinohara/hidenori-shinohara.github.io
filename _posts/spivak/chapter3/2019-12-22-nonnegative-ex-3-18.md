---
layout: post
title:  "The support of a non-negative function has measure 0 if $\\int_A f = 0$"
date:   2019-12-22
author: Hidenori
---

# Proposition
If $f: A \rightarrow \mathbb{R}$ is non-negative and $\int_A f = 0$, show that $\\{ x : f(x) \ne 0 \\}$ has measure 0.

## Solution
Let $n \in \mathbb{N}$ be given.
We will show that $\\{ x : f(x) > 1 / n \\}$ has content 0.
Let $\epsilon > 0$ be given.
Since $\inf \\{ U(f, P) \\} = 0$, there exists a partition $P$ such that $U(f, P) < \epsilon / n$.
Let $S_1, \cdots, S_k$ denote the subrectangles in which $f$ achieves a value higher than $1 / n$.
Note that there are only finitely many subrectangles because a partition must only contain finitely many subrectangles.

Since $f$ is non-negative, $M_S \geq 0$ for each subrectangle $S$.
Thus $U(f, P) \geq \sum v(S_i) / n$, so $\sum v(S_i) \leq n U(f, P) < \epsilon$.

Therefore, $S_1, \cdots, S_k$ form a finite cover of $\\{ x : f(x) > 1 / n \\}$ by closed rectangles such that the total volume is less than $\epsilon$.
Thus $\\{ x : f(x) > 1 / n \\}$ has content 0.

Since $n$ was chosen arbitrarily, $\\{ x : f(x) > 1 / n \\}$ has content 0 for any $n \in \mathbb{N}$.
We will use this to show that $\\{ x : f(x) \ne 0 \\}$ has measure 0.
Since $f$ is non-negative, it suffices to show that $\\{ x : f(x) > 0 \\}$ has measure 0.

Let $\epsilon > 0$ be given.

For each $n \in \mathbb{N}$, let $C_n$ denote a finite cover of $\\{ x : f(x) > 1 / n \\}$ by closed rectangles such that the total volume is less than $\epsilon / 2^n$.
This is always possible because each $\\{ x : f(x) > 1 / n \\}$ has content 0.

Let $C = \bigcup_{n \in \mathbb{N}} C_n$.
Then $C$ covers $\\{ x : f(x) > 0 \\}$ since for each $f(x) > 0$, there exists an $n \in \mathbb{N}$ such that $f(x) > 1 / n$.
Since the countable union of finite sets is at most countable by the diagonal argument on P.50, $C$ is countable.
Moreover, $\sum_{S \in C} v(S) = \sum_{i=1}^{n} \sum_{S \in C_i} S < \sum_{i=1}^{n} \epsilon / 2^i = \epsilon$.
(Note that the order in which we sum the volumes does not matter.
See Theorem 3.55 on P.78 of Principles of Mathematical Analysis.)
Thus we found a countable cover of $\\{ x : f(x) > 0 \\}$ by closed rectangles such that $\sum_{i=1}^{\infty} v(U_i) < \epsilon$.

Therefore, $\\{ x : f(x) > 0 \\}$ has measure 0.
