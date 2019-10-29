---
layout: post
title:  "Calculation of points on a variety"
date:   2019-10-29
author: Hidenori
---

# Proposition
Find the points in $\mathbb{C}^3$ on the variety

$$
\begin{align*}
  V(x^2 + y^2 + z^2 - 1, x^2 + y^2 + z^2 - 2x, 2x - 3y - z).
\end{align*}
$$

# Solution

    from sympy import *
    from sympy.polys.orderings import monomial_key

    x, y, z = symbols('x y z')

    print(groebner([x**2 + y**2 + z**2 - 1, x**2 + y**2 + z**2 - 2*x, 2*x - 3*y - z], x, y, z, order='lex'))

The Python code above generates the following output:

    GroebnerBasis([2*x - 1, 3*y + z - 1, 40*z**2 - 8*z - 23], x, y, z, domain='ZZ', order='lex')

Therefore, $\\{ 2x - 1, 3y + z - 1, 40z^2 - 8z - 23 \\}$ is a Groebner basis.

By solving this, we get $V(I) = \\{ (1/2, (1 - c)/3, c) \mid c = \frac{2 \pm \sqrt{26}}{20} \\}$.
