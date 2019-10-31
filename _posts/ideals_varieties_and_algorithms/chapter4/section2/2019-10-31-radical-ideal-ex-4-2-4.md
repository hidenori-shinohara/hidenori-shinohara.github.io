---
layout: post
title:  "Basic properties of a radical ideal"
date:   2019-10-31
author: Hidenori
---

# Proposition
Let $I$ be an ideal in $k[x_1, \cdots, x_n]$, where $k$ is an arbitrary field.

1. Show that $\sqrt{I}$ is a radical ideal.
1. Show that $I$ is radical if and only if $I = \sqrt{I}$.
1. Show that $\sqrt{\sqrt{I}} = \sqrt{I}$.

# Solution

## 1

First, we will show that $\sqrt{I}$ is an ideal.

1. $0 \in \sqrt{I}$, so $\sqrt{I}$ is nonempty.
1. Let $f, g \in \sqrt{I}$.
   Then $f^m, g^n \in I$ for some $m, n \in \mathbb{N}$.
   Then $(f - g)^{m + n - 1} = \sum_{i=0}^{m + n - 1} (-1)^{m + n - i}f^ig^{m + n - i}$.
   Since for any $i$, $i \geq m$ or $m + n - i \geq n$, each term is in $I$.
   Thus $(f - g)^{m + n - 1} \in I$, so $f - g \in \sqrt{I}$.
1. Let $f \in \sqrt{I}, g \in k[x_1, \cdots, x_n]$.
   Then $f^m \in I$ for some $m \in \mathbb{N}$.
   $(gf)^m = g^mf^m \in I$, so $gf \in \sqrt{I}$.
Therefore, $\sqrt{I}$ is indeed an ideal.

Let $f^m \in \sqrt{I}$.
Then $(f^m)^n \in I$ for some $n \in \mathbb{N}$.
$f^{mn} \in I$, so $f \in \sqrt{I}$.

Therefore, $\sqrt{I}$ is indeed a radical ideal.

## 2

Suppose $I$ is radical.
Let $f \in I$.
Then $f^1 \in I$, so $f \in \sqrt{I}$.
Let $g \in \sqrt{I}$.
Then $g^m \in I$ for some $m$.
Since $I$ is radical, $g \in I$.
Thus $\sqrt{I} = I$.

Suppose $\sqrt{I} = I$.
In 1, we showed that $\sqrt{I}$ is radical.
Thus $I$ is radical.

## 3
In 1, we showed that $\sqrt{I}$ is radical.
By using the results of 2, $\sqrt{I} = \sqrt{\sqrt{I}}$.
