---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Number of Intersections of Lines and Conics"
date:   2023-05-22
author: Hidenori
---

Exercise from P.42 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> In how many points can two (distinct) conics intersect?

Based on drawings of my own and on P.43, it seems that there can be up to 4 intersections.

> In how many points can a conic and a cubic intersect?

Based on drawings of my own and on P.43, it seems that there can be up to 6 intersections.

> In how many points can two (distinct) cubics intersect?

Based on drawings of my own and on P.43, it seems that there can be up to 8 intersections.

> What would be your guess for a generalization?

It looks like a curve of degree $N$ and a curve of degree $M$ can have up to $MN$ intersections.

> Consider the intersection of a rational line with a rational conic.

> Are the point(s) of intersection necessarily rational?

No.

$f(x, y) = x^2 + y^2 - 1, g(x, y) = x + y$.

They intersect at $(\frac{1}{\sqrt{2}}, \frac{-1}{\sqrt{2}})$, which is clearly not rational.

> Now let’s suppose that the line intersects the conic in two points, one of which is rational. Is the second point necessarily rational?

Yes.
Let $f(x, y) = ax + by + c$ and $g(x, y)$ be a conic.
Since we assume $f$ is a line, $a \ne 0$ or $b \ne 0$.
Without loss of generality, $a \ne 0$.

Then $Z(f) = \\{ (x, y) \mid y = \frac{-a}{b}x - \frac{a}{c}\\}$.

Using this, we eliminate $y$'s from $g$.

Then we get $\alpha x^2 + \beta x + \gamma = 0$ for some $\alpha, \beta, \gamma$.
They are derived from the rational coefficients of $f$ and $g$ through the arithmetic operations, so they must be rational.

Case 1: $\alpha = 0$.
Then there are inifintely many intersections, which is not possible by the problem statement.

Case 2: $\alpha \ne 0$.

Then $x = P \pm Q$ where $P = \frac{-\beta}{2\alpha}$, $Q = \frac{\sqrt{\beta^2 - 4\alpha \gamma}}{2\alpha}$.

It's obvious that $P$ is rational.
And if one of the intersections is rational, that means either $P + Q$ or $P - Q$ is rational.
But this implies that the other one must be rational.
And if the $x$ coordinate is rational, then the $y$ coordinate must be rational.

