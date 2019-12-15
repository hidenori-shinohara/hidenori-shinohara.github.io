---
layout: post
title:  "Mobius transformation and a unit circle"
date:   2019-12-15
author: Hidenori
---

# Proposition
Show that the Mobius transformation $f(z) = \frac{1 + z}{1 - z}$ maps the unit circle (minus the point $z = 1$) onto the imaginary axis.

# Solution

Let $z$ be a point on the unit circle minus the point $z = 1$.

Then $\abs{z} = 1$.
Let $w = f(z)$.
Then $w - 1 = z(1 + w)$, so $\abs{w - 1} = \abs{z}\abs{1 + w} = \abs{1 + w}$.
Since $\abs{w - 1} = \abs{w + 1}$, $w$ is a point equidistant from $1$ and $-1$.
In other words, $w$ is on the imaginary axis.

On the other hand, let $y \in \mathbb{R}$.
We claim that $f(z) = yi$ for some $z$ on the unit circle minus the point.
Let $z = (-1 + yi) / (1 + yi)$.

* $\abs{z} = \abs{-1 + yi} / \abs{1 + yi} = \sqrt{1 + y^2} / \sqrt{1 + y^2} = 1$.
* $\displaystyle z = \frac{-(-1 + yi)^2}{1 + y^2} = \frac{y^2 - 1}{1 + y^2} + \frac{2y}{1 + y^2}i$.
  If $y = 0$, then $z = -1$.
  If $y \ne 0$, hen $z \notin \mathbb{R}$, so $z \ne 1$.

Thus, $z$ is a point on the unit circle minus the point.

Therefore, the Mobius transformation maps he unit circle onto the imaginary axis.
