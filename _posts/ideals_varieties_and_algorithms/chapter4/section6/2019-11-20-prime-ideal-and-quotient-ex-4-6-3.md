---
layout: post
title:  "Quotients of prime ideals"
date:   2019-11-20
author: Hidenori
---

# Proposition
If $P \subset k[x_1, \cdots, x_n]$ is a prime ideal, then prove that $P:f = P$ if $f \notin P$ and $P:f = \ev{1}$ if $f \in P$.

# Solution
Suppose $f \notin P$.
Let $g \in P:f$.
Then $g\ev{f} \subset P$, so $gf \in P$.
Since $P$ is prime, $g \in P$ or $f \in P$.
Since we assumed that $f \notin P$, $g \in P$.
Therefore, $P:f \subset P$.
Since any ideal quotient contains the original ideal, $P \subset P:f$, so $P = P:f$.

Suppose $f \in P$.
Let $g \in k[x_1, \cdots, x_n]$.
Since $P$ is an ideal, $fg \in P$.
Therefore, $g \in P:f$.
Hence, $P:f = k[x_1, \cdots, x_n] = \ev{1}$.
