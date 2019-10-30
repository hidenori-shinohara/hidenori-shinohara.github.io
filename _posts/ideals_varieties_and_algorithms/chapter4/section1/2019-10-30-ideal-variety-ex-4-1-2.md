---
layout: post
title:  "Multiple ideals may correspond to the same ideal"
date:   2019-10-30
author: Hidenori
---

# Proposition
Let $J = \ev{ x^2 + y^2 - 1, y - 1 }$.
Find $f \in I(V(J))$ such that $f \notin J$.

# Solution

    GroebnerBasis([x**2, y - 1], x, y, domain='ZZ', order='lex')

Sympy shows that $\\{ x^2, y - 1 \\}$ is a Groebner basis of $J$.
Thus $(x, y) = (0, 1)$ is the only point in $V(J)$.
$(x, y) = (0, 1)$ vanishes on the function $h(x, y) = x$, so $h \in I(V(J))$.
However, $x \notin J$ because it is not divisible by the Groebner basis.

