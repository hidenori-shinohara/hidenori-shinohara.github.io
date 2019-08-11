---
layout: post
title:  "Path homotopy is an equivalence relation"
date:   2019-08-11
author: Hidenori
---

# Proposition
Let $X$ be a topological space.
For any points $p, q \in X$, path homotopy is an equivalence relation on the set of all paths in $X$ from $p$ to $q$.

# Solution

Let $f, g, h$ be paths in $X$ from $p$ to $q$.

## Reflexive property

$F(s, t) = f(s)$ is a path homotopy from $f$ to $f$.
Thus $f$ is path-homotopic to $f$.

## Symmetric property

Suppose $f$ is path-homotopic to $g$.
Let $F: I \times I \rightarrow X$ be a path homotopy from $f$ to $g$.
Then consider $G(s, t) = F(s, 1 - t)$.

* $G$ is continuous because
    * $t \mapsto 1 - t$ is continuous.
    * $s \times t \mapsto s \times (1 - t)$ is continuous since it is a product of two continuous functions.
    * A composition of continuous functions is continuous.
* $G(s, 0) = F(s, 1) = g(s)$.
* $G(s, 1) = F(s, 0) = f(s)$.
* $G(0, t) = F(0, 1 - t) = p$.
* $G(1, t) = F(1, 1 - t) = q$.

Therefore, $G$ is a path homotopy from $g$ to $f$, so $g$ is path-homotopic to $f$.

## Transitive property

Suppose $f$ is path-homotopic to $g$ and $g$ is path-homotopic to $h$.
Let $F$ be a path homotopy from $f$ to $g$, and $G$ be a path homotopy from $g$ to $h$.
Then consider $H: I \times I \rightarrow X$ such that

$$
\begin{align*}
  H(s, t) &= \begin{cases}
    F(s, 2t) & (t \in [0, 1/2]) \\
    G(s, 2t - 1) & (t \in [1/2, 1]).
  \end{cases}
\end{align*}
$$

* Is $H$ well-defined?
    * $\forall s \in I, H(s, 1/2) = F(s, 1) = g(1) = G(s, 0) = H(s, 1/2)$.
* $H$ is continuous by the gluing lemma.
* $H(s, 0) = F(s, 0) = f(s)$.
* $H(s, 1) = G(s, 1) = h(s)$.
* $H(0, t) = F(0, 2t) = p$.
* $H(1, t) = G(1, 2t - 1) = q$.

Therefore, $H$ is a path homotopy from $f$ to $h$, so $f$ is path-homotopic to $h$.

Hence, path homotopy is an equivalence relation.
