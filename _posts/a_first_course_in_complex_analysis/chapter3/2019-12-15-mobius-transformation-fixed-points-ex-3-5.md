---
layout: post
title:  "Fixed points of a Mobius transformation"
date:   2019-12-15
author: Hidenori
---

# Proposition
Prove that any Mobius transformation different from the identity map can have at most two fixed points.

# Solution
Let $f(z) = (az + b) / (cz + d)$ with $ad - bc \ne 0$.

If $c = 0$, it is easy to see that there exists exactly one $z \in \mathbb{C}$ that satisfies $z = (az + b) / d$.
Suppose $c \ne 0$.
Then $f(z) = z$ can be simplified to $cz^2 + (d - a)z - b = 0$.
Therefore, $z = \frac{a - d \pm \sqrt{(d - a)^2 + 4bc}}{2c}$, so there are either one or two fixed points.
