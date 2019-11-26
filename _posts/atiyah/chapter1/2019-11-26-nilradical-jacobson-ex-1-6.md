---
layout: post
title:  "Nilradical and Jacobson radical"
date:   2019-11-26
author: Hidenori
---

# Proposition
A ring $A$ is such that every ideal not contained in the nilradical contains a nonzero idempotent (that is, an element $e$ such that $e^2 = e \ne 0$).
Prove that the nilradical and Jacobson radical of $A$ are equal.

# Solution
When $A = (0)$, this is trivial.
Suppose $A \ne (0)$.

Let $N$ be the nilradical and $J$ be the Jacobson radical of $A$.
$N$ and $J$ are the intersections of all prime ideals and maximal ideals, respectively, so $N \subset J$ since every maximal ideal is prime.

Suppose $N \subsetneq J$.
Then $J$ must contain a nonzero idempotent, $x$.
$x$ is not a unit because $J \ne A$.

Since $x \in J$, $1 - x^2$ must be a unit in $A$ by Proposition 1.9[Atiyah].
$(1 - x^2)^2 = (1 - x)^2 = 1 - 2x + x^2 = 1 - 2x + x = 1 - x = 1 - x^2$.
Thus $(1 - x^2)^2 = (1 - x^2) \implies 1 - x^2 = 1$.
This implies that $1 - x = 1 - x^2 = 1$, so $x = 0$.
However, we chose $x$ to be a nonzero idempotent element.
This is a contradiction, so such $x$ cannot exist.

Therefore, $N = J$.
