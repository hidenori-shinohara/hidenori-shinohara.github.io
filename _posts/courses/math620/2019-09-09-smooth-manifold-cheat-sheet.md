---
layout: post
title:  "Cheat Sheet (Smooth Manifolds)"
date:   2019-09-09
author: Hidenori
---

# Vectors and derivations

* In this class, vectors and derivations seem to be synonyms.

# Push forwards
Let $F: U \rightarrow V$ be a smooth map where $U \subset \mathbb{R}^n, V \subset \mathbb{R}^m$.

* $dF$ and $F_*$ are called push forwards of $F$.
    * There are two different definitions of push forwards.
* $dF = F_*: TU \rightarrow TV$.
* Definition
    * Let $(v, p) \in TU$. 
      Let $\gamma: (-\epsilon, \epsilon) \rightarrow U$ be a curve such that $\gamma'(0) = v$.
      Then $F_*(v) = (F \circ \gamma)'(0)$.
    * Theorem
        * For each $j \in \\{ 1, \cdots, n \\}$, $\displaystyle F_*\begin{pmatrix}\frac{\partial}{\partial x^j}\end{pmatrix} = \sum_{s=1}^{m} \frac{\partial F^s}{\partial x^j} \frac{\partial}{\partial y^s}$.

# Vector fields
TODO

# Fields
An $X$ field on $Y$ = a function that assigns an element of $X$ to each point of $Y$ (in a smooth way).

* Examples
    * Vector field on $M$
        * A function that assigns a vector to each point of $M$.
