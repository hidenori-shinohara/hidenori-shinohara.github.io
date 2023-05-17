---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Properties of rational lines"
date:   2023-05-16
author: Hidenori
---

Exercise from P.40 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Is every point on a rational line a rational point?

No, $\sqrt{2}$ is famously irrational, and the rational line $f(x, y) = x - y$ passes $(\sqrt{2}, \sqrt{2})$.

> If a line passes through at least two rational points, is it a rational line?

By the book's definition, no.
For instance, according to the book's definition, $f(x, y) = \sqrt{2}(x - y)$ is an irrational line passing through many rational points.

However, we'll show that any such lines are equivalent to a rational line.
In other words, any such lines have the same zero set as a rational line.

Suppose a line $f(x, y) = ax + by + c$ passes two rational points $(x_1, y_1) \ne (x_2, y_2)$.

Case 1: $a = 0$.

$b \ne 0$ as $f$ is a line.
Then the zero set of $f(x, y) = by + c$ is a line $\\{ (x, \frac{-c}{b}) \mid x \in \mathbb{R} \\}$.
Since $\frac{-c}{b} = y_1 = y_2$, $\frac{-c}{b}$ must be rational.
$f$ has the same zero set as the rational line $g(x, y) = y + (\frac{-c}{b})$.

Case 2: $b = 0$.
Similar to Case 1.

Case 3: $a \ne 0$ and $b \ne 0$.
By plugging in both points, we get $a(x_1 - x_2) + b(y_1 - y_2) = 0$.
Since $x_1 - x_2, y_1 - y_2 \in \mathbb{Q}$, $\frac{a}{b}$ is a rational.
The zero set of $f(x, y)$ is the same as that of $g(x, y) = \frac{a}{b}x + y + \frac{c}{b}$.
Finally, $\frac{a}{b}x_1 + y_1` + \frac{c}{b} = 0$ and we know every term except $c/b$ is rational.
In other words, $\frac{c}{b}$ must be rational too.


> What about lines if we only know one rational point through which they pass?

No.
For instance, the line $f(x, y) = \sqrt{2}x + y + 1$ passes through a rational point $(0, -1)$, but it's not a rational line, and there's no rational line with the same zero set.
Suppose a line $ax + by + c$ has the same zero set.
Obviously $b \ne 0$.
So such a line has the same zero set as $\frac{a}{b}x + y + \frac{c}{a}$.

Therefore, $\sqrt{2}x + 1 = \frac{a}{b}x + \frac{c}{a}$.
By plugging in $x = 0$, we get $c = a$ and $\frac{a}{b} = \sqrt{2}$.
Therefore, $c = a = \sqrt{2}b$, so obviously there's no triple $(a, b, c) \in \mathbb{Q}^3$ that satisfies that.

> Consider two distinct rational lines which intersect. Do they intersect in a rational point?

Yes.

Let $f(x, y) = a_1x + b_1y + c_1, g(x, y) = a_2x + b_2y + c_2$ be two distinct rational lines.
If $a_1 = 0$, every point in the the zero set of $f$ has the same (rational) $y$ coordinate.
We get the $x$ coordinate of the intersection by plugging in that $y$ coordinate to $g$, so the point must be rational.

The same argument can be applied to the case that one of $b_1, a_2, b_2$ is 0.
Assume none of $a_i, b_i$'s are 0.

Consider $a_2f(x, y) - a_1g(x, y) = (a_2b_1 - a_1b_2)y + (a_2c_1 - a_1c_2)$.
If $a_2b_1 - a_1b_2 = 0$, then the two lines are parallel or identical.

At the intersection, we have $f(x_0, y_0) = g(x_0, y_0) = 0$.
Specifically, $0 = a_2f(x_0, y_0) - a_1g(x_0, y_0) = (a_2b_1 - a_1b_2)y + (a_2c_1 - a_1c_2)$.
Therefore, the $y$ coordinate of the intersection must be rational.
The same argument can be applied for the $x$ coordinate, so the intersection is a rational point.


