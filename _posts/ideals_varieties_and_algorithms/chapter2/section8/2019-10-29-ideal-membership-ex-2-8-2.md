---
layout: post
title:  "Ideal membership problem"
date:   2019-10-29
author: Hidenori
---

# Proposition
Determine whether $f = x^3z - 2y^2$ is in the ideal $I = \ev{ xz - y, xy + 2z^2, y - z }$.

# Solution

    from sympy import *
    from sympy.polys.orderings import monomial_key

    x, y, z = symbols('x y z')

    print(groebner([x * z - y, x * y + 2 * z * z, y - z], x, y, z, order='lex'))

The code above shows that 

    GroebnerBasis([x*z - z, y - z, 2*z**2 + z], x, y, z, domain='ZZ', order='lex')

is the groebner basis.
Let $(f_1, f_2, f_3) = (xz - z, y - z, 2z^2 + z)$.
Then $f = (x^2 + x + 1)f_1 - (2y + 2z)f_2 - f_3 + 2z$, so $f$ is not in the ideal.
