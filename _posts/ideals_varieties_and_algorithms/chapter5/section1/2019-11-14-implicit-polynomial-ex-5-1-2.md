---
layout: post
title:  "A variety mapped by a polynomial"
date:   2019-11-14
author: Hidenori
---

# Proposition
Let $V = V(y - x)$ in $\mathbb{R}^2$ and let $\phi: \mathbb{R}^2 \rightarrow \mathbb{R}^3$ be the polynomial mapping represented by $\phi(x, y) = (x^2 - y, y^2, x - 3y^2)$.
The image of $V$ under $\phi$ is a variety in $\mathbb{R}^3$.
Find a system of equations defining the image of $\phi$.

# Solution

$V = \\{ (a, a) \mid a \in \mathbb{R} \\}$.
Thus $\phi(V) = \\{ (a^2 - a, a^2, a - 3a^2) \mid a \in \mathbb{R} \\}$.

    from sympy import *
    from sympy.polys.orderings import monomial_key

    x, y, z, a = symbols('x y z a')

    print(groebner([x - a * a + a, y - a * a, z - a + 3 * a * a], a, z, y, x, order='lex'))

gives `GroebnerBasis([a + x - y, x + 2*y + z, x**2 - 2*x*y + y**2 - y], a, z, y, x, domain='ZZ', order='lex')`.

By Theorem 1 (Polynomial Implicitization) on P.134 (Ideals, Varieties, and Algorithms), $V(x + 2y + z, x^2 - 2xy + y^2 - y)$ is the smallest variety in $\mathbb{R}^3$ containing $\phi(V)$.
Since it is given that $\phi(V)$ is a variety, $\phi(V) = V(x + 2y + z, x^2 - 2xy + y^2 - y)$.
