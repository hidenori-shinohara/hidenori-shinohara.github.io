---
layout: post
title:  "Modern Cryptography and Elliptic Curves: $U_p$ is cyclic"
date:   2023-08-16
author: Hidenori
---

Important property used in Modern Cryptography and Elliptic Curves - A Beginner’s Guide.

> Given a finite field $F$, $F^{\times}$ is cyclic.

We will expand the proof given in Dummit and Foote in Proposition 18 in Section 9.5.

First, we prove a lemma:

> Given a cyclic group $G$ and $d \in \mathbb{N}$ such that $d \mid \abs{G}$, there are exactly $d$ elements of order dividing $d$.

Since $G$ is cyclic, we assume $G = \mathbb{Z}_n$.

It is obvious that $0, \frac{n}{d}, \frac{2n}{d}, \cdots, \frac{(d - 1)n}{d}$ are elements of order dividing $d$.
Let $m$ be any other element.
Then $\frac{kn}{d} < m < \frac{(k + 1)n}{d}$ for some $k \in \mathbb{Z}$.
This implies $kn < dm < (k + 1)n$, so $dm \ne 0$ in $\mathbb{Z}_n$.
Therefore, $m$ cannot have order dividing $d$.

In other words, $0, nd, \cdots, (d - 1)nd$ are all the elements of order dividing $d$, and it is easy to see that there are exactly $d$ of them.

Now we go back to the original theorem.
As $F^{\times}$ is a finite abelian group,
By the fundamental theorem of finitely generated abelian groups, $F^{\times}$ is isomorphic to

$$
\begin{align*}
    \mathbb{Z}_{n_1} \times \cdots \times \mathbb{Z}_{n_k}
\end{align*}
$$

where $n_k \mid n_{k - 1}, \cdots, n_2 \mid n_1$.

We focus on elements in $G$ whose order divides $n_k$.

By the lemma, for each $i$, there are exactly $n_k$ elements in $Z_{n_i}$ such that their order divides $n_k$.
More specifically,

For any $a \in \mathbb{Z}$ and $i$, $(0, \cdots, 0, a\frac{n_{i}}{n_k}, 0, \cdots, 0)$ has order dividing $n_k$ where the non-zero term is the $i$-th term.

Therefore, $$\mathbb{Z}_{n_1} \times \cdots \times \mathbb{Z}_{n_k}$$ has at least $\prod n_i$ elements of order dividing $n_k$.
Since it is isomorphic to $F^{\times}$, $F^{\times}$ must have $\prod n_i$ elements of order dividing $n_k$.

On the other hand, by Proposition 17 in Dummit and Foote, $x^{n_k} - 1 = 0$ in $F$ has at most $n_k$ roots.
In other words, $F^{\times}$ has at most $n_k$ elements of order dividing $n_k$.

This makes sense if and only if $k = 1$.
In other words, $F^{\times} \equiv \mathbb{Z}_{n_1}$, and hence it must be cyclic.
