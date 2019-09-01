---
layout: post
title:  "A subset is dense if and only if every nonempty open subset of $X$ contains a point of $A$" 
date:   2019-09-01
author: Hidenori
---

# Proposition
Show that a subset $A \subset X$ is dense if and only if every nonempty open subset of $X$ contains a point of $A$.

# Solution
Suppose $A \subset X$ is dense.
Let $U \subset X$ be a nonempty open subset.
Suppose that $U$ contains no point of $A$.
Then $A \subset U^c$.
Since $U^c$ is a closed set containing $A$, $\overline{A} \subset U^c$.
Since $U$ is nonempty, $U^c \subsetneq X$.
This implies $\overline{A} \ne X$, which is a contradiction.

On the other hand, suppose that every nonempty open subset of $X$ contains a point of $A$.
Since $\overline{A}$ is a closed set containing $A$, $\overline{A}^c$ is an open subset of $X$ that does not contain a point of $A$.
Therefore, $\overline{A}^c$ must be closed.
In other words, $\overline{A} = X$, so $A$ is dense.
