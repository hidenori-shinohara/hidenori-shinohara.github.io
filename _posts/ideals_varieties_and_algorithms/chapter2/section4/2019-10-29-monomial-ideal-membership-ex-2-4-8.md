---
layout: post
title:  "Monomial ideal membership"
date:   2019-10-29
author: Hidenori
---

# Proposition
If $I = \ev{ x^{\alpha(1)}, \cdots, x^{\alpha(s)} }$ is a monomial ideal, prove that a polynomial $f$ is in $I$ if and only if the remainder of $f$ on division by $x^{\alpha(1)}, \cdots, x^{\alpha(s)}$ is zero.

# Solution
If the remainder of $f$ on division by $x^{\alpha(1)}, \cdots, x^{\alpha(s)}$ is zero, then $f = h_1x^{\alpha(1)} + \cdots + h_sx^{\alpha(s)} \in I$.

On other hand, suppose $f \in I$.
By Lemma 3 on P.71 (Ideals, Varieties and Algorithms), every term of $f$ lies in $I$.
By Lemma 2 on P.70 (Ideals, Varieties and Algorithms), every term of $f$ is divisible by some $x^{\alpha(i)}$.
Thus the remainder of $f$ on division by $x^{\alpha(1)}, \cdots, x^{\alpha(s)}$ is zero.
