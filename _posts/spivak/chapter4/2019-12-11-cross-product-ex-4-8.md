---
layout: post
title:  "Cross product in $V$"
date:   2019-12-11
author: Hidenori
---

# Proposition
If $\omega \in \Lambda^n(V)$ is a volume element, define a "cross product" $v_1 \times \cdots \times v_{n - 1}$ in terms of $\omega$.

# Solution
A cross product is defined in the textbook on P.83 and P.84.
However, the textbook only defines a cross product for $\mathbb{R}^n$.
This problem asks for a general definition in a general vector space $V$, which may or may not be $\mathbb{R}^n$.

Let $v_1, \cdots, v_{n - 1} \in V$ be given.
Define $\phi: V \rightarrow \mathbb{R}$ by

$$
\begin{align*}
  \phi(w) = \omega(v_1, \cdots, v_{n - 1}, w).
\end{align*}
$$

Then $\phi \in \Lambda^1(V)$.

Therefore, it is natural to define a cross product $v_1 \times \cdots \times v_{n - 1}$ to be a unique $z \in V$ such that $T(w, z) = \phi(z)$ where $T$ is the inner product associated to the volume element $\omega$.

It is not clear (at least to me) whether such a $z$ exists at all, but the problem simply asks for a definition, so this is one way to define it.
