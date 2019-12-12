---
layout: post
title:  "If $A[x]$ is Noetherian, $A$ is Noetherian"
date:   2019-12-12
author: Hidenori
---

# Proposition
If $A[x]$ is Noetherian, is $A$ necessarily Noetherian?

# Solution
Yes.

Let $\phi: A[x] \rightarrow A$ be a ring homomorphism such that $a \mapsto a$ for all $a \in A$ and $x \mapsto 1$.
This uniquely determines the homomorphism because every element in $A[x]$ is a polynomial in $x$ with coefficients in $A$.
Moreover, $\phi$ is surjective because $\forall a \in A$, the constant polynomial $a$ is in $A[x]$.

By Proposition 7.1 [Atiyah], $A$ is Noetherian.
