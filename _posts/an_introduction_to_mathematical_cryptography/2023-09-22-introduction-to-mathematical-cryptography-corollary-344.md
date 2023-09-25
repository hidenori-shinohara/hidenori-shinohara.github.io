---
layout: post
title:  "An Introduction to Mathematical Cryptography: Corollary 3.44"
date:   2023-09-22
author: Hidenori
---

We prove Exercise 3.31 from P.184 of An Introduction to Mathematical Cryptography.

# (a)

Let $\epsilon = 1/20$.

$$
\begin{align*}
    (\ln X)^{\epsilon} < \ln (L(X)) < (\ln X)^{1 - \epsilon}
    &\iff (\ln X)^{2\epsilon - 1} < \ln (\ln(X)) < (\ln X)^{1 - 2\epsilon} \\
    &\iff (\ln X)^{-9/10} < \ln (\ln(X)) < (\ln X)^{9/10}
\end{align*}
$$

* One can verify that the last inequality is true when $X = 10$ by checking the value.
* We will check the derivative.
    * $(\ln X)^{-9/10}$ is obviously decreasing over $[10, \infty)$.
    * $\ln (\ln X)$ is obviously increasing over $[10, \infty)$.
      The derivative of $\ln (\ln X)$ is $\frac{1}{X \ln X}$.
    * $((\ln X)^{9/10})' = \frac{9}{10X (\ln X)^{1/10}}$.

$$
\begin{align*}
    \frac{1}{X \ln X} < \frac{9}{10X(\ln X)^{1/10}}
        &\iff \frac{10}{9} < (\ln X)^{9/10} \\
        &\iff \big(\frac{10}{9}\big)^{10/9} < \ln X \\
        &\iff \big(\frac{10}{9}\big)^{10/9} < 1.13 < \ln 10 < \ln X
\end{align*}
$$

Therefore, at $X = 10$, the inequality holds.
Furthermore, the derivative of each satisfies the inequality as well for all $X > 10$.
By the Mean Value Theorem, the inequality holds for all $X > 10$.

# (b)

First, we will simplify $u$.

$$
\begin{align*}
    u &= \frac{\ln X}{\ln Y} \\
      &= \frac{\ln X}{\ln (L(X)^c)} \\
      &= \frac{\ln X}{c\ln L(X)} \\
      &= \frac{\ln X}{c\sqrt{\ln X \ln \ln X}} \\
      &= \frac{1}{c}\sqrt{\frac{\ln X}{\ln \ln X}}.
\end{align*}
$$

Note that we are proving this for a large $X$, so we will not care about some corner cases such as $\ln X = 0$.

$$
\begin{align*}
    u^{-u} = L(X)^{-\frac{1}{2c}(1 + o(1))}
        &\iff u \ln u = \frac{1}{2c}(1 + o(1))\ln L(X) \\
        &\iff \frac{2cu\ln u}{1 + o(1)} = \ln L(X) \\
        &\iff \frac{2\sqrt{\frac{\ln X}{\ln \ln X}}\ln \big(\frac{1}{c}\sqrt{\frac{\ln X}{\ln \ln X}}\big)}{1 + o(1)} = \sqrt{(\ln L(X))(\ln \ln X)} \\
        &\iff \frac{2\big[-\ln c + \frac{\ln \ln X}{2} - \frac{\ln \ln \ln X}{2}\big]}{1 + o(1)} = \ln \ln X \\
        &\iff \frac{-2\ln c + \ln \ln X - \ln \ln \ln X}{\ln \ln X} = 1 + o(1) \\
        &\iff \frac{-2\ln c + \ln \ln X - \ln \ln \ln X}{\ln \ln X} - 1 = o(1) \\
        &\iff \lim_{X \rightarrow \infty} \frac{-2\ln c + \ln \ln X - \ln \ln \ln X}{\ln \ln X} - 1 = 0
\end{align*}
$$

