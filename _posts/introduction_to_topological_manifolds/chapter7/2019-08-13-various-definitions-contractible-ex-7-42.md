---
layout: post
title:  "Various ways to define a contractible space"
date:   2019-08-13 10:00:00
author: Hidenori
---

# Proposition
Show that the following are equivalent:
1. $X$ is contractible.
1. $X$ is homotopy equivalent to a one-point space.
1. Each point of $X$ is a deformation retract of $X$.

# Solution

## $1 \rightarrow 2$
Let $X$ be a contractible space.
Then there exists a point $p \in X$ and a continuous map $H: X \times I \rightarrow X$ such that

* $\forall x \in X, H(x, 0) = x$.
* $\forall x \in X, H(x, 1) = p$.


Let $\phi: X \rightarrow \\{ p \\}$ map every element in $X$ to $p$.
Let $\psi: \\{ p \\} \rightarrow X$ be the inclusion map.

* $\phi \circ \psi$ is the identity map for $\\{ p \\}$.
  Thus it is indeed homotopic to the identity map for $\\{ p \\}$.
* $\psi \circ \phi$ maps every point in $X$ to $p$.
  Then $H$ is a homotopy from the identity map for $X$ to $\psi \circ \phi$.
  Therefore, $\psi \circ \phi$ is homotopic to the identity map for $X$.

Thus $X$ is homotopy equivalent to $\\{ p \\}$, a one-point space.

## $2 \rightarrow 3$
TODO

## $3 \rightarrow 1$
TODO
