---
layout: post
title:  "$X$ is disconnected if and only if there exists a non-constant function to a discrete, two-point set."
date:   2019-08-17
author: Hidenori
---

# Proposition
Prove that a topological space $X$ is disconnected if and only if there exists a non-constant function from $X$ to the discrete space $\\{ 0, 1 \\}$.

# Solution
Suppose $X$ is disconnected.
Then there exist a pair of disjoint, open sets $U, V$ such that $U \cup V = X$.
Let $f: X \rightarrow \\{ 0, 1 \\}$ be defined such that

$$
\begin{align*}
  f(x) = \begin{cases}
    0 & (x \in U) \\
    1 & (x \in V).
  \end{cases}
\end{align*}
$$

* $f$ is non-constant because $U$ and $V$ are nonempty.
* Is $f$ continuous?
    * There are exactly $4$ open subsets of $\\{ 0, 1 \\}$.
        * $f^{-1}(\emptyset) = \emptyset$.
        * $f^{-1}(\\{ 0 \\}) = U$.
        * $f^{-1}(\\{ 1 \\}) = V$.
        * $f^{-1}(\\{ 0, 1 \\}) = X$.
    * Therefore, $f^{-1}(S)$ is open for any open $S \subset \\{ 0, 1 \\}$.

On the contrary, suppose that there exists a non-constant function from $X$ to the discrete space $\\{ 0, 1 \\}$
Let $f$ be such a function.
Let $U = f^{-1}(\\{ 0 \\})$ and $V = f^{-1}(\\{ 1 \\})$.
Then $\\{ 0 \\}$ and $\\{ 1 \\}$ are both open in $\\{ 0, 1 \\}$, and $f$ is continuous, so $U$ and $V$ are both open.
Since $f^{-1}(\\{ 0, 1 \\}) = X$ and $f^{-1}(\\{ 0, 1 \\}) = f^{-1}(\\{ 0 \\}) \cup f^{-1}(\\{ 1 \\}) = U \cup V$, $X = U \cup V$.
$U \cap V = \emptyset$ because there exists no element $x \in X$ such that $f(x) = 0$ and $f(x) = 1$.
Therefore, $U, V$ are disjoint open sets whose union equals $X$.
