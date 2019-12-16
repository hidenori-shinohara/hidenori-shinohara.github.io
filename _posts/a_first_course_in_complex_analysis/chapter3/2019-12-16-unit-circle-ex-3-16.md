---
layout: post
title:  "Unit circle and a Mobius transformation"
date:   2019-12-16
author: Hidenori
---

# Proposition
Let $\gamma$ be the unit circle.
Find a Mobius transformation that transforms $\gamma$ onto $\gamma$ and transforms $0$ to $1/2$.

# Solution
[We will use the formula given here.](https://math.stackexchange.com/questions/209308/can-we-characterize-the-möbius-transformations-that-maps-the-unit-disk-into-itse)

$f(z) = (z - 1/2) / (1 - z/2)$ maps $\gamma$ onto $\gamma$ and sends 1/2 to 0.
It suffices to take the inverse.
Therefore, the answer is $g(z) = (2z - 1) / (-z + 2)$.
