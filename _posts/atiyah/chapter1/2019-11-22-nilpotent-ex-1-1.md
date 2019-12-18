---
layout: post
title:  "$1 + x$ is a unit if $x$ is a nilpotent element"
date:   2019-11-22
author: Hidenori
---

# Proposition
Let $x$ be a nilpotent element of a ring $A$.
Show that $1 + x$ is a unit of $A$.
Deduce that the sum of a nilpotent element and a unit is a unit.

# Solution
Let $x$ be a nilpotent element and $x^n = 0$ for some $n \in \mathbb{N}$.
Then $(1 + x)(1 - x + x^2 - x^3 + \cdots + (-x)^n) = 1 + (-x)^n = 1 + (-1)^n \cdot 0 = 1$.
Therefore, $1 + x$ is a unit.

Let $a$ be a unit.

$$
\begin{align*}
  (a + x)(\sum_{i=0}^{n-1} a^i(-x)^{n-1-i})
    &= \sum_{i=0}^{n-1} a^{i+1}(-x)^{n-1-i}
       + \sum_{i=0}^{n-1} a^{i+1}x(-x)^{n-1-i} \\
    &= \sum_{i=1}^{n} a^{i}(-x)^{n-i}
       - \sum_{i=0}^{n-1} a^{i+1}(-x)^{n-i} \\
    &= -(-x)^n + (\sum_{i=1}^{n-1} a^{i}(-x)^{n-i}) + a^n \\
    &= a^n
\end{align*}
$$

Therefore, $(a + x)(\sum_{i=0}^{n-1} a^i(-x)^{n-1-i})/a^n = 1$, so $a + x$ is a unit.

(Alternative solution for the second part)
Let $a$ be a unit and $x$ be a nilpotent element with $x^n = 0$ for some $n \in \mathbb{N}$.
Then $x / a$ is nilpotent, so $1 + x / a$ is a unit.
Thus $a(1 + x / a) = a + x$ is a unit.
