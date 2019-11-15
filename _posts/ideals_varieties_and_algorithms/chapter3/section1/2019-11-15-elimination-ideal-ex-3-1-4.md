---
layout: post
title:  "Bases for elimination ideals"
date:   2019-11-15
author: Hidenori
---

# Proposition
Find bases for the elimination ideals $I_1$ and $I_2$ for the ideal $I$ determined by the equations:

$$
\begin{align*}
  x^2 + y^2 + z^2 &= 4, \\
  x^2 + 2y^2 &= 5, \\
  xz &= 1.
\end{align*}
$$

How many rational solutions are there?

# Solution

    from sympy import *
    from sympy.polys.orderings import monomial_key

    x, y, z = symbols('x y z')

    print(groebner([x * x + y * y + z * z - 4, x * x - 2 * y * y - 5, x * z - 1], x, y, z, order='lex'))

gives `GroebnerBasis([3*x + 2*z**3 - 13*z, 3*y**2 + z**2 + 1, 2*z**4 - 13*z**2 + 3], x, y, z, domain='ZZ', order='lex')`.
By Theorem 2 (The Elimination Theorem) on P.122,

* $G_1 = \\{ 3y^2 + z^2 + 1, 2z^4 - 13z^2 + 3 \\}$ is a basis for $I_1$.
* $G_2 = \\{ 2z^4 - 13z^2 + 3 \\}$ is a basis for $I_2$.

This gives $z = \pm \sqrt{\frac{13 \pm \sqrt{145}}{4}}$.
Therefore, there exists no rational solution.
