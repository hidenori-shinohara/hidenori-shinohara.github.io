---
layout: post
title:  "Varieties and quotient ideals"
date:   2019-11-07
author: Hidenori
---

# Proposition
Let $V, W \subset k^n$ be varieties.
Prove that $I(V):I(W) = I(V \setminus W)$.

# Solution
Let $f \in I(V):I(W)$.
Then for all $g \in I(W), fg \in I(V)$.
This implies that $fg$ vanishes on $V$ for all $g \in V$.

Suppose that $f \notin I(V \setminus W)$.
Then there exits an $x \in V \setminus W$ such that $f(x) \ne 0$.
Since $f \in I(V):I(W)$, $\forall g \in I(W), fg \in I(V)$.
In other words, $\forall g \in I(W), (fg)(x) = 0$.
Since $f(x) \ne 0$, $\forall g \in I(W), g(x) = 0$.
However, this implies that $x \in W$.
This is a contradiction, so $f \in I(V \setminus W)$.
Therefore, $I(V):I(W) \subset I(V \setminus W)$.

Let $f \in I(V \setminus W)$.
Let $g \in I(W)$.
Let $x \in V$.

* If $x \in W$, then $(fg)(x) = 0$ since $g(x) = 0$.
* If $x \notin W$, then $(fg)(x) = 0$ since $f(x) = 0$.

This implies that $fg \in I(V)$, so $fI(W) \subset I(V)$, so $f \in I(V):I(W)$.
