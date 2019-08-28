---
layout: post
title:  "The diagonal is closed if and only if the space is Hausdorff"
date:   2019-08-28
author: Hidenori
---

# Proposition
Let $X$ be a topological space.
The diagonal of $X \times X$ is the subset $\delta = \\{ (x, x) \mid x \in X \\} \subset X \times X$.
Show that $X$ is Hausdorff if and only if $\delta$ is closed in $X \times X$.

# Solution
Suppose $X$ is Hausdorff.
Let $(a, b) \in \delta^c$.
Then $a \ne b$, so there exist disjoint neighborhoods $U_a, U_b$ of $a, b$, respectively.

Then we claim $U_a \times U_b \cap \delta = \emptyset$.
Suppose otherwise.
Let $(c, d) \in U_a \times U_b \cap \delta$.
Then $(c, d) \in \delta$, so $c = d$.
This implies that $c = d \in U_a \cap U_b$, which is a contradiction.
Thus the intersection must be empty.

Therefore, $a \times b \in U_a \times U_b \subset \delta^c$.
Since $U_a \times U_b$ is a basis element for the product topology $X \times X$, $\delta^c$ is open.
Therefore, $\delta$ is closed.

Suppose, on the contrary, that $\delta$ is closed.
Let $(a, b) \in \delta^c$.
Since $\delta^c$ is open, there must exist a basis element $U_a \times U_B$ for the product topology $X \times X$ such that $(a, b) \in U_a \times U_b \subset \delta^c$.

Since $U_a \times U_b \subset \delta^c$, $U_a \cap U_b = \emptyset$.
Thus $U_a, U_b$ are disjoint neighborhoods of $a, b$, respectively.

Therefore, $X$ is Hausdorff.


