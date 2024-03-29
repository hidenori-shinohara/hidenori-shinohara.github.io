---
layout: post
title:  "A subvariety and the twisted cubic curve"
date:   2019-11-12
author: Hidenori
---

# Proposition
Let $C$ be the twisted cubic curve in $k^3$.
1. Show that $C$ is a subvariety of the surface $S = V(xz - y^2)$.
1. Find an ideal $J \subset k[S]$ such that $C = V_S(J)$.

# Solution

## 1
Let $f(x, y, z) = xz - y^2$.
$C = \\{ (a, a^2, a^3) \mid a \in k \\}$.
For every $(a, a^2, a^3) \in C$, $f(a, a^2, a^3) = 0$.
Therefore, $C \subset S$.

## 2
The ideal $J$ generated by $y - x^2 + \ev{xz - y^2}$ and $z - x^3 + \ev{xz - y^2}$ gives $C = V_S(J)$.
