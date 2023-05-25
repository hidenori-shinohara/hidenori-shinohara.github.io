---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Multiplicity at the Point of Tangency"
date:   2023-05-25
author: Hidenori
---

Exercise from P.44 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Now consider $y^2 = g(x)$ where $g$ is a cubic, that is the zero set of $f(x, y) = y^2 − g(x)$. We want to see that a nonvertical tangent has multiplicity at least 2 at the point of tangency.

Let $y = \alpha x + \beta$ denote the tangent line.
Note that this is possible as the problem specifies that it is nonvertical.
Let $(a, b)$ be the point of tangency.

We will first calculate a few values that will be useful in the following proof.

$$
\begin{align*}
    \alpha
        &= \frac{dy}{dx}\big\vert_{(a, b)} \\
        &= \frac{g'(x)}{2y}\big\vert_{(a, b)} \\
        &= \frac{g'(a)}{2b}.
\end{align*}
$$

In other words, $g'(a) = 2\alpha b$.

Let $h(x) = f(x, \alpha x + \beta) = (\alpha x + \beta)^2 - g(x)$.

As $(a, b)$ is the point of tangency, $b = \alpha a + \beta$, $f(a, b) = 0$ and $b^2 = g(a)$.

With these values, we will prove the proposition now.
To show that the multiplicity is at least 2, we will show that $h(a) = h'(a) = 0$ [based on the proposition proved here](https://hidenori-shinohara.github.io/2023/05/24/modern-cryptography-and-elliptic-curves-polynomialzero-order-generalization.html).

$h(a) = (\alpha a + \beta)^2 - g(a) = b^2 - b^2 = 0$.

$h'(x) = 2\alpha(\alpha x + \beta) - g'(x)$.
Therefore, $h'(a) = 2\alpha(\alpha a + \beta) - g'(a) = 2\alpha b - g'(a) = 0$.

Therefore, the tangent has multiplicity at least 2 at the point of tangency.

