---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Classification of small Abelian groups"
date:   2023-06-28
author: Hidenori
---

Exercise from P.140 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> For $5 \leq n \leq 15$, use your knowledge of these groups to characterize them as in the Fundamental Theorem.

- $U_5 = \langle 2 \rangle \cong \mathbb{Z}_4$
- $U_6 = \langle 5 \rangle \cong \mathbb{Z}_2$
- $U_7 = \langle 3 \rangle \cong \mathbb{Z}_6$
- $U_8 = \langle 3, 5 \rangle \cong \mathbb{Z}_2 \times \mathbb{Z}_2$
- $U_9 = \langle 2 \rangle \cong \mathbb{Z}_6$
- $U_{10} = \langle 3 \rangle \cong \mathbb{Z}_4$
- $U_{11} = \langle 2 \rangle \cong \mathbb{Z}_{10}$
- $U_{12} = \langle 5, 7 \rangle \cong \mathbb{Z}_{2} \times \mathbb{Z}_2$
- $U_{13} = \langle 2 \rangle \cong \mathbb{Z}_{12}$
- $U_{14} = \langle 3 \rangle \cong \mathbb{Z}_{6}$
- $U_{15} = \langle 2, 14 \rangle \cong \mathbb{Z}_{4} \times \mathbb{Z}_2$

I solved it by:
1. Listing all the elements in the group. $U_n$ has $\phi(n)$ elements.
1. Taking powers of the smallest element until I get 1.
1. If that generates the whole group, I'm done. Otherwise, look at the elements I haven't seen.

