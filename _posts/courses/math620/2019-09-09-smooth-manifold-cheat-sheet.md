---
layout: post
title:  "Cheat Sheet (Smooth Manifolds)"
date:   2019-09-09
author: Hidenori
---

* TOC
{:toc}

# Notes
## Vectors and derivations

* In this class, vectors and derivations seem to be synonyms.

## Fields
A _*something*_ field on _*set*_  = a function that assigns _*something*_ to each point of _*set*_.

* Examples
    * Vector field on $M$
        * A function that assigns a vector to each point of $M$.

## Star
For any vector space $V$, $V^*$ denotes $L(V, \mathbb{R})$, the set of all linear maps from $V$ to $\mathbb{R}$.

## Functions
There seem to be two types of functions in this class:
1. Assignment function
    * They assign a certain mathematical object to each point.
1. Signed length meter
    * They take 1 or more values and return a real number.
    * They can be seen as a generalization of the determinant function.
      The determinant function gets $n$ column vectors and returns the signed volume of the parallelepiped.
      For instance, we have a covector, which takes a vector (=derivation) and returns a number.
      This can be seen as finding the length of the vector.

# Definitions

## Push forwards ($F_*$ and $dF$)
Let $F: U \rightarrow V$ be a smooth map where $U \subset \mathbb{R}^n, V \subset \mathbb{R}^m$.

* $F_*$ is called a push forward of $F$.
    * There are two different definitions of push forwards.
        * The other (simpler) definition is:
        * Given $F: M \rightarrow N$, $$F_*: T_pM \rightarrow T_{F(p)}N$$ is defined such that $$(F_*X)(f) = X(f \circ F)$$ for any $X \in T_pM$ and $f \in \mathscr{C}^{\infty}(N)$.
        * $F_*$ takes a derivation $X$ in $M$ and turn that into another derivation in $N$.
* $F_*: TU \rightarrow TV$.
    * The lecture notes say $dF = F_*$, but I'm not sure what that means.
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

## Pull backs ($F^*$)
Let $F: M \rightarrow N, p \in M$.
Then the pullback $$F^*: T^*_{F(p)}M \rightarrow T^*_p N$$ associated with $F$ is defined by

$$
\begin{align*}
  \forall \zeta \in T^*_{F(p)}(N), X \in T_pM, (F^* \zeta)(X) = \zeta(F_*X).
\end{align*}
$$

## Vector fields

* A vector field $Y$ on $M$ assigns a vector to each point in $M$.
* Formally, a vector field is a function $Y: M \rightarrow TM$ such that, for all $p \in M$, $Y(p) = (p, X)$ for some $X \in T_pM$.
* $Y(p)$ is often denoted by $Y_p$. See P.60.
* Since $TM$ is a disjoint union, its elements is a pair $(p, X)$.
  However, it seems that we often think of $Y_p$ as a derivation instead of a pair of a point and a derivation.
* The textbook says "A vector field on $M$ is a section of $TM$", which I believe means the same thing.

## Covector fields $df$
Let $f$ be a smooth map on $M$.

Then $df$ denotes a covector field.

This is defined such that $\forall p \in M, \forall X_p \in T_pM, df_p(X_p) = X_pf$.

This sorta makes sense because

* $df$ is a covector field.
* $df_p$ is a covector, so it takes a vector.
* $X_p$ is a vector, so it takes a smooth map.
* Thus $X_pf$ is a real number.
* This means $df_p$ takes a vector and returns a real number, which is exactly what a covector should do.

## Set of all smooth vector fields ($\mathfrak{X}(M)$)

$\mathfrak{X}(M)$ denotes the set of all smooth vector fields on $M$.
There doesn't seem to be a name for $\mathfrak{X}(M)$.

* $\mathfrak{X}(M)$ is NOT a vector field. Each element in $\mathfrak{X}(M)$ is a vector field.
* $\mathfrak{X}(M)$ is a vector *space* over $\mathbb{R}$.
* Moreover, $\mathfrak{X}(M)$ is a module over $\mathscr{C}^{\infty}(M)$.
    * $\forall Y \in \mathfrak{X}(M), \forall f \in \mathscr{C}^{\infty}(M), \forall p \in M, (fY)(p) = f(p)Y_p$.
* Reference
    * Textbook P.60
    * P.62 discusses notations


## Tangent Space ($T_pM$)
$T_pM$ denotes the set of all derivations at $p$.

* $\\{ \partial_1, \cdots, \partial_n \\}$ is a basis of $T_p\mathbb{R}^n$.
  This implies that every derivation in $\mathbb{R}^n$ can be expressed as a linear combination of partial derivatives.

## Tangent Bundle ($TM$)

