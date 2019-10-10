---
layout: post
title:  "An example of ideals $I, J$ such that $I \\cup J$ is not an ideal"
date:   2019-10-10
author: Hidenori
---

# Proposition
Give an example of a ring $A$ and ideals $I, J$ such that $I \cup J$ is not an ideal;
in your example, what is the smallest ideal containing $I$ and $J$?

# Solution
Let $A = \mathbb{C}[x], I = (x + 1), J = (x)$.

$I \cup J$ contains $x$ and $x + 1$.
Since an ideal must be closed under subtraction, $x + 1 - x = 1$ must be in $I \cup J$.
However, $1 \notin I$ and $1 \notin J$.

The smallest ideal containing $I$ and $J$ is $A$ because any ideal containing $I$ and $J$ must contain $1$, and the only ideal containing $1$ is $A$.
