---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Zeros of Order 1 or 2"
date:   2023-05-23
author: Hidenori
---

Exercise from P.44 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Let $h(x)$ be a polynomial of degree $n \geq 2$ with coefficients in a field $F$, and let $a \in F$.

> (1) Prove $h(x) = (x − a)q(x) + h(a)$ for some polynomial $q$ having coefficients in $F$.

We do so by induction on the degree of $h$.
When the degree is 0, then $q(x) = 0$ and we are done.

Suppose that we have proved it for any $h(x)$ of degree $\leq n$ for some $n \geq 0$.

Let $h(x) = a_{n + 1}x^{n + 1} + \cdots + a_0$ be given.
Let $g(x) = a_{n + 1}x^n + a_nx^{n - 1} + \cdots + a_1$.
Note $h(a) = ag(a) + a_0$.
By the inductive hypothesis, $g(x) = q(x)(x - a) + g(a)$ for some $q(x) \in F[x]$.

$$
\begin{align*}
    h(x) &= a_{n + 1}x^{n + 1} + \cdots + a_0 \\
         &= xg(x) + a_0 \\
         &= x(q(x)(x - a) + g(a)) + a_0 \\
         &= (x - a)(xq(x)) + g(a)x + a_0 \\
         &= (x - a)(xq(x)) + g(a)(x - a) + (ag(a) + a_0) \\
         &= (x - a)(xq(x)) + g(a)(x - a) + h(a) \\
         &= (x - a)(xq(x) + g(a)) + h(a).
\end{align*}
$$

By induction, the proposition must be true for any degree.


> (2) $h(a) = 0$ if and only if $h(x) = (x − a)q(x)$.

Obvious from the above.

> (3) $h$ has a double root at $a$ if and only if $h(a) = h'(a) = 0$, where $h′(x)$ is the first derivative of $h(x)$.

$h$ has a double root if and only if $h(x) = (x - a)^kq(x)$ for $k \geq 2$ and some $q(x)$ such that $q(a) \ne 0$.


If that's the case, then $h(a)$ is clearly 0.
Furthermore, $h'(x) = k(x - a)^{k - 1}q(x) + (x - a)^kq'(x)$.
Since $k \geq 2$, $h'(a) = 0$.

On the other hand, assume $h(a) = h'(a) = 0$.
By (2), $h(x) = (x - a)q(x)$ for some $q(x)$.
$h'(x) = q(x) + (x - a)q'(x)$, so $h'(a) = q(a) = 0$.
By (2), this implies $q(x) = (x - a)r(x)$ for some $r(x)$.
By plugging this back, we get $h(x) = (x - a)^2r(x)$.
$r(x) = (x - a)^ls(x)$ for some $l \geq 0$ and $s(x)$ such that $s(a) \ne 0$.
Then we have $h(x) = (x - a)^{2 + l}s(x)$ where $2 + l \geq 2$ and $s(a) \ne 0$.

