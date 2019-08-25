---
layout: post
title:  "Open quotient maps and Hausdorff spaces"
date:   2019-08-25
author: Hidenori
---

# Proposition
Suppose $q: X \rightarrow Y$ is an open quotient map.
Then $Y$ is Hausdorff if and only if the set $\mathscr{R} = \\{ (x_1, x_2) \mid q(x_1) = q(x_2) \\}$ is closed in $X \times X$.

# Solution
First, we will suppose that $Y$ is Hausdorff.
We will show that $\mathscr{R}$ is closed in $X \times X$.
Let $(a, b) \in X \times X \setminus \mathscr{R}$.
Then $q(a) \ne q(b)$.

Since $Y$ is Hausdorff, there must exist disjoint neighborhoods $U, V$ of $q(a), q(b)$, respectively.
Then $a \in q^{-1}(U), b \in q^{-1}(V)$.
$q$ is a quotient map, so $q^{-1}(U)$ and $q^{-1}(V)$ are both open.
Thus $q^{-1}(U) \times q^{-1}(V)$ is a neighborhood of $(a, b)$.
We claim that this neighborhood is contained in $X \times X \setminus \mathscr{R}$.
Let $(c, d) \in q^{-1}(U) \times q^{-1}(V)$.

* $q(c) \in q(q^{-1}(U)) = U$ because $q$ is surjective.
* $q(d) \in q(q^{-1}(V)) = V$ because $q$ is surjective.

Since $U \cap V = \emptyset$, $q(c) \ne q(d)$.
Therefore, $(c, d) \in X \times X \setminus \mathscr{R}$.
Thus $X \times X \setminus \mathscr{R}$ is open, so $\mathscr{R}$ is closed.

On the other hand, suppose that the set $\mathscr{R} = \\{ (x_1, x_2) \mid q(x_1) = q(x_2) \\}$ is closed in $X \times X$.
We will show that $Y$ is Hausdorff.

Let $y_1 \ne y_2 \in Y$.
Since $q$ is surjective, there exist $x_1, x_2 \in X$ such that $q(x_1) = y_1, q(x_2) = y_2$.
Since $q(x_1) = y_1 \ne y_2 = q(x_2)$, $(x_1, x_2) \notin \mathscr{R}$.
Since $\mathscr{R}$ is closed, the complement is open.
Therefore, $X \times X \setminus \mathscr{R}$ is a neighborhood of $(x_1, x_2)$.
Thus there must exist a basis element $U_1 \times U_2$ such that $(x_1, x_2) \in U_1 \times U_2 \subset X \times X \setminus \mathscr{R}$ where $U_1, U_2$ are open in $X$.
Then $(y_1, y_2) = (q(x_1), q(x_2)) \in q(U_1) \times q(U_2)$.
Since $q$ is open, $q(U_1), q(U_2)$ are both open.
Therefore, they are neighborhoods of $y_1, y_2$, respectively.

We claim that $q(U_1) \cap q(U_2) = \emptyset$.
Suppose otherwise.
Let $y \in q(U_1) \cap q(U_2)$.
Then there exists an $a_1 \in U_1$ such that $q(a_1) = y$.
Similarly, there exists an $a_2 \in U_2$ such that $q(a_2) = y$.
Then $(a_1, a_2) \in \mathscr{R}$.
However, since $(a_1, a_2) \in U_1 \times U_2 \subset X \times X \setminus \mathscr{R}$, $(a_1, a_2)$ cannot be an element of $\mathscr{R}$.
Therefore, $q(U_1) \cap q(U_2) = \emptyset$.

Then $q(U_1), q(U_2)$ are disjoint neighborhoods of $y_1, y_2$, so $Y$ is Hausdorff.
