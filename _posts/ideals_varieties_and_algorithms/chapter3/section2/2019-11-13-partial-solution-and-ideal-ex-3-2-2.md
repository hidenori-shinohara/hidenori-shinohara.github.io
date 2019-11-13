---
layout: post
title:  "Ideals and partial solutions"
date:   2019-11-13
author: Hidenori
---

# Proposition
Verify that $\ev{(y - z)x^2 + xy - 1, (y - z)x^2 + xz - 1} = \ev{xy - 1, xz - 1}$.
Also check that $y - z$ vanishes at all partial solutions in $V(I_1)$.

# Solution

* $\ev{(y - z)x^2 + xy - 1, (y - z)x^2 + xz - 1} \subset \ev{xy - 1, xz - 1}$.
  * $x((xy - 1) - (xz - 1)) + (xy - 1) = x^2(y - z) + xy - 1$.
  * $x((xy - 1) - (xz - 1)) + (xz - 1) = x^2(y - z) + xz - 1$.
* $\ev{xy - 1, xz - 1} \subset \ev{(y - z)x^2 + xy - 1, (y - z)x^2 + xz - 1}$.
  * $((y - z)x^2 + xy - 1) - x[((y - z)x^2 + xy - 1) - ((y - z)x^2 + xz - 1)] = xy - 1$.
  * $((y - z)x^2 + xz - 1) - x[((y - z)x^2 + xy - 1) - ((y - z)x^2 + xz - 1)] = xz - 1$.


```
    from sympy import *
    from sympy.polys.orderings import monomial_key

    x, y, z = symbols('x y z')

    print(groebner([x*y - 1, x*z - 1], x, y, z, order='lex'))
```

gives `GroebnerBasis([x*z - 1, y - z], x, y, z, domain='ZZ', order='lex')`.
Therefore, $V(I_1) = \ev{y - z}$ by the Elimination theorem on P.122 (Ideas, Varieties and Algorithms).
