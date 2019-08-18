---
layout: post
title:  "A subset of a subspace is closed if and only if it is the intersection with a closed subset"
date:   2019-08-18
author: Hidenori
---

# Proposition
Suppose $S$ is a subspace of $X$.
Prove that a subset $B \subset S$ is closed in $S$ if and only if it is equal to the intersection of $S$ with some closed subset of $X$.

# Solution
Let $B \subset S$.

Suppose that $B$ is closed in $S$.
Then $S \setminus B$ is open in $S$.
By the definition of a subspace topology, $S \setminus B = S \cap U$ for some open $U \subset X$.

We claim that $(X \setminus U) \cap S = B$.

$(X \setminus U) \cap S$ and $B$ are subsets of $S$.
Thus it suffices to check if each point in $S$ is either in both of them or in neither of them.
For any $x \in S$,

$$
\begin{align*}
  x \in (X \setminus U) \cap S
    &\iff x \in X \setminus U \\
    &\iff x \notin U \\
    &\iff x \notin S \cap U \\
    &\iff x \notin S \setminus B \\
    &\iff x \in B.
\end{align*}
$$

Therefore, $B = (X \setminus U) \cap S$ where $X \setminus U$ is closed in $X$.

Suppose that $B = S \cap C$ where $C$ is a closed subset of $X$.

Then $X \setminus C$ is open in $X$.
Then $S \cap (X \setminus C)$ is open in $S$.
We claim that $S \cap (X \setminus C) = S \setminus B$.
Note that each of them is a subset of $S$.
Let $x \in s$.

$$
\begin{align*}
  x \in S \cap (X \setminus C)
    &\iff x \in X \setminus C \\
    &\iff x \notin C \\
    &\iff x \notin S \cap C \\
    &\iff x \notin B \\
    &\iff x \in S \setminus B.
\end{align*}
$$

Therefore, $S \setminus B$ is open in $S$, so $B$ is closed in $S$.
