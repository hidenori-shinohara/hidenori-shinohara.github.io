---
layout: post
title:  "Properties of the Zariski topology"
date:   2019-12-17
author: Hidenori
---

# Proposition
For each $f \in A$, let $X_f$ denote the complement of $V(f)$ in $X = \Spec(A)$.
The sets $X_f$ are open.
Show that they form a basis of open sets for the Zariski topology, and that

1. $X_f \cap X_g = X_{fg}$;
1. $X_f = \emptyset \iff f$ is nilpotent;
1. $X_f = X \iff f$ is a unit;
1. $X_f = X_g \iff r((f)) = r((g))$;
1. $X$ is quasi-compact;
1. More generally, each $X_f$ is quasi-compact.
1. An open subset of $X$ is quasi-compact if and only if it is a finite union of sets $X_f$.

# Solution

## Basis
* $X_1 = (V(1))^c = \emptyset^c = X$.
  Thus the union of all $X_f$ is $X$.
* Let $X_{f_1}, X_{f_2}$ be given.

  $$
  \begin{align*}
    X_{f_1} \cap X_{f_2}
      &= V(f_1)^c \cap V(f_2)^c \\
      &= (V(f_1) \cup V(f_2))^c \\
      &= (V(\ev{f_1}) \cup V(\ev{f_2}))^c \\
      &= (V(\ev{f_1}\ev{f_2}))^c \\
      &= (V(\ev{f_1f_2}))^c \\
      &= (V(f_1f_2))^c \\
      &= X_{f_1f_2}.
  \end{align*}
  $$

  We showed that $V(\ev{f_1}) \cup V(\ev{f_2}) = V(\ev{f_1}\ev{f_2})$ [in this post](/2019/11/27/zariski-topology-ex-1-15.html).
  Therefore, $\forall x \in X_{f_1} \cap X_{f_2}, x \in X_{f_1f_2} \subset X_{f_1} \cap X_{f_2}$.

Hence, $\\{ X_f \mid f \in A \\}$ is a basis for the Zariski topology.

## 1
By definition, $X_f = \\{ p \in \Spec(A) \mid f \notin p \\}$ for each $f$.
Since every set in $\Spec(A)$ is a prime ideal, $\forall p \in \Spec(A), \forall f, g \in A$,

$$
\begin{align*}
  fg \notin p \iff f \notin p \text{ and } g \notin p.
\end{align*}
$$

Therefore, $X_f \cap X_g = X_{fg}$.

## 2

$$
\begin{align*}
  X_f = \emptyset
    &\iff \forall p \in \Spec(A), f \in p \\
    &\iff f \in \cap_{p \in \Spec(A)} p \\
    &\iff f \in \mathfrak{R} & \text{(By Proposition 1.8[Atiyah])} \\
    &\iff \text{$f$ is nilpotent}
\end{align*}
$$

## 3
$$
\begin{align*}
  X_f = X
    &\iff \forall p \in \Spec(A), f \notin p.
\end{align*}
$$

Suppose $X_f = X$.
Every non-unit element is contained in some maximal ideal by Corollary 1.5 [Atiyah].
Since every maximal ideal is prime, $f$ must be a unit element.

On the other hand, since every prime ideal is a proper ideal, a unit is not contained in any prime ideal.

Therefore, $X_f = X$ if and only if $f$ is a unit.

## 4

$$
\begin{align*}
  r((f)) = r((g))
    &\iff \bigcap_{p \in \Spec(A), (f) \subset p} p = \bigcap_{p \in \Spec(A), (g) \subset p} p & \text{(Proposition 1.14)} \\
    &\iff \bigcap_{p \in \Spec(A), f \in p} p = \bigcap_{p \in \Spec(A), g \in p} p.
\end{align*}
$$

On the other hand, $(X_f = X_g \iff V(f) = V(g)) \iff (\forall p \in \Spec(A), f \in p \iff g \in p)$.

We claim that 

$$
\begin{align*}
  (\bigcap_{p \in \Spec(A), f \in p} p = \bigcap_{p \in \Spec(A), g \in p} p) \iff \forall p \in \Spec(A), f \in p \iff g \in p.
\end{align*}
$$

