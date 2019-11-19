---
layout: post
title:  "Radical of $\\ev{xy, (x - y)x}$"
date:   2019-11-19
author: Hidenori
---

# Proposition
Let $J = \ev{xy, (x - y)x}$.
Describe $V(J)$ and show that $\sqrt{J} = \ev{x}$.

# Solution

    from sympy import *
    from sympy.polys.orderings import monomial_key

    x, y, a = symbols('x y a')

    print(groebner([x*y, (x - y)*x], x, y, a, order='lex'))

gives `GroebnerBasis([x**2, x*y], x, y, a, domain='ZZ', order='lex')`.

Let $S = \\{ (0, y) \mid y \in k \\}$.
Then $S \subset V(J)$ since $0^2 = 0 \cdot y = 0$.

On the other hand, let $(x, y) \in V(J)$.
Then $(x, y)$ satisfies $x^2 = 0$, so $x = 0$.
Therefore, $(x, y) \in S$.

Hence, $V(J) = S$.

Since $x^2 \in J$, $x \subset \sqrt{J}$.
This implies that $\ev{x} \subset \sqrt{J}$.

Let $f \in \sqrt{J}$.
Then $f^m \in J$.
In other words, $f^m = ax^2 + bxy$ for some $a, b \in k[x, y]$.
Since $f^m = (ax + by)x \in \ev{x}$, $f \in \sqrt{\ev{x}}$.
By Proposition 9 on P.186 of Ideals, Varieties, and Algorithms, $\sqrt{\ev{x}} = \ev{x}$.
Therefore, $\sqrt{J} \subset \ev{x}$.

Hence, $\sqrt{J} = \ev{x}$.
