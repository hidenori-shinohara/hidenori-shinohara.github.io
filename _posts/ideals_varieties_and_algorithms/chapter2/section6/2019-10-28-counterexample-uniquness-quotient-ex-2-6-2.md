---
layout: post
title:  "Quotients need not be unique (Grobner basis)"
date:   2019-10-28
author: Hidenori
---

Section 2.5 of Ideals, Varieties, and Algorithms shows that $G = \\{ x + z, y - z \\}$ is a Grobner basis for lex order.

* Dividing $xy$ by $x + z, y - z$ shows that $xy = y(x + z) - z(y - z) - z^2$.
* Dividing $xy$ by $y - z, x + z$ shows that $xy = x(y - z) + z(x + z) - z^2$.

Thus the remainder is the same, but the "quotients" are different.
Therefore, the uniqueness of the remainder is the best one we can hope for from a Grobner basis.
