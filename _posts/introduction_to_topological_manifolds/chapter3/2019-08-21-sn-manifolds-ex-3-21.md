---
layout: post
title:  "$S^n$ is an $n$-manifold"
date:   2019-08-21
author: Hidenori
---

# Proposition
For each $n \in \mathbb{N}$, $S^n = \\{ x \in \mathbb{R}^{n + 1} \mid \abs{x} = 1 \\}$ is an $n$-manifold.

# Solution
Let $n \in \mathbb{N}$ be given.
We will show that $S^n$ is an $n$-manifold.
Since $S^n$ is a subspace of $\mathbb{R}^{n + 1}$, it is Hausdorff and second countable.
We will show that $S^n$ is locally Euclidean.
Let $a = (a_1, \cdots, a_{n + 1}) \in S^n$.
Since $a_1^2 + \cdots + a_{n + 1}^2 = 1$, there must exists an $i$ such that $a_i \ne 0$.

First, we will assume $a_i > 0$.

Let $U = \\{ (x_1, \cdots, x_{n + 1}) \in \mathbb{R}^{n + 1} \mid x_i > 0 \\}$.
Then $U$ is an open set subset of $\mathbb{R}^{n + 1}$.
Therefore, $U \cap S^n$ is an open subset of $S^n$.
Since $a \in U \cap S^n$, $U \cap S^n$ is a neighborhood of $a$ in $S^n$.

Let $V = \\{ x \in \mathbb{R}^n \mid \abs{x} < 1 \\} $.
Let $f(x_1, \cdots, x_{n - 1}) = (x_1, \cdots, x_{i - 1}, \sqrt{1 - x_1^2 - \cdots - x_{n - 1}^2}, x_i, \cdots, x_{n - 1})$.
Then $f$ maps $V$ into $U \cap S^n$.
We claim that this is a homeomorphism.

* Well defined?
    * $x_1^2 + \cdots + x_{i - 1}^2 + (1 - x_1^2 - \cdots - x_{n - 1}^2) + x_i^2 + \cdots + x_{n - 1}^2 = 1$.
    * Since $\sqrt{1 - x_1^2 - \cdots - x_{n - 1}^2} > 0$, $f$ indeed maps $V$ into $U \cap S^n$.
* Continuous?
    * Each component function is continuous, so it is continuous.
* Injective?
    * Suppose $f(x_1, \cdots, x_{n - 1}) = f(y_1, \cdots, y_{n - 1})$.
      Then $x_1 = y_1, x_2 = y_2, \cdots, x_{n - 1} = y_{n - 1}$.
* Surjective?
    * Let $x_1, \cdots, x_{n + 1} \in U \cap S^n$.
      Then $x_1^2 + \cdots + x_{n + 1}^2 = 1$.
      Moreover, $x_i > 0$.
      Therefore, $x_i = \sqrt{x_1^2 + \cdots + x_{i - 1}^2 + x_{i + 1}^2 + \cdots + x_{n + 1}^2}$.
* Continuous inverse?
    * The inverse function is $(\pi_1, \pi_2, \cdots, \pi_{i - 1}, \pi_{i + 1}, \cdots, \pi_{n + 1})$ where each $\pi_k$ is the projection of the $k$-th coordinate.
      Since each coordinate function is continuous, the inverse is continuous.

Thus $f$ is indeed a homeomorphism, so $V$ is homeomorphic to $U \cap S^n$.
This means that we found a neighborhood of $a$ that is homemorphic to an open subset of $\mathbb{R}^n$.
$a$ was chosen arbitrarily, so this means $S^n$ is locally Euclidean.
Thus $S^n$ is an $n$-manifold.

The case for $a_i < 0$ is similar.