* $TM = \coprod_{p \in M} T_pM$ is called the tangent bundle of $M$.
* See P.57.
* Let $\pi: TM \rightarrow M$ be defined such that $\pi(p, X) = p$ for each $(p, X) \in TM$.
  We call $\pi$ the *projection map*.
* An element of $TM$ is denoted by $(p, X), X_p$, or simply $X$ for convenience. See P.57.
* It is the collection of all vectors on $M$.

## Cotangent space ($T_p^*M$)

$T_p^{*}M = L(T_pM, \mathbb{R})$ is the cotangent space at $p$.

Each element of $T_p^*M$ is called a (tangent) covector.
See P.68.

* Vector
    * In this class, vector = derivation = arrow.
* Covector
    * A covector assigns a number to a vector.
      One can think of this as a signed length, just like $\det$ gives a signed volume to a set of column vectors.

## Cotangent bundle ($$T^*M$$)

$$T^*M = \coprod_{p \in M} T^*_pM$$ is the cotangent bundle on $M$.
In other words, it is the collection of all covectors on $M$.

## Local framing
There are different types of local framings, but they are very similar.
## Local framing of a tangent bundle
A local framing of $TM$ over $U$ is a collection $\{ x_1, \cdots, x_n \} \subset \mathfrak{X}(U)$ such that $\{ x_{1, p}, \cdots, x_{n, p} \}$ is a basis of $T_pM$ for all $p \in U$.

* $x_1, \cdots, x_n$ are vector fields, so $x_{1, p}$ is a derivation at $p \in U$.
* It makes sense that $\{ x_{1, p}, \cdots, x_{n, p} \}$ might be a basis of $T_pM$ because $T_pM$ is the set of all derivations at $p$, and $x_{i, p}$ is a derivation at $p$.
* $\{ \frac{\partial}{\partial x^1}, \cdots, \frac{\partial}{\partial x^n} \} \subset \mathfrak{X}(U)$ is a global framing.

![Local framing](/assets/courses/math620/framing.jpeg)

## Local framing of a cotangent bundle
$\\{ \eta^1, \cdots, \eta^n \\} \subset \mathscr{A}^1(U)$ is called a local framing of $T^kM$ if $\forall p \in U$, $\\{ \eta^1_p, \cdots, \eta^n_p \\}$ is a basis of $$T_p^*M$$.

This sorta makes sense because:

* For each $i$, $\eta^i$ is a 1-form.
  In other words, $\eta^i$ assigns a covector to each point.
* $\eta^i_p$ is a covector for each $i$ and $p \in U$, so $\\{ \eta^1_p, \cdots, \eta^n_p \\}$ is a set of covectors at $p$.
* $$T_p^*M$$ is the collection of all covectors at $p$, so $\\{ \eta^1_p, \cdots, \eta^n_p \\}$ is indeed a subset of $$T_p^*M$$.


## Local section (1-form)
A 1-form is a smooth covector field.

A map $\eta: U \rightarrow T^*M$ is called a local section of $$T^*M$$ over $U$ if $\pi \circ \eta = \Id_U$.
In other words, $\eta$ assigns a covector of $p$ to $p$, instead of a covector of a different point.

It is said to be smooth if $\forall X \in \mathfrak{X}(U)$, $p \mapsto \eta_p(X_p)$ is smooth.
This statement makes sense because:
* $X$ is a vector field, so $X_p$ is a vector.
* $\eta$ assigns a covector to each point, so $\eta_p$ is a covector.
* Thus $\eta_p(X_p)$ means that we pass a vector to a covector.

A local section assigns a covector to each point.
In other words, a local section provides us with a way to assigned a signed length to each derivation.

## Set of all 1-forms ($\mathscr{A}^1(U)$)

$\mathscr{A}^1(U)$ is the set of all 1-forms on $U$.

* $\mathscr{A}^1(U)$ itself is not a 1-form.
  It contains 1-forms.
* $\mathscr{A}^1(U)$ is a vector space over $\mathscr{C}^{\infty}(U)$.
* 1-form assigns a covector to each point.
  Thus $\mathscr{A}^1(U)$ is the set of all different ways to assign covectors to points.
  
## $k$-forms ($\bigwedge^k(T^*_p\mathbb{R}^n), \mathscr{A}^k$)

The $k$-th exterior power of the cotangent bundle is the disjoint union

$$
\begin{align*}
  \bigwedge^k T^*\mathbb{R}^n = \coprod_{p \in \mathbb{R}^n} \bigwedge^k(T^*_p\mathbb{R}^n)
\end{align*}
$$

A function $$\eta: \mathbb{R}^n \rightarrow \bigwedge^kT^*\mathbb{R}^n$$ is called a $k$-form if

