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
