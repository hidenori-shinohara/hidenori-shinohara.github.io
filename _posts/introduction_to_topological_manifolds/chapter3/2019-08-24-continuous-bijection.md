---
layout: post
title:  "A continuous bijection from a compact space into a Hausdorff space is a homeomorphism"
date:   2019-08-24
author: Hidenori
---

# Proposition
Let $f: X \rightarrow Y$ be a continuous bijection.
If $X$ is compact and $Y$ is Hausdorff, then $f$ is a homeomorphism.

# Solution
It suffices to show that $f$ is an open map.
Let $U \subset X$ be open.
We will show that $f(U)$ is open.
Let $f(x) \in f(U)$ be given.
It makes sense to identify each point in $Y$ with $f(x)$ because $f$ is bijective.
For each $f(y) \in Y \setminus f(U)$, there exist disjoint neighborhoods $V_y, W_y$ of $f(x), f(y)$, respectively.

We claim that $\\{ f^{-1}(W_y) \mid y \in X \setminus U \\}$ is an open cover of $X \setminus U$.

* Since $f$ is continuous, each $f^{-1}(W_y)$ is open.
* For each $y \in X \setminus U$, $f(y) \in W_y$, so $y \in f^{-1}(W_y)$.

Since $X \setminus U$ is compact, there exists a finite sequence $y_1, y_2, \cdots, y_n$ such that $f^{-1}(W_{y_1}), \cdots, f^{-1}(W_{y_n})$ cover $X \setminus U$.
Since $f$ is bijective, this means $W_{y_1}, \cdots, W_{y_n}$ cover $f(X \setminus U) = Y \setminus f(U)$.
Let $V = V_{y_1} \cap V_{y_2} \cap \cdots \cap V_{y_n}$.
Then $V$ is a neighborhood of $f(x)$ in $Y$.
Moreover, $V$ is disjoint from $W_{y_1} \cup \cdots \cup W_{y_n}$.
Therefore, $V$ is disjoint from $Y \setminus f(U)$, so $V \subset f(U)$.

This implies that $f(x)$ is an interior point of $f(U)$, so $f(U)$ is an open set in $Y$.
Hence, $f$ is a homeomorphism.
