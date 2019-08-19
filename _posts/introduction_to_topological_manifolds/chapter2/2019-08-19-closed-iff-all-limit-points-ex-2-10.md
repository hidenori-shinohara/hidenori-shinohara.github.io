---
layout: post
title:  "Show that a subset of a topological space is closed if and only if it contains all of its limit points"
date:   2019-08-19
author: Hidenori
---

# Proposition
Show that a subset of a topological space is closed if and only if it contains all of its limit points.

# Solution
Suppose $A$ is closed.
Let $x \notin A$.
$A^c$ is a neighborhood of $x$ that does not contain a point of $A$.
Thus $x$ is not a limit point of $A$.
By taking the contrapositive, if $x \in X$ is a limit point of $A$, $x \in A$.
In other words, $A$ contains all of its limit points.

Suppose that $A$ contains all of its limit points.
Let $x \in A^c$.
Then $x$ is not a limit point of $A$, so there must exist an open set $U$ such that $x \in U$ and $U$ does not contain a point of $A$ other than $x$.
Since $x \notin A$, $U$ does not contain any point of $A$.
This implies that $x \in U \subset A^c$, so $A^c$ is open.
Therefore, $A$ is closed.
