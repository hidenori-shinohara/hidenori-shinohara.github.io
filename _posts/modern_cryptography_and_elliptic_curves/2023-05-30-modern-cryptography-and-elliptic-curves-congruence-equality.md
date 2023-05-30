---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Congruence and Equality"
date:   2023-05-30
author: Hidenori
---

Exercise from P.62 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

* Show (by example) that the congruence $ax \equiv ay \pmod n$ does not necessarily imply that $x \equiv y \pmod n$.

$1 \not\equiv 0 \pmod 2$ but $2 \cdot 1 \equiv 2 \cdot 0 \pmod 2$.

* On the other hand, show that if $x \equiv y \pmod n$, then $ax \equiv ay \pmod n$ for any integer $a$.

This is the same as Proposition 3.2.1.

* Show that there exist integers $u, v$ so that $au + nv = b$ if and only if $ax \equiv b \pmod n$ is solvable.

Let $a, b \in \mathbb{Z}$ and $n \in \mathbb{N}$ be given.
Pick $q \in \mathbb{Z}, r \in [0, \abs{n})$ such that $b = nq + r$.

$$
\begin{align*}
    \exists u, \exists v, au + nv = b
    &\iff \exists u, \exists v, au + nv = nq + r \\
    &\iff \exists u, \exists v, au = n(q - v) + r \\
    &\iff \exists u, au \equiv b.
\end{align*}
$$
