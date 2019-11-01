---
layout: post
title:  "Ideals, leading terms and leading monomials"
date:   2019-11-01
author: Hidenori
---

# Proposition
If $I \subset k[x_1, \cdots, x_n]$ is an ideal, prove that $\ev{ \LT(g) \mid g \in I \setminus \\{ 0 \\} } = \ev{ \LM(g) \mid g \in I \setminus \\{ 0 \\} }$.

# Solution
Let $T = \ev{ \LT(g) \mid g \in I \setminus \\{ 0 \\} }, M = \ev{ \LM(g) \mid g \in I \setminus \\{ 0 \\} }$.

Let $\LT(g) \in T$.
Then $\LT(g) = (1/\LC(g)) \cdot \LM(g) \in M$.

Let $\LM(g) \in M$.
Let $\LM(g) = \LC(g) \cdot \LT(g) \in T$.
