---
layout: post
title:  "The set of all ideals in which every element is a zero divisor"
date:   2019-11-28
author: Hidenori
---

# Proposition
In a ring $A$, let $\Sigma$ be the set of all ideals in which every element is a zero divisor.
Show that the set $\Sigma$ has maximal elements and that every maximal element of $\Sigma$ is a prime ideal.
Hence the set of zero-divisors in $A$ is a union of prim ideals.

# Solution
By Zorn's lemma, it suffices to show that $\Sigma$ contains upper bounds for every chain.
Let $(a_{\alpha})$ be a nonempty chain in $\Sigma$ where $I$ is the index set.
Let $a = \cup_{\alpha \in I} a_{\alpha}$.

1. Is $a$ an ideal?
  * $a$ is nonempty.
  * Let $x, y \in a$.
    Then there exist $\alpha, \beta \in I$ such that $x \in a_{\alpha}$ and $y \in a_{\beta}$.
    Then $a_{\alpha} \subset a_{\beta}$ or $a_{\beta} \subset a_{\alpha}$.
    Therefore, $a_{\alpha}$ or $a_{\beta}$ contains both $x$ and $y$, so it contains $x - y$.
    Thus $x - y \in a$.
1. $a$ only contains zero divisors.

Therefore, $a \in \Sigma$, and clearly $a_{\alpha} \subset a$.
By Zorn's lemma, $\Sigma$ contains a maximal element.

Let $p$ be a maximal element in $\Sigma$.
Let $x, y \in A$.
Suppose that $x \notin p$ and $y \notin p$.
Since $p$ is a maximal element, $(x) + p$ and $(y) + p$ are not in $\Sigma$.
In other words, they both contain elements that are not zero divisors.
Since the product of elements that are not zero divisors is not a zero divisor, $((x) + p)((y) + p) = (xy) + p$ must contain an element that is not a zero divisor.
Therefore, $(xy) + p \ne p$, so $xy \notin p$.

Hence, $p$ is a prime ideal.


Let $x \in A$ be a zero divisor.
Then $(x)$ is an ideal only containing zero divisors.
Therefore, $(x) \in \Sigma$, so $(x) \subset p$ for some maximal element $p$, which is a prime ideal.
Thus, the set of zero divisors in $A$ is a union of prime ideals.
