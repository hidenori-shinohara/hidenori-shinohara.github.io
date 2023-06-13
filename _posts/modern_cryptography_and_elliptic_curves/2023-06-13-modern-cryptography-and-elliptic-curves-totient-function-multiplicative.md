---
layout: post
title:  "Modern Cryptography and Elliptic Curves: $\\phi$ is multiplicative"
date:   2023-06-13
author: Hidenori
---

Exercise from P.94 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> When $\gcd(m, n) = 1$, $\phi(mn) = \phi(m)\phi(n)$.

For any $k \in \mathbb{N}$, $U_k = \\{ \lbrack a\rbrack_k \mid \gcd(a, n) = 1 \\}$ as defined in the book.

By Proposition 4.11, it suffices to show $\abs{U_{mn}} = \abs{U_m \times U_n}$.

We will do so by showing that $$F: \lbrack a\rbrack_{mn} \mapsto (\lbrack a\rbrack_m, \lbrack a\rbrack_n)$$ is a well-defined bijection.

First, for any $\lbrack a\rbrack_{mn}$, we have $\gcd(mn, a) = 1$.
Therefore, $\gcd(m, a) = \gcd(n, a) = 1$, and thus $F(\lbrack a\rbrack_{mn}) \in U_m \times U_n$ for any $\lbrack a\rbrack_{mn} \in U_{mn}$.

Furthermore, for any $\lbrack a\rbrack_{mn} = \lbrack b\rbrack_{mn}$, we have $a \equiv b \pmod{mn}$.
This means $mn \mid (a - b)$, so $m \mid (a - b)$ and thus $a \equiv b \pmod{m}$.
Similarly, $a \equiv b \pmod{n}$.
Thus $F(\lbrack a\rbrack_{mn}) = F(\lbrack b\rbrack_{mn})$ for any $\lbrack a\rbrack_{mn} = \lbrack b\rbrack_{mn}$.

Now that we have shown that $F$ is a well-defined function, we will show that it is bijective.

Let $(\lbrack a\rbrack_{m}, \lbrack b\rbrack_{n}) \in U_m \times U_n$ be given.
By the Chinese Remainder Theorem, there exists a solution for

$$
\begin{align*}
    x &\equiv a \pmod{m} \\
    x &\equiv b \pmod{n}.
\end{align*}
$$

Any solution $c$ to the system above will give us $\lbrack c\rbrack_{mn}$ such that $F(\lbrack c\rbrack_{mn}) = (\lbrack a\rbrack_m, \lbrack b\rbrack_n)$.
Therefore, $F$ is surjective.

Let $\lbrack c\rbrack_{mn}, \lbrack c'\rbrack_{mn}$ such that $F(\lbrack c\rbrack_{mn}) = F(\lbrack c'\rbrack_{mn}) = (\lbrack a\rbrack_m, \lbrack b\rbrack_n)$.
Then both $c$ and $c'$ satisfy the above system.
The Chinese Remainder Theorem states that such a solution is unique up to $\pmod{mn}$.
Therefore, $c \equiv c' \pmod{mn}$, so $\lbrack c\rbrack_{mn} = \lbrack c'\rbrack_{mn}$.
Hence, $F$ is injective.
