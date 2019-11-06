---
layout: post
title:  "A prime ideal is radical"
date:   2019-11-06
author: Hidenori
---

# Proposition
Show that a prime ideal is radical.

# Solution
Let $P$ be a prime ideal.

Let $m = 1$.
Let $f$ be given such that $f^m \in P$.
Then $f \in P$.

Suppose that $f^m \in P \implies f \in P$ for all $f$ for some $m \geq 2$.
Let $f$ be given that $f^{m + 1} \in P$.
Then $f \in P$ or $f^{m} \in P$.
By the inductive hypothesis, $f \in P$.

By mathematical induction, $P$ is radical.
