---
layout: post
title:  "Inverse of a Mobius transformation"
date:   2019-11-23
author: Hidenori
---

# Proposition
Show that if $f(z) = \frac{az + b}{cz + d}$ is a Mobius transformation then $f^{-1}(z) = \frac{dz - b}{-cz + a}$.

# Solution

$$
\begin{align*}
  f^{-1}(f(z))
    &= \frac{d(az + b)/(cz + d) - b}{-c(az + b)/(cz + d) + a} \\
    &= \frac{d(az + b) - b(cz + d)}{-c(az + b) + a(cz + d)} \\
    &= \frac{adz - bcz}{ad - bc} \\
    &= z.
\end{align*}
$$

$$
\begin{align*}
  f^{-1}(f(z))
    &= \frac{d(az + b)/(cz + d) - b}{-c(az + b)/(cz + d) + a} \\
    &= \frac{d(az + b) - b(cz + d)}{-c(az + b) + a(cz + d)} \\
    &= \frac{adz - bcz}{-bc + ad} \\
    &= z.
\end{align*}
$$
