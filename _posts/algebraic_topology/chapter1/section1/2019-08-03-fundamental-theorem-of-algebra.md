---
layout: post
title:  "The Fundamental Theorem of Algebra"
date:   2019-08-03
author: Hidenori
---

# Proposition
Every non-constant polynomial with coefficients in $\mathbb{C}$ has a root in $\mathbb{C}$.

# Solution
Let $p(z) = z^n + a_1z^{n - 1} + \cdots + a_n$ be given where $n \geq 0$.
Suppose that $p(z)$ has no roots in $\mathbb{C}$.

For each $r \geq 0$, define

$$
\begin{align*}
  f_r(s) = \frac{p(re^{2\pi is})/p(r)}{\abs{p(re^{2\pi is})/p(r)}}.
\end{align*}
$$

Then for each $r \geq 0$ and each $s \in \mathbb{C}$, $f_r(s) \in S^1 \subset \mathbb{C}$.

For a fixed $r \geq 0$,

* $f_r(0) = f_r(1) = 1$, and
* $f_r(s)$ is continuous,

so $f_r$ is a loop based at $1$.

For any $r \geq 0$, $g_t$ is a homotopy from $f_0$ to $f_r$ where $g_t(s) = f_{rt}(s)$.
Thus $f_0 \simeq f_r$ for each $r \geq 0$.

Let $r = \abs{a_1} + \cdots + \abs{a_n} + 1$.
Then $r \geq 1$ and $r > \abs{a_1} + \cdots + \abs{a_n}$.

Then for any $z \in \mathbb{C}$ such that $\abs{z} = r$,

$$
\begin{align*}
  \abs{z^n}
    &= \abs{z}\abs{z^{n - 1}} \\
    &> (\abs{a_1} + \cdots + \abs{a_n})\abs{z^{n - 1}} \\
    &= \abs{a_1}\abs{z^{n - 1}} + \cdots + \abs{a_n}\abs{z^{n - 1}} \\
    &\geq \abs{a_1}\abs{z^{n - 1}} + \abs{a_2}\abs{z^{n - 2}} + \cdots + \abs{a_n}\abs{z^{0}} \\
    &\geq \abs{a_1z^{n - 1} + a_2z^{n - 2} + \cdots + a_nz^{0}} \\
\end{align*}
$$

Therefore, we have $\abs{z^n} > \abs{a_1z^{n - 1} + a_2z^{n - 2} + \cdots + a_n}$.
Let $p_t(z) = z^n + t(a_1z^{n - 1} + \cdots + a_n)$ for each $t \in I$.
Then for each $t \in I$ and for each $z$ such that $\abs{z} = r$, $p_t(z) \ne 0$.

Consider the following:

$$
\begin{align*}
  h_t(s) = \frac{p_t(re^{2\pi is}) / p_t(r)}{\abs{p_t(re^{2\pi is}) / p_t(r)}}.
\end{align*}
$$

* $h_0(s) = e^{2\pi ins} = (\cos(2\pi s) + i\sin(2\pi s))^n$.
* $h_1(s) = f_r(s)$.

We claim that $h_t$ is a homotopy from $h_0$ to $h_1$.

* For any $t$, $h_t(0) = \frac{p_t(r) / p_t(r)}{\abs{p_t(r) / p_t(r)}} = 1$
* For any $t$, $h_t(1) = \frac{p_t(r) / p_t(r)}{\abs{p_t(r) / p_t(r)}} = 1$
* $H(s, t) = h_t(s)$ is continuous.

Thus $h_0 \simeq h_1$.

We showed earlier that $f_r \simeq f_0$.

Thus we have $h_0 \simeq h_1 = f_r \simeq f_0$, so $h_0 \simeq f_0$.
$h_0$ is the $n$th power of the generator of the fundamental group of $S^1$.
Since a power of a generator of the infinite cyclic group is equal to the identity element if and only if the power is $0$, $n = 0$.
Thus there exists no non-constant complex polynomials without complex roots.
