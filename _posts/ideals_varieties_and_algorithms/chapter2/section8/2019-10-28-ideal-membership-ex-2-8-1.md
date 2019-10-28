---
layout: post
title:  "Ideal membership problem"
date:   2019-10-28
author: Hidenori
---

# Proposition
Determine whether $f = xy^3 - z^2 + y^5 - z^3$ is in the ideal $I = \ev{ -x^3 + y, x^2y - z }$.

# Solution

    from sympy import *
    from sympy.polys.orderings import monomial_key

    x, y, z = symbols('x y z')

    print(groebner([-x**3 + y, x**2 * y - z], x, y, z, order='lex'))

The code above shows that 

    GroebnerBasis([x**3 - y, x**2*y - z, x*y**3 - z**2, x*z - y**2, y**5 - z**3], x, y, z, domain='ZZ', order='lex')

is the groebner basis.
In other words, $\\{ x^3 - y, x^2y - z, xy^3 - z^2, xz - y^2, y^5 - z^3 \\}$.
Then $f = (xy^3 - z^2) + (y^5 - z^3)$, so $f$ is indeed in the ideal.
