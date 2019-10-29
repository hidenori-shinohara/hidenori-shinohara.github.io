---
layout: post
title:  "Calculation of $S$ polynomials"
date:   2019-10-28
author: Hidenori
---

# Proposition
Calculate $S(f_i, f_j)$ for each $i < j$. (Grlex)

1. $f_1 = x^3 - 2xy$.
1. $f_2 = x^2y - 2y^2 + x$.
1. $f_3 = -x^2$.
1. $f_4 = -2xy$.
1. $f_5 = -2y^2 + x$.

# Solution

* $S(f_1, f_2) = -x^2$.
* $S(f_1, f_3) = -2xy$.
* $S(f_1, f_4) = -2xy^2 = yf_4$.
* $S(f_1, f_5) = x^4/2 - 2xy^3 = \frac{x}{2}f_1 + f_2 + y^2f_4 - f_5$.

* $S(f_2, f_3) = -2y^2 + x = f_5$.
* $S(f_2, f_4) = -2y^2 + x = f_5$.
* $S(f_2, f_5) = x^3 - 2y^3 + xy = f_1 - f_4 + yf_5$.

* $S(f_3, f_4) = 0$.
* $S(f_3, f_5) = x^3 / 2$.

* $S(f_4, f_5) = x^2 / 2$.
