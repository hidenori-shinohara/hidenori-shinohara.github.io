---
layout: post
title:  "Closure and interior"
date:   2019-08-29
author: Hidenori
---

# Proposition
Suppose $X$ is a topological space and $U \subset S \subset X$.

1. Show that the closure of $U$ in $S$ is equal to $\overline{U} \cap S$.
1. Show that the interior of $U$ in $S$ contains $\Int{U} \cap S$; give an example to show that they might not be equal.

# Solution

## 1

Let $\mathscr{C}$ be the set of all closed sets in $X$.
Let $\mathscr{C}_S$ be the set of all closed sets in $S$.
Then $\mathscr{C}_S = \\{ C \cap S \mid C \in \mathscr{C} \\}$.

$$
\begin{align*}
  \cl_S(U)
    &= \bigcap_{C \in \mathscr{C}_S, U \subset C} C \\
    &= \bigcap_{C \in \mathscr{C}, U \subset C \cap S} (C \cap S) \\
    &= [\bigcap_{C \in \mathscr{C}, U \subset C \cap S} C] \cap S \\
    &= [\bigcap_{C \in \mathscr{C}, U \subset C} C] \cap S \\
    &= \overline{U} \cap S.
\end{align*}
$$

## 2
Let $x \in \Int{U} \cap S$.
Since $x \in \Int{U}$, $x$ has a neighborhood $N$ of $x$ in $X$ such that $N \subset U$.
Then $N \cap S$ is open in $S$ and it contains $x$.
Thus $N \cap S$ is contained in the interior of $U$ in $S$.
Thus $x$ is in the interior of $U$ in $S$.

Consider $X = \mathbb{R}, S = U = [0, 1]$.
Then $\Int{U} \cap S = (0, 1) \cap [0, 1] = (0, 1)$.
On the other hand, the interior of $U$ in $S$ is $U$ because $U$ is open in $S$.
This is an example where they might not be equal.
