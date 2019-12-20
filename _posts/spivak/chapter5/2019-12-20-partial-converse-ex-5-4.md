---
layout: post
title:  "Partial converse of Theorem 5-1[Spivak]"
date:   2019-12-20
author: Hidenori
---

# Proposition
Prove a partial converse of Theorem 5-1:
If $M \subset \mathbb{R}^n$ is a $k$-dimensional manifold and $x \in M$, then there is an open set $A \subset \mathbb{R}^n$ containing $x$ and a differentiable function $g: A \rightarrow \mathbb{R}^{n - k}$ such that $A \cap M = g^{-1}(0)$ and $g'(y)$ has rank $n - k$ when $g(y) = 0$.

# Solution
Let $x \in M$.
Then there exists an open set $U$ around $x$ and an open set $V \subset \mathbb{R}^n$ with a diffeomorphism $f: U \rightarrow V$ such that $f(U \cap M) = V \cap (\mathbb{R}^k \times \\{ 0 \\})$.
Let $p: V \rightarrow \mathbb{R}^{n - k}$ be defined such that $p(x^1, \cdots, x^n) = (x^{n - k + 1}, \cdots, x^n)$.
$p$ is the projection map of the last $n - k$ coordinates, so $p$ is differentiable.

Let $g = p \circ f$.
Since $f$ and $p$ are differentiable, $g$ is a differentiable function from $U$ into $\mathbb{R}^{n - k}$.

$$
\begin{align*}
  g^{-1}(\{ 0 \})
    &= f^{-1}(p^{-1}(\{ 0 \})) \\
    &= f^{-1}(V \cap (\mathbb{R}^k \times \{ 0 \})) \\
    &= U \cap M.
\end{align*}
$$

Let $y \in U$ be given such that $g(y) = 0$.
Then $Dg(y) = Dp(f(y))Df(y)$.
$Df(y)$ is invertible because $f$ is invertible.
Thus the rank of $Dg(y)$ equals the rank of $Dp(f(y))$.

$$
\begin{align*}
  Dp(f(y)) &= \begin{bmatrix}
    0 & 0 \\
    0 & I_{n - k}
  \end{bmatrix}.
\end{align*}
$$

Thus the rank of $Dp(f(y)) = n - k$.
