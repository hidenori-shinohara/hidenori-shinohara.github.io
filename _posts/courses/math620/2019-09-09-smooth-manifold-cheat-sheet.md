---
layout: post
title:  "Cheat Sheet (Smooth Manifolds)"
date:   2019-09-09
author: Hidenori
---

* TOC
{:toc}

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
* Notes
    * Let $Y$ be a smooth vector field on $U$.
      Let $p \in U$ be given.
      Then $Y_p \in T_pU \subset TU$.
      Thus $$F_*(Y_p) \in TV$$.
      
      This implies that, for each $p \in U$, we get a derivation $$F_*(Y_p)$$ at $F(p)$.
      In other words, for each $F(p) \in V$, we have a derivation $$F_*(Y_p)$$.
      Does this sound like a vector field?
      It does!
      However, the map $$F(p) \mapsto F_*(Y_p)$$ is not necessarily a vector field on $V$.
      For instance, if $F(U) \subsetneq V$, then we won't have a vector assigned to each point.

# Pull backs
Let $F: M \rightarrow N, p \in M$.
Then the pullback $$F^*: T^*_{F(p)}M \rightarrow T^*_p N$$ associated with $F$ is defined by

$$
\begin{align*}
  \forall \zeta \in T^*_{F(p)}(N), X \in T_pM, (F^* \zeta)(X) = \zeta(F_*X).
\end{align*}
$$

# Vector fields

* A vector field $Y$ on $M$ assigns a vector to each point in $M$.
* Formally, a vector field is a function $Y: M \rightarrow TM$ such that, for all $p \in M$, $Y(p) = (p, X)$ for some $X \in T_pM$.
* $Y(p)$ is often denoted by $Y_p$. See P.60.
* Since $TM$ is a disjoint union, its elements is a pair $(p, X)$.
  However, it seems that we often think of $Y_p$ as a derivation instead of a pair of a point and a derivation.
* The textbook says "A vector field on $M$ is a section of $TM$", which I believe means the same thing.

# Set of all smooth vector fields

$\mathfrak{X}(M)$ denotes the set of all smooth vector fields on $M$.
There doesn't seem to be a name for $\mathfrak{X}(M)$.

* $\mathfrak{X}(M)$ is NOT a vector field. Each element in $\mathfrak{X}(M)$ is a vector field.
* Reference
    * Textbook P.60
    * P.62 discusses notations

# Fields
A _*something*_ field on _*set*_  = a function that assigns _*something*_ to each point of _*set*_.

* Examples
    * Vector field on $M$
        * A function that assigns a vector to each point of $M$.

# Tangent Bundle

* $TM = \coprod_{p \in M} T_pM$ is called the tangent bundle of $M$.
* See P.57.
* Let $\pi: TM \rightarrow M$ be defined such that $\pi(p, X) = p$ for each $(p, X) \in TM$.
  We call $\pi$ the *projection map*.
* An element of $TM$ is denoted by $(p, X), X_p$, or simply $X$ for convenience. See P.57.
