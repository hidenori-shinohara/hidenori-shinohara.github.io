---
layout: post
title:  "Properties of quotient ideals"
date:   2019-11-25
author: Hidenori
---

# Proposition
1. $a \subset (a:b)$
1. $(a:b)b \subset a$
1. $((a:b):c) = (a:bc) = ((a:c):b)$
1. $(\cap_i a_i:b) = \cap_i (a_i:b)$
1. $(a:\sum_i b_i) = \cap_i (a:b_i)$.

# Solution
## Lemma
Let $a, b, c$ be ideas.
If $\forall x \in a, xb \subset c$, then $ab \subset c$.

(Proof)
Let $\sum a_ib_i \in ab$ be given.
Then each $a_ib_i \in c$.
Since $c$ is closed under addition, $\sum a_ib_i \in c$.
Therefore, $ab \subset c$.

## 1
Let $x \in a$.
Then $\forall y \in b, xy \in a$ since $a$ is an ideal.
Then $xb \subset a$, so $x \in (a:b)$.

## 2
For all $x \in (a:b)$, $xb \subset a$.
By the Lemma above, $(a:b)b \subset a$.

## 3
Let $x \in ((a:b):c)$.
Then $xc \subset (a:b)$.
For all $xz \in xc, (xz)b \subset a$.
Therefore, $(xc)b \subset a$ by the Lemma above.
Then $x(cb) \subset a$, so $x(bc) \subset a$.
Hence, $x \in (a:bc)$.

On the other hand, suppose $x \in (a:bc)$.
Then $x(bc) \subset a$.
$x(bc) \subset a \implies (xb)c \subset a \implies xb \subset (a:c) \implies x \in ((a:c):b)$.

Therefore, $((a:b):c) = (a:bc)$.

We showed that $((a:b):c) = (a:bc)$.
This implies $(a:cb) = ((a:c):b)$.
Since $(a:bc) = (a:cb)$, we have $((a:b):c) = (a:bc) = (a:cb) = ((a:c):b)$.
