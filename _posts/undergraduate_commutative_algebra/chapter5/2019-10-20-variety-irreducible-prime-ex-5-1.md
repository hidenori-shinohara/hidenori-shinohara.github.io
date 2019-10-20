---
layout: post
title:  "A variety $X$ is irreducible if $I(X)$ is prime."
date:   2019-10-20
author: Hidenori
---

# Proposition
A variety $X$ is irreducible if $I(X)$ is prime.

# Solution
Let a variety $X$ be given.
Suppose that $I(X)$ is a prime ideal.
Let $X_1, X_2$ be two varieties such that $X = X_1 \cup X_2$.
If $X_1 = X$ or $X_2 = X$, we are done.
Suppose otherwise.
Let $I_1 = I(X_1)$ and $I_2 = I(X_2)$.

* $X_1 = \\{ p \in k^n \mid \forall f \in A, f(p) = 0 \\}$.
  If every $f \in I_1$ vanishes on $X$, then $X \subset X_1$.
  Since we assume that $X \ne X_1$, there exists $f_1 \in I_1$ such that $f_1$ does not vanish on $X$.
  $f_1$ obviously vanishes on $X_1$ because $f_1 \in I_1$.
* Similarly, there exists $f_2 \in I_2$ such that $f_2$ does not vanish on $X$.
  $f_2$ obviously vanishes on $X_2$ because $f_2 \in I_2$.

Consider $f = f_1f_2$.
Let $p \in X$.
If $p \in X_1$, then $f(p) = f_1(p)f_2(p) = 0 \cdot f_2(p) = 0$.
If $p \in X_2$, then $f(p) = f_1(p)f_2(p) = f_1(p) \cdot 0 = 0$.
Thus $f$ vanishes on $X$.
$f \in I(X)$, but $f_1 \notin I(X)$ and $f_2 \notin I(X)$ because they do not vanish on $X$.
This is a contradiction because $I(X)$ is a prime ideal.
Therefore, $X$ must be irreducible.
