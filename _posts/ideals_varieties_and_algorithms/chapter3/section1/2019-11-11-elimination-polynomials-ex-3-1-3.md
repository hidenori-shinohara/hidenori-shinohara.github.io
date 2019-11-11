---
layout: post
title:  "Solving a system of equations using a Grobner basis"
date:   2019-11-11
author: Hidenori
---

# Proposition
Determine all solutions $(x, y) \in \mathbb{Q}^2$ of the system of equations

$$
\begin{align*}
  x^2 + 2y^2 &= 2, \\
  x^2 + xy + y^2 &= 2.
\end{align*}
$$

Also determine all solutions in $\mathbb{C}^2$.

# Solution
Let $I = \ev{x^2 + 2y^2 - 2, x^2 + xy + y^2 - 2}$.

    from sympy import *
    from sympy.polys.orderings import monomial_key

    x, y = symbols('x y')

    print(groebner([x**2 + 2*y**2 - 2, x**2 + x*y + y**2 - 2], x, y, order='lex'))

gives `GroebnerBasis([x**2 + 2*y**2 - 2, x*y - y**2, 3*y**3 - 2*y], x, y, domain='ZZ', order='lex')`
By solving this from the last element in the basis, we get $(x, y) = (\pm \sqrt{2}, 0), (\sqrt{6}/3, \sqrt{6}/3), (-\sqrt{6}/3, -\sqrt{6}/3)$.
Thus there are no solutions in $\mathbb{Q}^2$ and there are 3 solutions in $\mathbb{C}^2$.


