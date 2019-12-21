---
layout: post
title:  "Maximum and minimum of $\\abs{f(z)}$ on the closed unit disk"
date:   2019-12-21
author: Hidenori
---

# Proposition
Let $f: \mathbb{C} \rightarrow \mathbb{C}$ be given by $f(z) = z^2 - 2$.
Find the maximum and minimum of $\abs{f(z)}$ on the closed unit disk.

# Solution
* $\abs{z^2 - 2} \leq \abs{z^2} + \abs{-2} \leq 3$.
    * $\abs{f(i)} = 3$, so 3 is the maximum value.
* $\abs{2} \leq \abs{2 - z^2} + \abs{z^2}$, so $\abs{z^2 - 2} \geq \abs{2} - \abs{z^2} \geq 1$.
    * $\abs{f(1)} = 1$, so 1 is the minimum value.
