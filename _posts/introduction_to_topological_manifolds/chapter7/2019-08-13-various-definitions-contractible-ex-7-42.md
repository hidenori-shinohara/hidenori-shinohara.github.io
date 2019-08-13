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
Suppose that $X$ is homotopy equivalent to a one-point space $Y = \\{ y \\}$.
Let $x_0 \in X$.
We will show that $\\{ x_0 \\}$ is a deformation retract of $X$.

Let $f_1: \\{ x_0 \\} \rightarrow \\{ y \\}, f_2: \\{ y \\} \rightarrow \\{ x_0 \\}$.
Then $f_1 \circ f_2$ and $f_2 \circ f_1$ are both the identity maps on $\\{ y \\}$ and $\\{ x_0 \\}$, respectively.
Thus $\\{ x_0 \\}$ is homotopy equivalent to $\\{ y \\}$.

Since [homotopy equivalence is an equivalence relation]({{ site.baseurl }}{% post_url /introduction_to_topological_manifolds/chapter7/2019-08-10-homotopy-equivalence-ex-7-36 %}), $X$ is homotopy equivalent to $\\{ x_0 \\}$.

Then there exists a continuous map $F: X \times I \rightarrow X$ such that

* $F(x, 0) = x_0$ for all $x \in X$.
* $F(x, 1) = x$ for all $x \in X$.

Let $r: X \rightarrow \\{ x_0 \\}$ be defined such that $r(x) = F(x, 0)$.
* $r$ is a constant function, so it is continuous.
* $r$ fixes $x_0$.

Thus, $r$ is a retraction.
Moreover, $F$ is a homotopy from $i_{\\{ x_0 \\}} \circ r$ to the identity map of $X$.
Therefore, $\\{ x_0 \\}$ is a deformation retract of $X$.

## $3 \rightarrow 1$
TODO
