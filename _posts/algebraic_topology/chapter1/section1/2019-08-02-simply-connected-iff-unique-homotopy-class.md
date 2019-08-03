---
layout: post
title:  "A space is simply connected iff any two points are connected by paths of a unique homotopy class"
date:   2019-08-02
author: Hidenori
---

# Proposition
A space $X$ is simply-connected iff there is a unique homotopy class of paths connecting any two points in $X$.

# Solution
Suppose that $X$ is simply-connected.

Let $x, y \in X$ be given.
Since $X$ is path-connected, $x, y$ are connected by a path.
Let $f, g$ be two paths connecting $x$ and $y$.
Then $f \cdot \overline{g}$ is a loop with a basepoint $x$.
Since $X$ is simply-connected, $\pi(X, x)$ is the trivial group.
Let $e$ denote the constant loop at $x$.
Then $f \cdot \overline{g} \simeq e$.

$$
\begin{align*}
  f \cdot \overline{g} \simeq e
    &\implies (f \cdot \overline{g}) \cdot g \simeq e \cdot g \\
    &\implies f \cdot (\overline{g} \cdot g) \simeq g \\
    &\implies f \cdot e \simeq g \\
    &\implies f \simeq g.
\end{align*}
$$

Therefore, $f$ and $g$ are path homotopic, so there is a unique homotopy class of paths connecting any two points in $X$.

On the other hand, suppose that there is a unique homotopy class of paths connecting any two points in $X$.

Then $X$ is path-connected.
Let $x \in X$.
Let $[f] \in \pi(X, x)$.
Then $f$ is a path connecting $x$ with $x$.
Let $e$ be the constant loop at $x$.
Then $f$ and $e$ are both paths connecting $x$ to $x$, so $f \simeq e$.
Therefore, $\pi(X, x) = \\{ [e] \\}$s, so $X$ is simply-connected.