$\impliedby$ is obvious.
Suppose that there exists a prime ideal $p$ such that $f \in p$ and $g \notin p$.
Then $g \notin \bigcap_{p \in \Spec(A), f \in p} p$ and $g \in \bigcap_{p \in \Spec(A), g \in p} p$.
Using a similar argument for the case that $f \notin p$ and $g \in p$, $\implies$ can be shown.


## 5
$X_1 = X$ by Part 3.
By Part 6, $X$ is quasi-compact.

## 6
Let $f \in X$ be given.
Let $$\{ U_{\alpha} \}_{\alpha \in I}$$ be an open cover of $X_f$.
Let $V_{\alpha} = U_{\alpha} \cap X_f$ for each $\alpha \in I$.
Then $\\{ V_{\alpha} \\}$ is an open cover of $X_f$ such that $X_f = \bigcup_{\alpha \in I} V_{\alpha}$.
We will show that $\\{ V_{\alpha} \\}$ contains a finite cover.

Then $X \setminus V_{\alpha}$ is closed for each $\alpha \in I$.
By definition, each closed set in the Zariski topology is of the form of $V(a)$ for some ideal $a$.
Thus there exists an ideal $a_{\alpha}$ such that $X \setminus V_{\alpha} = V(a_{\alpha})$ for each $\alpha \in I$.

$$
\begin{align*}
  X_f
    &= \bigcup_{\alpha \in I} (X \setminus V(a_{\alpha})) \\
    &= X \setminus (\bigcap_{\alpha \in I} V(a_{\alpha})) \\
    &= X \setminus V(\bigcup_{\alpha \in I} a_{\alpha}) \\
    &= X \setminus V(\sum_{\alpha \in I} a_{\alpha}).
\end{align*}
$$

This implies that $V(f) = V(\sum a_{\alpha})$, thus

$$
\begin{align*}
  \bigcap_{p \in \Spec(A), f \in p} p = \bigcap_{p \in \Spec(A), \sum_{\alpha \in I} a_{\alpha} \subset p} p.
\end{align*}
$$

By Proposition 1.8, $r((f)) = r(\sum a_{\alpha})$.
Then $f \in r((f)) = r(\sum a_{\alpha})$, so $f^m \in \sum a_{\alpha}$.
This implies the existence of $x_{\alpha_1} \in a_{\alpha_1}, \cdots, x_{\alpha_n} \in a_{\alpha_n}$ for some $\alpha_1, \cdots, \alpha_n \in I$ such that $f^m = x_{\alpha_1} + \cdots + x_{\alpha_n}$.

$$
\begin{align*}
  (f^m) \subset (x_{\alpha_1}) + \cdots + (x_{\alpha_n}) \subset a_{\alpha_1} + \cdots + a_{\alpha_n}
    &\implies V((f^m)) \supset V(a_{\alpha_1} + \cdots + a_{\alpha_n}) \\
    &\implies V((f)) \supset V(a_{\alpha_1} + \cdots + a_{\alpha_n}) \\
    &\implies (X \setminus V((f))) \subset (X \setminus V(a_{\alpha_1} + \cdots + a_{\alpha_n})) \\
    &\implies X_f \subset (X \setminus V(a_{\alpha_1} \cup \cdots \cup a_{\alpha_n})) \\
    &\implies X_f \subset (X \setminus \cap V(a_{\alpha_i})) \\
    &\implies X_f \subset \bigcup_{i=1}^n V_{\alpha_i} \\
    &\implies X_f \subset \bigcup_{i=1}^n U_{\alpha_i}.
\end{align*}
$$

## 7
A finite union of compact sets is compact, so a finite union of sets $X_f$ is compact.

Let $U$ be a compact, open subset of $X$.
We will show that $U$ is a finite union of sets $X_f$.
Let $C = \\{ X_f \mid f \in A, X_f \subset U \\}$.
$C$ is an open cover because $\\{ X_f \mid f \in A \\}$ is a basis, so every open set is the union of basis elements.
Since $U$ is compact, $U \subset X_{f_1} \cup \cdots \cup X_{f_n}$ for some $X_{f_1}, \cdots, X_{f_n} \in C$.
On the other hand, $X_{f_1} \cup \cdots \cup X_{f_n} \subset U$.
Therefore, $U = X_{f_1} \cup \cdots \cup X_{f_n}$.

