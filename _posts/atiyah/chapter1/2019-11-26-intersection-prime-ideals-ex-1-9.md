---
layout: post
title:  "$a = r(a)$ if and only if $a$ is an intersection of prime ideals"
date:   2019-11-26
author: Hidenori
---

# Proposition
Let $a$ be an ideal $\ne (1)$ in a ring $A$.
Show that $a = r(a) \iff a$ is an intersection of prime ideals.

# Solution
Suppose $a = r(a)$.
By Proposition 1.14[Atiyah], $r(a)$ is the intersection of the prime ideals containing $a$.
Therefore, $a$ is an intersection of prime ideals.

Suppose $a$ is an intersection of prime ideals.
Let $\\{ P_{\alpha} \\}$ be a collection of prime ideals such that $a = \cap_{\alpha} P_{\alpha}$.
Then $\forall \alpha, a \subset P_{\alpha}$.
Since $r(a)$ is the intersection of all the prime ideals containing $a$, $r(a) \subset \cap_{\alpha} P_{\alpha}$.

Therefore, we have $a \subset r(a) \subset \cap_{\alpha} P_{\alpha} = a$.
This implies $r(a) = a$.

The condition that $a \ne (1)$ does not seem necessary if we assume the intersection of no sets is $A$.
