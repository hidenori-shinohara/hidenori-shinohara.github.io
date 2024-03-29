---
layout: post
title:  "Basic properties of Boolean rings"
date:   2019-11-30
author: Hidenori
---

# Proposition
A ring $A$ is Boolean if $x^2 = x$ for all $x \in A$.
In a Boolean ring $A$, show that

1. $2x = 0$ for all $x \in A$;
1. every prime ideal $p$ is maximal, and $A/p$ is a field with two elements;
1. every finitely generated ideal in $A$ is principal.

# Solution
## 1
$(x + x)^2 = 4x^2 = 4x$, and $(x + x)^2 = x + x = 2x$.
Thus $2x = 0$.

## 2
Let $p$ be a prime ideal.
Let $x \in A \setminus p$.
$x(1 - x) = x - x^2 = x - x = 0$.
Thus $x(1 - x) \in p$ and $p$ is a prime ideal not containing $x$.
Therefore, $1 - x \in p$.
This implies that $p + \ev{x}$ contains $1 = (1 - x) + x$.
Therefore, $p + \ev{x}$ is a maximal ideal, so there exists no proper ideal of $A$ containing $p$ properly.
Thus $p$ is a maximal ideal.

## 3
Let $\ev{x_1, x_2} \subset A$ be given.
Then $x_1 + x_2 + x_1x_2 \in \ev{x_1, x_2}$.
On the other hand,

* $x_1(x_1 + x_2 + x_1x_2) = x_1^2 + x_1x_2 + x_1^2x_2 = x_1 + x_1x_2 + x_1x_2 = x_1$.
* $x_2(x_1 + x_2 + x_1x_2) = x_2x_1 + x_2^2 + x_1x_2^2 = x_2 + 2x_1x_2 = x_2$.

Therefore, $\ev{x_1, x_2} \subset \ev{x_1 + x_2 + x_1x_2}$.
Hence, $\ev{x_1, x_2} = \ev{x_1 + x_2 + x_1x_2}$.

It is clear that this can be extended to an ideal generated by $n$ elements for any finite $n$ by using mathematical induction.
