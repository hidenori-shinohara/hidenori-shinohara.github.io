---
layout: post
title:  "Multilinear functions and their derivatives(WIP)"
date:   2019-12-25
author: Hidenori
---

# Proposition
Let $E_i, i = 1, \cdots, k$ be Euclidean spaces of various dimensions.

1. If $f$ is multilinear and $i \ne j$, show that for $h = (h_1, \cdots, h_k)$, with $h_l \in E_l$, we have
   $$
   \begin{align*}
     \lim_{h \rightarrow 0} \frac{\abs{f(a_1, \cdots, h_i, \cdots, h_j, \cdots, a_k)}}{\abs{h}} = 0.
   \end{align*}
   $$
1. TODO

# Solution

## 1
Let $g(x, y) = f(a_1, \cdots, x, \cdots, y, \cdots, a_k)$.
Then we can just use [the results we showed for bilinear functions because $g$ is bilinear](/2019/12/25/bilinear-ex-2-13.html).

## 2
TODO
