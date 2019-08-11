---
layout: post
title:  "Properties of path-homotopic paths"
date:   2019-08-11
author: Hidenori
---

# Proposition
Let $X$ be a path-connected topological space.

1. Let $f, g: I \rightarrow X$ be two paths from $p$ to $q$.
   Show that $f \sim g$ if and only if $f \circ \overline{g} \sim c_p$.
1. Show that $X$ is simply connected if and only if any two paths in $X$ with the same initial and terminal points are path-homotopic.

# Solution

## 1
$$
\begin{align*}
  f \sim g
    &\iff [f] = [g] \\
    &\iff [f] \cdot [\overline{g}] = [g] \cdot [\overline{g}] \\
    &\iff [f \cdot \overline{g}] = [g \cdot \overline{g}] \\
    &\iff [f \cdot \overline{g}] = c_p \\
    &\iff f \cdot \overline{g} \sim c_p.
\end{align*}
$$

## 2

Suppose that $X$ is simply connected.
Let $f, g$ be two paths in $X$ with the same initial and terminal points $p, q$.
Then $f \cdot \overline{g}$ is a loop based at $p$.
Since $X$ is simply connected, $f \cdot \overline{g} \sim c_p$.
From 1, we know that this implies $f \sim g$.

On the other hand, suppose that any two paths in $X$ with the same initial and terminal points are path-homotopic.
Let $[f] \in \pi_1(X, p)$.
Then $f$ is path-homotopic to $c_p$.
Thus $[f] = [c_p]$, so $\pi_1(X, p)$ is the trivial group.

