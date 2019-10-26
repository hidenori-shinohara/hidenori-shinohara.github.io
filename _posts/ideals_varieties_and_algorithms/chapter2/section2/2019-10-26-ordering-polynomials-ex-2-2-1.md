---
layout: post
title:  "Orderings on the monomials"
date:   2019-10-26
author: Hidenori
---

# Proposition
Rewrite each of the following polynomials, ordering the terms using the lex order, grlex order, and the grevlex order, giving $\LM(f), \LT(f)$ and $\multideg(f)$ in each case.

1. $f(x, y, z) = 2x + 3y + z + x^2 - z^2 + x^3$.
1. $f(x, y, z) = 2x^2y^8 - 3x^5yz^4 + xyz^3 - xy^4$.

# Solution
## 1
* lex: $z - z^2 + 3y + 2x + x^2 + x^3$.
    * $\LM(f) = z$.
    * $\LT(f) = z$.
    * $\multideg(f) = 3$.
* grlex: $z + 3y + 2x - z^2 + x^2 + x^3$.
    * $\LM(f) = z$.
    * $\LT(f) = z$.
    * $\multideg(f) = 3$.
* grevlex: $2x + 3y + z + x^2  - z^2 + x^3$.
    * $\LM(f) = x$.
    * $\LT(f) = 2x$.
    * $\multideg(f) = 3$.

## 2
* lex: $xyz^3 - xy^4 + 2x^2y^8 -3x^5yz^4$.
    * $\LM(f) = xyz^3$.
    * $\LT(f) = xyz^3$.
    * $\multideg(f) = 10$.
* grlex: $xyz^3 - xy^4 + 2x^2y^8 -3x^5yz^4$.
    * $\LM(f) = z$.
    * $\LT(f) = z$.
    * $\multideg(f) = 10$.
* grevlex: $-xy^4 + xyz^3 - 3x^5yz^4 + 2x^2y^8$.
    * $\LM(f) = xy^4$.
    * $\LT(f) = -xy^4$.
    * $\multideg(f) = 10$.
