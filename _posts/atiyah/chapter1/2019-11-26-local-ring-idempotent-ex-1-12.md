---
layout: post
title:  "A local ring contains no idempotent $\\ne 0, 1$"
date:   2019-11-26
author: Hidenori
---

# Proposition
A local ring contains no idempotent $\ne 0, 1$.

# Solution
Let $A$ be a local ring that contains no idempotent $\ne 0, 1$.

Let $x$ be an idempotent $\ne 0, 1$.
If no such element exists, we are done.

Suppose it is a unit and let $y$ be the inverse of $x$.
Then $x^2 = x$ implies $y(x^2) = yx$, so $x = 1$.
This is a contradiction, so $x$ is not a unit.

Let $m$ be the maximal ideal of $A$.
Since $m$ is the only maximal ideal, the Jacobson radical $\mathfrak{R} = m$.

By Corollary 1.5[Atiyah], $x$ is contained in a maximal ideal since $x$ is not a unit.
Since there is only one maximal ideal, $x \in m$.
Therefore, $x \in \mathfrak{R}$.

By Proposition 1.9, $1 - xy$ must be a unit in $A$ for all $y \in A$.
Let $y = x$.
Then $(1 - x^2)^2 = (1 - x)^2 = 1 - 2x + x^2 = 1 - x^2$.
Therefore, $1 - x^2 = 1 - x$ is an idempotent.
Since $x \ne 0, 1$, $1 - x \ne 0, 1$.
Using the same argument as above, we conclude that $1 - x$ is not a unit.
Therefore, this is a contradiction, so there cannot be an idempotent $\ne 0, 1$.
