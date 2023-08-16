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

It is obvious that $0, nd, 2nd, \cdots, (d - 1)nd$ are elements of order dividing $d$.
Let $m$ be any other element.
Then $\frac{kn}{d} < m < \frac{(k + 1)n}{d}$ for some $k \in \mathbb{Z}$.
This implies $kn < dm < (k + 1)n$, so $dm \ne 0$ in $\mathbb{Z}_n$.
Therefore, $m$ cannot have order dividing $d$.

In other words, $0, nd, \cdots, (d - 1)nd$ are all the elements of order dividing $d$, and it is easy to see that there are exactly $d$ of them.

Now we go back to the original theorem.
As $G = F^{\times}$ is a finite abelian group,
By the fundamental theorem of finitely generated abelian groups, $G$ is isomorphic to

$$
\begin{align*}
    \mathbb{Z}_{n_1} \times \cdots \times \mathbb{Z}_{n_k}
\end{align*}
$$

where $n_k \mid n_{k - 1}, \cdots, n_2 \mid n_1$.

TODO: Finish this proof!


