---
layout: post
title:  "Necessary and sufficient conditions for $A/\\mathfrak{R}$ to be a field"
date:   2019-11-27
author: Hidenori
---

# Proposition
Let $A$ be a ring, $\mathfrak{R}$ its nilradical.
Show that the following are equivalent:
1. $A$ has exactly one prime ideal;
1. every element of $A$ is either a unit or nilpotent;
1. $A/\mathfrak{R}$ is a field.

# Solution

By Proposition 1.8[Atiyah], $\mathfrak{R}$ is the intersection of all the prime ideals of $A$.
We will use this property in the following solution without explicitly mentioning it.
We will assume that $A \ne (0)$.

## $1 \implies 2$
Suppose $A$ has only one prime ideal, $p$.
Then $\mathfrak{R} = p$.

Since every maximal ideal is prime, $A$ is a local ring.
Then $p$ is its maximal ideal.
Let $x \in A$ be given.
Suppose that $x$ is not a unit.
By Corollary 1.5[Atiyah], $x$ is in some maximal ideal.
Since the only maximal ideal in $A$ is $p$, $x \in p = \mathfrak{R}$.
By definition, $\mathfrak{R}$ is the set of all nilpotent elements.
Thus $x$ must be a nilpotent element.

## $2 \implies 3$
Let $x + \mathfrak{R} \in A / \mathfrak{R}$.
Suppose $x + \mathfrak{R} \ne 0$.
In other words, $x \notin \mathfrak{R}$.
Since $x$ is the set of all nilpotent elements, $x$ must be a unit.
Then $x^{-1} \in A$, so $(x^{-1} + \mathfrak{R})(x + \mathfrak{R}) = 1 + \mathfrak{R} = 1 \in A / \mathfrak{R}$.
Therefore, $A / \mathfrak{R}$ is a field.

## $3 \implies 1$
Let $p \subset A$ be a prime ideal.
Then $\mathfrak{R} \subset p$.
If we can show that $\mathfrak{R} = p$, then it implies that $\mathfrak{R}$ is the only prime ideal in $A$.
Let $I = \\{ x + \mathfrak{R} \mid x \in p \\}$ be an ideal in $A / \mathfrak{R}$.
By Proposition 1.2[Atiyah], $I = (0)$ or $(1)$.
Let $y \in A \ p$ and $x \in p$.
Then $y - x \notin p$.
Therefore, $y - x \notin \mathfrak{R}$.
This implies $y + \mathfrak{R} \ne x + \mathfrak{R}$, so $y + \mathfrak{R} \notin I$.
Thus $I \ne (1)$.

Since $I = (0)$, $p \subset \mathfrak{R}$, so $p = \mathfrak{R}$.
