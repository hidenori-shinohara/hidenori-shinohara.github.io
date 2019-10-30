---
layout: post
title:  "Radical example"
date:   2019-10-30
author: Hidenori
---

# Proposition
Given a field $k$, show that $\sqrt{\ev{x^2, y^2}} = \ev{x, y}$, and, more generally, show that $\sqrt{\ev{x^m, y^n}} = \ev{x, y}$ for any positive integers $n$ and $m$.

# Solution
We have $x, y \in \sqrt{\ev{x^m, y^n}}$.
Since the radical of an ideal is an ideal by Lemma 5 (P. 182, Ideals, Varieties, and Algorithms), $\ev{x, y} \subset \sqrt{\ev{x^m, y^n}}$.
Let $f \in \sqrt{\ev{x^m, y^n}}$.
Then $f^k = h_1x^m + h^2y^n$ for some $k \in \mathbb{N}$, $h_1, h_2 \in k[x, y]$.
Since this implies that $f$ has no constant term, $f \in \ev{x, y}$.
Therefore, $\ev{x, y} = \sqrt{\ev{x^m, y^n}}$.
