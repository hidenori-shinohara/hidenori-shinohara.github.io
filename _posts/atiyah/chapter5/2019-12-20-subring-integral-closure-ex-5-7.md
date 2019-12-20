---
layout: post
title:  "An integrally closed subring"
date:   2019-12-20
author: Hidenori
---

# Proposition
Let $A$ be a subring of a ring $B$, such that the set $B - A$ is closed under multiplication.
Show that $A$ is integrally closed in $B$.

# Solution
Let $C$ be the integral closure of $A$ in $B$.
Clearly, $A \subset C$.
Suppose $A \subsetneq C$.
Let $x \in C \setminus A \subset B \setminus A$.
Then there exist $n \in \mathbb{N}, a_{n - 1}, \cdots, a_1, a_0 \in A$ such that

$$
\begin{align*}
  x^n + a_{n - 1}x^{n - 1} + \cdots + a_1x + a_0 = 0.
\end{align*}
$$

Then 

$$
\begin{align*}
  x(x^{n - 1} + a_{n - 1}x^{n - 2} + \cdots + a_1) = -a_0 \in A.
\end{align*}
$$

Since $x \in B \setminus A$ and $-a_0 \in A$, $x^{n - 1} + a_{n - 1}x^{n - 2} + \cdots + a_1$ cannot be in $B \setminus A$ because $B \setminus A$ is closed under multiplication.
Therefore, $x^{n - 1} + a_{n - 1}x^{n - 2} + \cdots + a_1 \in A$.

Then 

$$
\begin{align*}
  x(x^{n - 2} + a_{n - 2}x^{n - 3} + \cdots + a_2) \in A.
\end{align*}
$$

Since $x \in B \setminus A$ and $B \setminus A$ is closed under multiplication, $x^{n - 2} + a_{n - 2}x^{n - 3} + \cdots + a_2 \in A$.

By repeating this argument, we will eventually obtain $x(x + a_{n - 1}) \in A$.
This implies that $x + a_{n - 1} \in A$, but this is a contradiction.
Therefore, $A = C$.
