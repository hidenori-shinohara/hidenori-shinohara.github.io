---
layout: post
title:  "Properties of Quotient Maps"
date:   2019-08-26
author: Hidenori
---

# Proposition
1. Any composition of quotient maps is a quotient map.
1. TODO
1. TODO
1. TODO
1. TODO

# Solution
## 1
Let $X, Y, Z$ be topological spaces and $p: X \rightarrow Y, q: Y \rightarrow Z$ be quotient maps.
Let $U \subset Z$ be given.

* Since $q$ is a quotient map, $U$ is open if and only if $q^{-1}(U)$ is open.
* Since $p$ is a quotient map, $q^{-1}(U)$ is open if and only if $p^{-1}(q^{-1}(U))$ is open.

Therefore, $U$ is open if and only if $p^{-1}(q^{-1}(U))$ is open.
Since $p^{-1}(q^{-1}(U)) = (q \circ p)^{-1}(U)$, $U$ is open if and only if $(q \circ p)^{-1}(U)$ is open.
Therefore, $q \circ p$ is a quotient map.

## 2
TODO

## 3
TODO

## 4
TODO

## 5
TODO
