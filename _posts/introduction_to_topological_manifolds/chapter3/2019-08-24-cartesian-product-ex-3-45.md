---
layout: post
title:  "Cartesian products and disjoint unions"
date:   2019-08-24
author: Hidenori
---

# Proposition
Let $X$ be any space and $Y$ be a discrete space.
Show that the Cartesian product $X \times Y$ is equal to the disjoint union $\coprod_{y \in Y} X$, and the product topology is the same as the disjoint union topology.

# Solution

$$
\begin{align*}
  \coprod_{y \in Y} X
    &= \bigcup_{y \in Y} X \times \{ y \} \\
    &= \bigcup_{y \in Y} \{ x \times y \mid x \in X \} \\
    &= \{ x \times y \mid x \in X, y \in Y \} \\
    &= X \times Y.
\end{align*}
$$

Let $\mathscr{B}_X$ be a basis of $X$, $\mathscr{T}_X$ be the topology of $X$.
Let $\mathscr{B}_Y = \\{ \\{ y \\} \mid y \in Y \\}$ be a basis of $Y$.
Then $\mathscr{B}_X \times \mathscr{B}_Y$ is a basis for the product topology $\mathscr{T}_p$ of $X \times Y$.

Let $U_0 \times \\{ y_0 \\} \in \mathscr{B}_X \times \mathscr{B}_Y$ be given.
Then $$U_0 \times \{ y_0 \} = \coprod_{y \in Y} V_y$$ where

$$
\begin{align*}
  V_y &= \begin{cases}
    U_0 & (y = y_0) \\
    \emptyset & (y \ne y_0).
  \end{cases}
\end{align*}
$$

For any $y \in Y$, the intersection of $\coprod_{y \in Y} V_y$ with $X$ (there is only one $X$, but the $X$ that corresponds to the $y$) is $V_y$.
Since each $V_y$ is open in $X$, $\coprod_{y \in Y} V_y$ is open in the disjoint union topology.
Therefore, this implies that the disjoint union topology is finer than the product topology.

Let $U \subset \coprod_{y \in Y} X$ be an open set.
For each $y \in Y$, let $U_y$ denote the intersection of $U$ with $X$ for the index $y$.
Each $U_y$ is open because $U$ is open.
Then $U = \coprod_{y \in Y} U_y = \bigcup_{y \in Y} U_y \times \\{ y \\}$.
Then each $U_y \times \\{ y \\}$ is a basis element in $\mathscr{B}_X \times \mathscr{B}_Y$.
Therefore, $U$ is open in the product topology, so the product topology is finer than the disjoint union topology.

Hence, the product topology and the disjoint union topology are the same.
