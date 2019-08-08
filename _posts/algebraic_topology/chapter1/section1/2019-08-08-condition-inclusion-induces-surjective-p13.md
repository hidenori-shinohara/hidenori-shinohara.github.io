---
layout: post
title:  "The condition when an inclusion map induces a surjective homomorphism."
date:   2019-08-08
author: Hidenori
---

# Proposition
Given a space $X$ and a path-connected subspace $A$ containing the basepoint $x_0$, show that the map $\pi_1(A, x_0) \rightarrow \pi_1(X, x_0)$ induced by the inclusion $A \rightarrow X$ is surjective iff every path in $X$ with endpoints in $A$ is homotopic to a path in $A$.

# Solution

First, suppose that $$i_*$$ is surjective.
Let $p_a, p_b \in A$ and $h$ be a path in $X$ from $p_a$ to $p_b$.
Since $A$ is path-connected, let $a, b$ denote paths from $x_0$ to $p_a, p_b$, respectively.

Then $a \cdot h \cdot \overline{b}$ is a loop based at $x_0$, so $[a \cdot h \cdot \overline{b}] \in \pi_1(X, x_0)$.
Since $$i_*$$ is surjective, there must exist a $[f] \in \pi_1(A, x_0)$ such that $$i_*([f]) = [a \cdot h \cdot \overline{b}]$$.
Then $[i \circ f] = [a \cdot h \cdot \overline{b}]$.
This implies $[\overline{a} \cdot (i \circ f) \cdot b] = [h]$, and $\overline{a} \cdot (i \circ f) \cdot b$ is a path in $A$.
Therefore, any path in $X$ with endpoints in $A$ is homotopic to a path in $A$.

Next, suppose that every path in $X$ with endpoints in $A$ is homotopic to a path in $A$.
Let $[f] \in \pi_1(X, x_0)$.
Then $f$ is a loop in $X$ based at $x_0$.
Thus it must be homotopic to a path in $A$.
Let $g$ be such a path.
Then $[g] \in \pi_1(A, x_0)$, so $$i_*([g]) = [i \circ g] = [g] = [f]$$, so $$i_*$$ is surjective.
