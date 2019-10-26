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
* lex: $x^3 + x^2 + 2x + 3y - z^2 + z$.
    * $\LM(f) = x^3$.
    * $\LT(f) = x^3$.
    * $\multideg(f) = 3$.
* grlex: $x^3 + x^2 - z^2 + 2x - 3y + z$.
    * $\LM(f) = x^3$.
    * $\LT(f) = x^3$.
    * $\multideg(f) = 3$.
* grevlex: $x^3 - z^2 + x^2 + z - 3y + 2x$.
    * $\LM(f) = x^3$.
    * $\LT(f) = x^3$.
    * $\multideg(f) = 3$.

## 2
* lex: $-3x^5yz^4 + 2x^2y^8 - xy^4 + xyz^3$.
    * $\LM(f) = x^5yz^4$.
    * $\LT(f) = -3x^5yz^4$.
    * $\multideg(f) = 10$.
* grlex: $-3x^5yz^4 + 2x^2y^8 - xy^4 + xyz^3$.
    * $\LM(f) = x^5yz^4$.
    * $\LT(f) = -3x^5yz^4$.
    * $\multideg(f) = 10$.
* grevlex: $2x^2y^8 - 3x^5yz^4 + xyz^3 - xy^4$.
    * $\LM(f) = x^2y^8$.
    * $\LT(f) = 2x^2y^8$.
    * $\multideg(f) = 10$.
