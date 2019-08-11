---
layout: post
title:  "In a convex set, two continuous maps that agree on $A$ are homotopic relative to $A$."
date:   2019-08-11
author: Hidenori
---

# Proposition
Let $B \subset \mathbb{R}^n$ be any convex set, $X$ be any topological space, and $A$ be any subset of $X$.
Show that any two continuous maps $f, g: X \rightarrow B$ that agree on $A$ are homotopic relative to $A$.

# Solution
We claim that the straight-line homotopy $F(x, t) = f(x) + t(g(x) - f(x))$ is actually a homotopy relative to $A$.

* It makes sense to consider the straight-line homotopy since $B$ is a convex set.
* $\forall x \in A, \forall t \in I, F(x, t) = f(x) + t(g(x) - f(x)) = f(x) + 0 = f(x)$ since $f, g$ agree on $A$.
  Therefore, $f\mid_A = g\mid_A$.

Thus $f$ and $g$ are homotopic relative to $A$.
