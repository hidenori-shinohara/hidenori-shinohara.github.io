---
layout: post
title:  "Determine if the given ideal is radical"
date:   2019-11-14
author: Hidenori
---

# Proposition
Let $f_1 = y^2 + 2xy - 1$ and $f_2 = x^2 + 1$.
Prove that $\ev{f_1, f_2}$ is not a radical ideal.

# Solution
$f_1 + f_2 = (x + y)^2$.
Thus $(x + y)^2 \in \ev{f_1, f_2}$.
We claim that $x + y \notin \ev{f_1, f_2}$.


    from sympy import *
    from sympy.polys.orderings import monomial_key

    x, y = symbols('x y')

    print(groebner([y * y + 2 * x * y - 1, x * x + 1], x, y, order='lex'))

gives `GroebnerBasis([2*x + y**3 + 3*y, y**4 + 2*y**2 + 1], x, y, domain='ZZ', order='lex')`.

As the remainder on division of $x + y$ by the Grobner basis is not zero, $x + y \notin \ev{f_1, f_2}$ by Corollary 2 on P.84 (Ideals, Varieties and Algorithms).
Therefore, $\ev{f_1, f_2}$ is not radical.
