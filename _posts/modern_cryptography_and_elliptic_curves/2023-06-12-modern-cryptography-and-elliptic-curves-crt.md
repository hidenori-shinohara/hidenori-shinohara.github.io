---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Chinese Remainder Theorem"
date:   2023-06-12
author: Hidenori
---

Exercise from P.71 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Prove the Chinese Remainder Theorem.

We proved the special case with $n = 2$ [previously](/2023/06/12/modern-cryptography-and-elliptic-curves-crt-2.html)
We will prove this by induction on $n$.

Assume that we have proved it for some $n \geq 2$.
Now, let a system of congruences be given.

$$
\begin{align*}
    x &\equiv a_1 \pmod{m_1} \\
    x &\equiv a_2 \pmod{m_2} \\
    \vdots \\
    x &\equiv a_{n + 1} \pmod{m_{n + 1}}
\end{align*}
$$

where $\gcd(m_i, m_j) = 1$ for any $i \ne j$.

By induction, we can solve the first $n$.
In other words, there exists a unique solution for

$$
\begin{align*}
    x &\equiv a_1 \pmod{m_1} \\
    x &\equiv a_2 \pmod{m_2} \\
    \vdots \\
    x &\equiv a_{n} \pmod{m_{n}}
\end{align*}
$$

up to $m_1 \cdots m_n$.

Let $S$ be a solution.
Then we construct another system of congruences:

$$
\begin{align*}
    x &\equiv S \pmod{m_1 \cdots m_n} \\
    x &\equiv a_{n + 1} \pmod{m_{n + 1}}.
\end{align*}
$$

Then by the base case of induction, we can find a solution $T$ unique up to $m_1 \cdots m_{n + 1}$.
We claim that $T$ is a solution to the original system of congruences.

- $T \equiv S \pmod{m_1 \cdots m_{n}} \implies T \equiv S \equiv a_i \pmod {m_i}$ for each $i = 1, \cdots, n$.
- $T \equiv a_{n + 1} \pmod{m_{n + 1}}$.

Finally, we need to prove that it is unique up to $m_1 \cdots m_{n + 1}$.
Let $K, L$ be two solutions to the original system of congruences.
Then $K \equiv L \pmod m_i$ for each $i$.
So, $m_i \mid (K - L)$ for each $i$.
Since $m_i$'s are pairwise relatively prime, $\Pi m_i \mid (K - L)$.
In other words, $K \equiv L \pmod{\Pi m_i}$.

