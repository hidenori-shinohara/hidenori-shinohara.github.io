---
layout: post
title:  "The intersection of two principal ideals is a principal ideal"
date:   2019-10-30
author: Hidenori
---

# Proposition
The intersection $I \cap J$ of two principal ideals $I = \ev{f}, J = \ev{g} \subset k[x_1, \cdots, x_n]$ is a principal ideal.

# Solution
Let $h = \lcm(f, g)$.
Then $f \mid h$ and $g \mid h$, so $\ev{h} \subset \ev{f}$ and $\ev{h} \subset \ev{g}$.
Thus $\ev{h} \subset \ev{f} \cap \ev{g}$.

Let $F \in \ev{f} \cap \ev{g}$.
Thus $f$ and $g$ divide $F$.
Since $h$ is the lowest common multiplier, $h \mid F$.
Therefore, $F \in \ev{h}$.

Therefore, $\ev{f} \cap \ev{g} = \ev{h}$.
