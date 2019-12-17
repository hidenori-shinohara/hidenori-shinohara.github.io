---
layout: post
title:  "$\\Spec(A)$ is irreducible if and only if the nilradical of $A$ is prime"
date:   2019-12-17
author: Hidenori
---

# Proposition
Show that $\Spec(A)$ is irreducible if and only if the nilradical of $A$ is a prime ideal.

# Solution
Let $\mathfrak{R}$ denote the nilradical of $A$.
Let $a, b \in A$.
Suppose that $ab \in \mathfrak{R}$.
We will show that $a \in \mathfrak{R}$ or $b \in \mathfrak{R}$.

* Case 1: $V(\\{ a \\})^c$ is empty. 
  Then $V(\\{ a \\}) = \Spec(A)$, so every prime ideal contains $a$.
  Thus $a \in \mathfrak{R}$.
* Case 2: $V(\\{ b \\})^c$ is empty. 
  Similarly, $b \in \mathfrak{R}$.
* Case 3: Neither $V(\\{ a \\})^c$ nor $V(\\{ b \\})^c$ is empty.
  Then $V(\\{ a \\})^c \cap V(\\{ b \\})^c \ne \emptyset$
  Thus there exists $x \in \Spec(A)$ such that $x \notin V(\\{ a \\})$ and $x \notin V(\\{ b \\})$.
  This implies $a \notin p_x$ and $b \notin p_x$.
  This is a contradiction because $ab \in \mathfrak{R} \subset p_x$.
  Therefore, this case is not possible.

Therefore, if $\Spec(A)$ is irreducible then the nilradical is prime.

Suppose $\mathfrak{R}$ is a prime ideal.

[As shown in this post](/2019/12/17/zariski-topology-ex-1-17.html), $\\{ X_f \mid f \in A \\}$ forms a basis for the Zariski topology.
Since every open set is the union of some basis elements [Lemma 13.1, Munkres], it suffices to show that the intersection of any two nonempty basis elements is nonempty.
Let $X_{f_1}, X_{f_2}$ be two nonempty basis elements.
Then $V(f_1) \ne \Spec(A)$ and $V(f_2) \ne \Spec(A)$.
This implies that there exists $p_x \in \Spec(A)$ such that $f_1 \notin p_x$
Since $\mathfrak{R} \subset p_x$, $f_1 \notin \mathfrak{R}$.
Thus $\mathfrak{R} \notin V(f_1)$, so $\mathfrak{R} \in X_{f_1}$.
Similarly, $\mathfrak{R} \in X_{f_2}$.
Thus $X_{f_1} \cap X_{f_2} \ne \emptyset$.
