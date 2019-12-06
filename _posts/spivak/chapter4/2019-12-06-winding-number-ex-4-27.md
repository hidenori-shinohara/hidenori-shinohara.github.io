---
layout: post
title:  "Winding number"
date:   2019-12-06
author: Hidenori
---

# Proposition
Show that the integer $n$ of Problem 4-24[Spivak] is unique.

# Solution
Let $c  = c_{1, n} + \partial c^2$.

$$
\begin{align*}
  \int_{c} d\theta
    &= \int_{c_{1, n}} d\theta + \int_{\partial c^2} d\theta \\
    &= \int_{\partial c_{1, n}} \theta + \int_{\partial^2 c^2} \theta & \text{(Stokes' theorem)} \\
    &= \int_{\partial c_{1, n}} \theta + 0 \\
    &= 2\pi n.
\end{align*}
$$

Thus the value $n$ must be unique.
