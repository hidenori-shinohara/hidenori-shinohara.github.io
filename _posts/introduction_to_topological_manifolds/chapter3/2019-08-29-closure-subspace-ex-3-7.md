---
layout: post
title:  "Closure and interior"
date:   2019-08-29
author: Hidenori
---

# Proposition
Suppose $X$ is a topological space and $U \subset S \subset X$.

1. Show that the closure of $U$ in $S$ is equal to $\overline{U} \cap S$.
1. TODO

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
TODO
