---
layout: post
title:  "The set of limit points of $A \\subset X$ is closed in $X$"
date:   2019-08-11
author: Hidenori
---

# Proposition
Let $X$ be a Hausdorff space, let $A \subset X$, and let $A'$ denote the set of limit points of $A$.
Show that $A'$ is closed in $X$.

# Solution
Let $x \in X \setminus A'$.
Then $x$ is not a limit point of $A$.
This implies that $x$ has a neighborhood $U$ such that $(U \setminus \\{ x \\}) \cap A = \emptyset$.
Since $X$ is Hausdorff, $\\{ x \\}$ is closed.
(See Proposition 2.37 on P.32 of Introduction to Topological Manifolds.)
Thus $U \setminus \\{ x \\}$ is open.

Let $y \in U \setminus \\{ x \\}$.
Then $U \setminus \\{ x \\}$ is $y$'s neighborhood that does not intersect $A$ at all.
Therefore, $y$ is not a limit point of $A$.

This implies that $x \in U \subset X \setminus A'$.
Therefore, $X \setminus A'$ is open in $X$, so $A'$ is closed in $X$.


