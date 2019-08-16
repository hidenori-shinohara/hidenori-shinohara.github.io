---
layout: post
title:  "Every sequence in $Y$ converges to every point of $Y$"
date:   2019-08-16
author: Hidenori
---

# Proposition
Let $Y$ be a topological space with the trivial topology.
Show that every sequence in $Y$ converges to every point of $Y$.

# Solution
Let $\\{ y_n \\}$ be a sequence in $Y$.
Let $y \in Y$ be given.
Let $U$ be a neighborhood of $Y$.
Since $Y$ has the trivial topology, $U$ is either empty or $Y$.
Since $y \in U$, $U \ne \emptyset$.
Therefore, $U = Y$.

This means that $\forall n \in N, y_n \in U$.
Thus $y_n$ converges to $y$.
