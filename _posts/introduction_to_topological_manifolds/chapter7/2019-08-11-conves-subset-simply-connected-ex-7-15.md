---
layout: post
title:  "Convex subsets of $\\mathbb{R}^n$ are simply connected"
date:   2019-08-11
author: Hidenori
---

# Proposition
Show that every convex subset of $\mathbb{R}^n$ is simply connected.
Conclude that $\mathbb{R}^n$ itself is simply connected.

# Solution
Let $X$ be a convex subset of $\mathbb{R}^n$.
Let $p \in X$.
Let $[f] \in \pi_1(X, p)$.
Then the straight-line homotopy $F(s, t) = f(s) + t(c_p(s) - f(s))$ shows that $f$ is path-homotopic to $\pi_1(X, p)$.
This works because $X$ is convex.
Thus $\pi_1(X, p) = \\{ [c_p] \\}$, and thus any convex subset of $\mathbb{R}^n$ is simply connected.