* $$\eta_p \in \bigwedge^kT_p^{*}\mathbb{R}^n$$.
* Let $X_i \in \mathfrak{X}(\mathbb{R}^n)$ be given.
  Then we can define $F: \mathbb{R}^n \rightarrow \mathbb{R}$ such that $F(p) = \eta_p(X_{1, p}, \cdots, X_{k, p})$.
  Such an $F$ must be smooth for all $X_i$'s.

The set of all $k$-forms is denoted by $\mathscr{A}^k(\mathbb{R}^n)$.
The set of all $k$-forms is called $\mathscr{A}^k$ because $\mathscr{A}$ looks like $\bigwedge$ (See P.212).

This sorta makes sense because:

* $\eta_p$ is in $\bigwedge^kT^*\mathbb{R}^n$.
  $\eta_p$ is an alternating $k$-tensor, so it takes $k$ vectors.
* $X_1, \cdots, X_k$ are vector fields, so $X_{1, p}, \cdots, X_{k, p}$ are vectors.
* Thus $\eta_p(X_{1, p}, \cdots, X_{k, p})$ is a real number. 

I like the textbook's definition better.

> A smooth section of $\bigwedge^kM$ is called a differential $k$-form, or just a $k$-form;
> this is just a smooth tensor field whose value at each point is an alternating tensor.

Note that the textbook uses $\bigwedge^k T\mathbb{R}^n$ to mean $\bigwedge^k T^*\mathbb{R}^n$ in this class.

## Wedge product ($\wedge$)

$$
\begin{align*}
  (\mu^1 \wedge \cdots \wedge \mu^k)(v_1, \cdots, v_k)
    &= \sum_{\sigma \in S^k} \sgn(\sigma)\mu^{\sigma_1}(v_1) \cdots \mu^{\sigma_k}(v_k).
\end{align*}
$$

$$
\begin{align*}
  (\tau \wedge \omega)(v_1, \cdots, v_{k + l})
    &= \frac{1}{k!l!} \sum_{\sigma \in S_{k + l}} \sgn(\sigma)(\tau(v_{\sigma_1}, \cdots, v_{\sigma_k})\omega(v_{\sigma_{k + 1}}, \cdots, v_{\sigma_{k + l}})).
\end{align*}
$$

## Pullback of a $k$-form
Let $U \subset \mathbb{R}^n, V \subset \mathbb{R}^m, \eta \in \mathscr{A}^k(V), F: U \rightarrow V$.
We will define $$F^*\eta$$ to be a $k$-form on $V$.
In other words, $$F^*\eta \in \mathscr{A}^k(V)$$.

Let $p \in U$.
Then $(F^*\eta)_p$ is defined such that

$$
\begin{align*}
  \forall v_1, \cdots, v_k \in T_pU, (F^*\eta)_p(v_1, \cdots, v_k) = \eta_{F(p)}(F_* v_1, \cdots, F_* v_k).
\end{align*}
$$


This sorta makes sense because:

* $v_1, \cdots, v_k$ are vectors in $U$.
* The [push-forward](#push-forwards-f_-and-df) $$F_*$$ maps $T_pU$ into $T_pV$.
  In other words, $$F_*$$ maps a vector in $U$ to a vector in $V$.
* $$F_* v_1, \cdots, F_* v_k$$ are vectors in $V$.
* $\eta$ is a $k$-form, which is an assignment of an alternating $k$-tensor to each point of $V$.
  So, $\eta_{F(p)}$ is an alternating $k$-tensor of $V$.
* Thus $\eta_{F(p)}$ takes $F_* v_1, \cdots, F_* v_k$ as arguments, and returns a real number.
  So, $(v_1, \cdots, v_k) \mapsto \eta_{F(p)}(F_* v_1, \cdots, F_* v_k)$ is an alternating $k$-tensor.
* This means $F^*\eta \in \mathscr{A}^k(U)$, and $$(F^*\eta)_p \in \bigwedge^k(T_pU)$$.
* With this definition, $F^*$ maps $\mathscr{A}^k(V)$ into $\mathscr{A}^k(U)$.
  In other words, $k$-forms pull back to $k$-forms.
* $\displaystyle F^*(dy^s) = \frac{\partial F^s}{\partial x^i} dx^i$. 

## Diffeomorphisms

A diffeomorphism $U \subset \mathbb{R}^n$ to $V \subset \mathbb{R}^n$ is a smooth map $F = (f^1, \cdots, f^n) : U \rightarrow V$ that has a smooth inverse.

Some formulas
* Chain rule: $\displaystyle \frac{\partial}{\partial x^a} = \frac{\partial f^i}{\partial x^a}\frac{\partial}{\partial y^i}$ where $y_i = f^i(x)$.
    * If we let $G = F^{-1}$, then $\displaystyle \frac{\partial}{\partial y^a} = \frac{\partial g^j}{\partial y^a}\frac{\partial}{\partial x^j}$.
