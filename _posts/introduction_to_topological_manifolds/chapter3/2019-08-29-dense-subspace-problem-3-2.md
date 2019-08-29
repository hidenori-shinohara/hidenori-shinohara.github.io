---
layout: post
title:  "A dense subspace"
date:   2019-08-29
author: Hidenori
---

# Proposition
Suppose $X$ is a topological space and $A \subset B \subset X$.
Show that $A$ is dense in $X$ if and only if $A$ is dense in $B$ and $B$ is dense in $X$.

# Solution
Suppose that $A$ is dense in $X$.
Since the closure of a set is the intersection of all closed sets containing it, $A \subset B$ implies $\overline{A} \subset \overline{B}$.
Since $A$ is dense in $X$, $\overline{A} = X$.
Therefore, $\overline{B} = X$.

Suppose $A$ is dense in $B$ and $B$ is dense in $X$.

Then $\cl_B(A) = B$ and $\cl_X(B) = X$.
Suppose that $\cl_X(A) \ne X$.
Then there exists an $x \in X \setminus \cl_X(A)$.
Since $\cl_X(A)$ is the intersection of all closed sets containing $A$, there must exist a closed set $C$ in $X$ such that $A \subset C$ and $x \notin C$.

* $C \cap B$ is a closed set in $B$.
* $x \notin C \cap B$.
* $A \subset C \cap B$.

Therefore, $x \notin \cl_B(A)$ and $\cl_B(A) \subset C \cap B$.
Then $B = \cl_B(A) \subset C \cap B \subset C$.

This implies that $\cl_X(B) \subset C \subsetneq X$.
This is a contradiction because we assumed that $B$ is dense in $X$.
Therefore, there exists no such $x$.
