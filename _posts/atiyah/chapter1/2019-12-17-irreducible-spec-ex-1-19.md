---
layout: post
title:  "$\\Spec(A)$ is irreducible if and only if the nilradical of $A$ is prime(WIP)"
date:   2019-12-17
author: Hidenori
---

# Proposition
Show that $\Spec(A)$ is irreducible if and only if the nilradical of $A$ is a prime ideal.

# Solution
Let $\mathfrak{R}$ denote the nilradical of $A$.
Let $a, b \in A$.
Suppose that $ab \in \mathfrak{R}$.
We will show that $a \in \mathfrak{R}$ or $b \in \mathfrak{R}$.

* Case 1: $V(\\{ a \\})^c$ is empty. 
  Then $V(\\{ a \\}) = \Spec(A)$, so every prime ideal contains $a$.
  Thus $a \in \mathfrak{R}$.
* Case 2: $V(\\{ b \\})^c$ is empty. 
  Similarly, $b \in \mathfrak{R}$.
* Case 3: Neither $V(\\{ a \\})^c$ nor $V(\\{ b \\})^c$ is empty.
  Then $V(\\{ a \\})^c \cap V(\\{ b \\})^c \ne \emptyset$
  Thus there exists $x \in \Spec(A)$ such that $x \notin V(\\{ a \\})$ and $x \notin V(\\{ b \\})$.
  This implies $a \notin p_x$ and $b \notin p_x$.
  This is a contradiction because $ab \in \mathfrak{R} \subset p_x$.
  Therefore, this case is not possible.

Therefore, if $\Spec(A)$ is irreducible then the nilradical is prime.

TODO: Show the other direction.
