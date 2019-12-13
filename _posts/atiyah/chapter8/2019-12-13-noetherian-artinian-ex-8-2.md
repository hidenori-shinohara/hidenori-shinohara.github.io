---
layout: post
title:  "Noetherian and Artinian rings"
date:   2019-12-13
author: Hidenori
---

# Proposition
Let $A$ be a Noetherian ring.
Prove that the following are equivalent:
1. $A$ is Artinian;
1. $\Spec(A)$ is discrete and finite;
1. $\Spec(A)$ is discrete.

# Solution
## $1 \rightarrow 2$

By Proposition 8.1[Atiyah], $\Spec(A)$ only contains maximal ideals.
By Proposition 8.3[Atiyah], $\Spec(A)$ only contains finitely many elements.
[As shown previously](/2019/12/12/spec-ex-1-18.html), a singleton of $\Spec(A)$ is closed if and only if the element is a maximal ideal.
Since a finite union of closed sets is closed, $\Spec(A)$ is closed.

## $2 \rightarrow 3$
Obvious.

## $3 \rightarrow 2$
Since $\Spec(A)$ is discrete, every element in $\Spec(A)$ is maximal [as shown previously](/2019/12/12/spec-ex-1-18.html),
In other words, every prime ideal in $\Spec(A)$ is maximal.
Suppose there exists a chain of length $\geq 1$.
Since a subsequence of a chain is also a chain, there exists a chain of length 1, $p_0 \subsetneq p_1$.
However, this is impossible because $p_0$ is a maximal ideal, so there cannot be a prime ideal containing it properly.
Hence, the dimension of $A$ is 0.
Since $A$ is Noetherian and $\dim A = 0$, $A$ is Artinian by Theorem 8.5.
