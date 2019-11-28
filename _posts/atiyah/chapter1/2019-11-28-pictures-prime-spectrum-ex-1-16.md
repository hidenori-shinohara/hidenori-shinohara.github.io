---
layout: post
title:  "Pictures of $\\Spec$"
date:   2019-11-28
author: Hidenori
---

# Proposition
Draw pictures of $\Spec(\mathbb{Z}), \Spec(\mathbb{R}), \Spec(\mathbb{C}[x]), \Spec(\mathbb{R}[x]), \Spec(\mathbb{Z}[x])$.

# Solution

I am not sure how to draw pictures of these spaces, so I will just describe them in words.

## $\Spec(\mathbb{Z})$
$\Spec(\mathbb{Z}) = \\{ (0) \\} \cup \\{ (p) \mid p \text{ prime} \\}$.

Let $E \subset \mathbb{Z}$.
If $E$ is empty or $E = \\{ 0 \\}$, $V(E) = \Spec(\mathbb{Z})$.

Let $p$ be a prime number.

* If there exists $x \in E$ such that $p \nmid x$, then $E \not\subset (p)$.
* If $\forall x \in E, p \mid x$, then $E \subset (p)$.

Thus this is a necessary and sufficient condition for $(p)$ to be in $V(E)$.
Since $E$ contains a nonzero element, $V(E)$ must be finite.

On the other hand, given primes $p_1, \cdots, p_n$, $V(\\{ p_1p_2 \cdots p_n \\}) = \\{ (p_1), \cdots, (p_n) \\}$.

Therefore, all closed sets in $\Spec(\mathbb{Z})$ are:

* any finite set of the form $\\{ (p_1), \cdots, (p_n) \\}$,
* $\\{ (0) \\}$, 
* $\Spec(\mathbb{Z})$.
