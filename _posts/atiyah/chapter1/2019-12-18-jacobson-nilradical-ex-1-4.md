---
layout: post
title:  "The Jacobson radical of $A[x]$ equals the nilradical"
date:   2019-12-18
author: Hidenori
---

# Proposition
In the ring $A[x]$, the Jacobson radical is equal to the nilradical.

# Solution
Since every maximal ideal is prime, $N(A[x]) \subset J(A[x])$.
Let $f \in J(A[x])$.
By Proposition 1.9[Atiyah], $1 - xf$ is a unit in $A[x]$.
[As we showed previously](/2019/12/18/ring-of-polynomials-ex-1-2.html), this implies $a_0, \cdots, a_n \in A$ are nilpotent.
Moreover, the same post implies that $a_0 + a_1x + \cdots + a_nx^n \in A[x]$ is nilpotent.
Therefore, $f \in N(A[x])$.

