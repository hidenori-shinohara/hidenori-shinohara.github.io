---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Proof for Bachet duplication formula"
date:   2023-05-15
author: Hidenori
---

Exercise from P.38 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

Given an elliptic curve $y^2 = x^3 + k$ and a point $(a, b)$, we'll find the intersection between the line tangent at $(a, b)$ and the curve.

$\frac{dy}{dx} = \frac{3x^2}{2y}$, so the slope of the tangent line is $\frac{3a^2}{2b}$.
The $y$-intercept is $b - \text{slope} \cdot a = \frac{2b^2 - 3a^3}{2b}$.

Now, plug $k = b^2 - a^3$ and $y = \text{slope} x + \text{y-intercept}$ into $y^2 = x^3 + k$.
To simplify, multiply each side by $4b^2$.
Move everything on one side and factor out $(x - a)^2$.
We can do so by the following Python code.

```
import sympy

x, a, b, k = sympy.symbols('x a b k')
y = 3*a*a*x - 3*a*a*a + 2*b*b
xCubedPlusK = 4*b*b*(x*x*x + b*b - a*a*a)
div = x - a
# Prints -9*a**4 + 8*a*b**2 + 4*b**2*x
print(sympy.simplify((xCubedPlusK - y*y) / div / div))
```

Therefore, the last root is $\frac{9a^4 - 8ab^2 - 4b^2x}{(x - a)^2}$.
By using $b^2 = a^3 + k$, we have $\frac{a^4 - 8ak}{4b^2}$.
In other words, this is the $x$ coordinate of the other intersection.

Finally plug this $x$ coordinate into $y = \text{slope} \cdot x + \text{y-intercept}$.
Multiply both sides by $8b^3$ while using $b^2 = a^3 + k$ whenever appropriate.


```
yTimesEightBCubed =  (3 * a**2) * (a**4 - 8 * a * k)
bSquared = a**3 + k
yInterceptTimesEightBCubed = 4 * bSquared * (2 * bSquared - 3 * a**3)

# Prints -a**6 - 20*a**3*k + 8*k**2
print(sympy.simplify(yTimesEightBCubed + yInterceptTimesEightBCubed))
```

It is easy to see that this matches the formula in the book exactly.
