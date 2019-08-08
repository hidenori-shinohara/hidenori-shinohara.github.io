---
layout: post
title:  "The fundamental group is abelian iff basepoint-change homomorphisms depend only on the endpoints"
date:   2019-08-08
author: Hidenori
---

# Problem Statement
For a path-connected space $X$, show that $\pi_1(X)$ is abelian iff all basepoint-change homomorphisms $\beta_h$ depend only on the endpoints of the path $h$.

# Solution
First, suppose that $\pi_1(X)$ is abelian.

Let $x_0, x_1 \in X$ be given.
Let $h_1, h_2$ be paths from $x_0$ to $x_1$.
We claim that $\beta_{h_1} = \beta_{h_2}$.

Let $[f] \in \pi_1(X, x_1)$ be given.
Then $[h_1 \cdot f \cdot \overline{h_2}], [h_2 \cdot \overline{h_1}] \in \pi_1(X, x_0)$.

$$
\begin{align*}
  \beta_{h_1}([f])
    &= [h_1 \cdot f \cdot \overline{h_1}] \\
    &= [h_1 \cdot f \cdot \overline{h_2}] \cdot [h_2 \cdot \overline{h_1}] \\
    &= [h_2 \cdot \overline{h_1}] \cdot [h_1 \cdot f \cdot \overline{h_2}] \\
    &= [h_2 \cdot f \cdot \overline{h_2}] \\
    &= \beta_{h_2}([f]).
\end{align*}
$$

Therefore, $\beta_{h_1} = \beta_{h_2}$.

On the other hand, suppose that all basepoint-change homomorphisms $\beta_h$ depend only on the endpoints of the path $h$.
Let $x_0 \in X$ be given.
Let $f, g \in \pi_1(X, x_0)$ be given.
Let $x_1 = g(1 / 2)$.
Define two paths $h_1, h_2$ from $x_1$ to $x_0$ such that

* $h_1(t) = g((1 - t) / 2)$.
* $h_2(t) = g((1 + t) / 2)$.

Then $[g] = [\overline{h_1} \cdot h_2]$.

By our assumption, $\beta_{h_1} = \beta_{h_2}$.

$$
\begin{align*}
  \beta_{h_1}([f]) = \beta_{h_2}([f])
    &\implies [h_1 \cdot f \cdot \overline{h_1}] = [h_2 \cdot f \cdot \overline{h_2}] \\
    &\implies [\overline{h_1} \cdot (h_1 \cdot f \cdot \overline{h_1}) \cdot h_2] = [\overline{h_1} \cdot (h_2 \cdot f \cdot \overline{h_2}) \cdot h_2] \\
    &\implies [f \cdot \overline{h_1} \cdot h_2] = [\overline{h_1} \cdot h_2 \cdot f] \\
    &\implies [f \cdot g] = [g \cdot f] \\
    &\implies [f][g] = [g][f].
\end{align*}
$$

Therefore, $\pi_1(X)$ is abelian.

