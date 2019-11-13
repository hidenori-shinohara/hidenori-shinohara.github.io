---
layout: post
title:  "Sufficient condition for a homomorphism to map an ideal to an ideal"
date:   2019-11-13
author: Hidenori
---

# Proposition
Suppose that $k$ is a field and $\phi: k[x_1, \cdots, x_n] \rightarrow k[x_1]$ is a ring homomorphism that is the identity on $k$ and maps $x_1$ to $x_1$.
Given an ideal $I \subset k[x_1, \cdots, x_n]$, prove that $\phi(I) \subset k[x_1]$ is an ideal.

# Solution
Since $\phi$ is a ring homomorphism, $\phi(I)$ is an additive subgroup of $k[x_1]$.
Let $f \in k[x_1]$.
Then $f$ is a polynomial in $x_1$.
$f$ can be seen as an element of $k[x_1, \cdots, x_n]$, and moreover, $\phi(f) = f$.
Since $I$ is an ideal, $fI \subset I$.
Then $f\phi(I) = \phi(f)\phi(I) = \phi(fI) \subset \phi(I)$, so $\phi(I)$ is indeed an ideal.

