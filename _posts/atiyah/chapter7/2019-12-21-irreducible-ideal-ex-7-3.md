---
layout: post
title:  "When are irreducible ideals primary?(WIP)"
date:   2019-12-20
author: Hidenori
---

# Proposition
Let $a$ be an irreducible ideal in a ring $A$.
Then the following are equivalent:
1. $a$ is primary;
1. for every multiplicatively closed subset $S$ of $A$ we have $(S^{-1}a)^{c} = (a:x)$ for some $x \in S$;
1. the sequence $(a:x^n)$ is stationary, for every $x \in A$.

# Solution
## $1 \implies 2$
Let $p = r(a)$.

1. Suppose $S \cap p = \emptyset$.
   Then $(S^{-1}a)^c = a$ by Proposition 4.8 [Atiyah].
   Since $S \cap p = \emptyset$, $1 \notin p$.
   $(a:1) = a$ by Lemma 4.4 [Atiyah].
   Therefore, $(S^{-1}a)^c = (a:1)$ where $1 \in S$.
1. Suppose $S \cap p \ne \emptyset$.
   Proposition 4.8 [Atiyah] implies $(S^{-1}a)^c = (S^{-1}A)^c = A$.
   Let $x \in S \cap p$.
   Then $x \in p$, so $x^n \in q$ for some $n \in \mathbb{N}$.
   Therefore, $A = (a:x^n)$ by Lemma 4.4.
   Since $S$ is multiplicatively closed, $x^n \in S$.
   Thus we have $(S^{-1}a)^c = A = (a:x^n)$ with $x^n \in S$.

## $2 \implies 3$
TODO

## $3 \implies 1$
TODO

