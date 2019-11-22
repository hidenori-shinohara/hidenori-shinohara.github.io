---
layout: post
title:  "A ring in which every element satisfies $x^n = x$ for some $n$"
date:   2019-11-22
author: Hidenori
---

# Proposition
Let $A$ be a ring in which every element $x$ satisfies $x^n = x$ for some $n > 1$ (depending on $x$).
Show that every prime ideal in $A$ is maximal.

# Solution
Let $P$ be a prime ideal.
Let $x + P \in A / P$ be given.
Since $x \in A$, there exists an $n \geq 2$ such that $x^n = x$.
Then $(x + P)^n = x^n + P = x + P$.
Therefore, $0 = (x^n - x) + P = (x + P)((x^{n - 1} - 1) + P)$.
Since $A / P$ is an integral domain, it does not contain a zero divisor.
If $x + P \ne 0$, then $(x^{n - 1} - 1) + P = 0$.
In other words, $x^{n - 1} + P = 1 + P$.
This implies that $x + P$ is either 0 or a unit. 
Therefore, $A / P$ is a field, so $P$ is a maximal ideal.
