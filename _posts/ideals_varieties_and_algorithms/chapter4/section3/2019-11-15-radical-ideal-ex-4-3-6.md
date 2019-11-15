---
layout: post
title:  "Basic properties of radicals of ideals"
date:   2019-11-15
author: Hidenori
---

# Proposition
Let $I$ and $J$ be ideals in $k[x_1, \cdots, x_n]$, where $k$ is an arbitrary field.
Prove the following:

1. If $I^l \subset J$ for some integer $l > 0$, then $\sqrt{I} \subset \sqrt{J}$.
1. $\sqrt{I + J} = \sqrt{\sqrt{I} + \sqrt{J}}$.

# Solution
## 1
Let $f \in \sqrt{I}$.
Then $f^k \in I$ for some $k \geq 1$.
Then $f^{k + l} \in I^l \subset J$, so $f^{k + l} \in J$.
Therefore, $f \in \sqrt{J}$.

## 2
Let $f \in \sqrt{I + J}$.
Then $f^m \in I + J$ for some $m \geq 1$.
This implies that $f^m = ag + bh$ for some $g \in I, h \in J, a, b \in k[x_1, \cdots, x_n]$.
Moreover, $I \subset \sqrt{I}$ and $J \subset \sqrt{J}$, so $f^m \in \sqrt{I} + \sqrt{J}$.
Therefore, $f \in \sqrt{\sqrt{I} + \sqrt{J}}$.

On the other hand, let $f \in \sqrt{\sqrt{I} + \sqrt{J}}$.
Then $f^m \in \sqrt{I} + \sqrt{J}$ for some $m \geq 1$.
This implies that $f^m = ag + bh$ for some $g \in \sqrt{I}, h \in \sqrt{J}, a, b \in k[x_1, \cdots, x_n]$.
Choose $k, l \in \mathbb{N}$ such that $g^k \in I$ and $h^l \in J$.

Then $(f^m)^{k + l} = (ag + bh)^{k + l} = \sum_{i = 0}^{k + l} \binom{k + l}{i} (ag)^i(bh)^{k + l - i}$.
Then for each $i$, $i \geq k$ or $k + l - i \geq l$.
Therefore, $(ag)^i \in I$ or $(bh)^{k + l - i} \in J$ for each $i$, so $(f^m)^{k + l} \in I + J$.
This implies that $f \in \sqrt{I + J}$.
