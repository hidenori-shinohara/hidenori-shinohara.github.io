---
layout: post
title:  "Radical membership problem"
date:   2019-11-19
author: Hidenori
---

# Proposition
Determine whether the following polynomials lie in the following radicals.
If the answer is yes, what is the smallest power of the polynomial that lies in the ideal?

1. Is $x + y \in \sqrt{\ev{x^3, y^3, xy(x + y)}}$?
1. Is $x^2 + 3xz \in \sqrt{\ev{x + z, x^2y, x - z^2}}$?

# Solution

    from sympy import *
    from sympy.polys.orderings import monomial_key

    x, y, z, a = symbols('x y z a')

    print(groebner([x**3, y**3, x*y*(x + y), 1 - a * (x + y)], x, y, z, a, order='lex'))
    print(groebner([x + z, x**2*y, x - z**2, 1 - a * (x**2 + 3*x*z)], x, y, z, a, order='lex'))

gives

    GroebnerBasis([1], x, y, z, a, domain='ZZ', order='lex')
    GroebnerBasis([x - 1, y, z + 1, 2*a + 1], x, y, z, a, domain='ZZ', order='lex')

, so the answer to 1 is yes and 2 is no.

$x^3 + y^3 + 3xy(x + y) = (x + y)^3$.
Moreover, each monomial of $x^3$, $y^3$ and $xy(x + y)$ has a total degree of 3, so the smallest power of $x + y$ that lies in the ideal cannot be less than 3.
Therefore, the answer is 3.
