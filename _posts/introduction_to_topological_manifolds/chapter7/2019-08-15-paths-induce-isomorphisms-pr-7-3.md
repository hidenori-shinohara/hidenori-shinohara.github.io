---
layout: post
title:  "Paths give the same isomorphism if and only if the fundamental group is abelian"
date:   2019-08-15
author: Hidenori
---

# Proposition
Let $X$ be a path-connected topological space, and let $p, q \in X$.
Show that all paths from $p$ to $q$ give the same isomorphism of $\pi_1(X, p)$ with $\pi_1(X, q)$ if and only if $\pi_1(X, p)$ is abelian.

# Solution
Suppose that all paths from $p$ to $q$ give the same isomorphism of $\pi_1(X, p)$ with $\pi_1(X, q)$.

Let $[f], [g] \in \pi_1(X, p)$.
We will show that $[f] \cdot [g] = [g] \cdot [f]$.
Let $h$ be a path from $p$ to $q$.
Such a path must exist since $X$ is path-connected.
Then $f \cdot h$ and $g \cdot h$ are both paths from $p$ to $q$.
By our assumption, $\beta_{f \cdot h} = \beta_{g \cdot h}$.

$$
\begin{align*}
  \beta_{f \cdot h}([g]) = \beta_{g \cdot h}([g])
    &\implies [\overline{f \cdot h} \cdot g \cdot f \cdot h] = [\overline{g \cdot h} \cdot g \cdot g \cdot h] \\
    &\implies [\overline{h} \cdot \overline{f} \cdot g \cdot f \cdot h] = [\overline{h} \cdot \overline{g} \cdot g \cdot g \cdot h] \\
    &\implies [\overline{h} \cdot \overline{f} \cdot g \cdot f \cdot h] = [\overline{h} \cdot g \cdot h] \\
    &\implies [\overline{f} \cdot g \cdot f] = [g] \\
    &\implies [g \cdot f] = [f \cdot g] \\
    &\implies [g] \cdot [f] = [f] \cdot [g].
\end{align*}
$$

Therefore, $\pi_1(X, p)$ is abelian.

TODO
