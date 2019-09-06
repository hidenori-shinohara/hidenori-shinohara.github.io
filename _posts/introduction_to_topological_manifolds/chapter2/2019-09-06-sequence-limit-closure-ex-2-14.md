---
layout: post
title:  "A limit of a sequence and the closure"
date:   2019-09-05
author: Hidenori
---

# Proposition
Suppose $X$ is a topological space, $A$ is a subset of $X$, and $(x_i)$ is a sequence of points in $A$ that converges to a point $x \in X$.
Show that $x \in \overline{A}$.

# Solution
Suppose $x \notin \overline{A}$.

Then $\overline{A}^c$ is a neighborhood of $x$.
Since $x_i \rightarrow x$, there must exist an $N \in \mathbb{N}$ such that $\forall n \geq N, x_n \in \overline{A}^c$.
Since all the points of the sequence are in $A$, they are not in $\overline{A}^c$.
Therefore, no such $N$ exists.

This implies that $x$ must be in $\overline{A}$.
