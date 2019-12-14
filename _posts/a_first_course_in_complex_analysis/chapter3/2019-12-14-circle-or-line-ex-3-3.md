---
layout: post
title:  "Equation for a circle or line(WIP)"
date:   2019-12-14
author: Hidenori
---

# Proposition
Show that $\alpha(x^2 + y^2) + \beta x + \gamma y + \delta = 0$ is the equation for a circle or line if and only if $\beta^2 + \gamma^2 > 4\alpha\delta$.
Conclude that $x + iy$ is a solution to the equation above if and only if $u + iv$ is a solution to $\alpha + \beta u - \gamma v + \delta(u^2 + v^2)$ where $u + iv = (x - iy) / (x^2 + y^2)$.

# Solution
We will consider different cases:

* $\alpha = 0$
    * $\beta = \gamma = 0$.
      Then we have $\delta = 0$.
      Every point in $\mathbb{C}$ satisfies the equation $0 = 0$, and $\mathbb{C}$ is not a line or circle.
    * If $\\{ \beta, \gamma \\} \ne 0$, then $\beta x + \gamma y + \delta = 0$ is a line.
* $\alpha \ne 0$.
    * Then the equation equals $(x + \beta/2\alpha)^2 + (y + \gamma/2\alpha)^2 = (\beta^2 + \delta^2 - 4\alpha\delta) / 4\alpha^2$.
      If $(\beta^2 + \delta^2 - 4\alpha\delta) / 4\alpha^2 > 0$, then this is a circle.
      If it equals 0, then this is $(-\beta/2\alpha, -\gamma/2\alpha)$.
      if it is negative, there exists no solutions $x + iy \in \mathbb{C}$.

Therefore, the equation for a circle or line if and only if $\beta^2 + \gamma^2 > 4\alpha\delta$.

TODO(Finish the second part of the problem)

