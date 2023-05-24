---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Orders of zeros and derivatives"
date:   2023-05-24
author: Hidenori
---

Exercise from P.44 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Show that $h$ has a zero of order $k$ at $x = a$ if and only if $h(a) = h'(a) = \cdots = h^{(k−1)}(a) = 0$ and $h^{(k)}(a) = 0$, where $h^{(i)}$ is the $i$th derivative of $h$.

Let $n$ denote $h$'s degree.
It is obvious that $h^{(i)} = 0$ for all $i > n$.
Using the Taylor expansion, we have

$$
\begin{align*}
    h(x) &= \sum_{i=0}^{n}\frac{(x - a)^ih^{(i)}(a)}{i!} \\
         &= (x-a)^k[\sum_{i=k}^{n}\frac{(x - a)^{i-k}h^{(i)}(a)}{i!}] + \sum_{i=0}^{k-1}\frac{(x - a)^ih^{(i)}(a)}{i!}.
\end{align*}
$$

Denote the summations by $P(x), Q(x)$ such that $h(x) = (x-a)^kP(x) + Q(x)$.
We will use this equality throughout the proof.

By definition, $h$ has a zero of order $k$ at $x = a$ if and only if $h(x) = (x - a)^{k}q(x)$ with $q(a) \ne 0$.

First, assume $h$ has a zero of order $k$ at $x = a$.
Then $(x - a)^k(P(x) - q(x)) = Q(x)$.
The left hand side has a degree of either $\geq k$ or 0, depending on whether $P(x) - q(x) = 0$.
However, the degree on the left hand side cannot be $\geq k$ as the right hand side clearly has a degree $\leq k - 1$.

Thus $Q(x) = 0$, and hence $h^{(i)}(a) = 0$ for each $i = 0, \cdots, k - 1$.
Since $P(x) = q(x)$ and $q(a) \ne 0$, $P(a) \ne 0$.
This implies $\frac{h^{(k)}(0)}{k!} \ne 0$.
Hence, $h^{(k)} \ne 0$.

On the other hand, assume that $h^{(i)} = 0$ for each $i = 0, \cdots, k - 1$ and $h^{(k)} \ne 0$.
This implies $Q(x) = 0$.
Then we have $h(x) = (x - a)^kP(x)$.
$P(a) \ne 0$ as $P(a) = \frac{h^{(k)}(0)}{k!} \ne 0$.
