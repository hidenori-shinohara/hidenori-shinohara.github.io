---
layout: post
title:  "Properties of the Zariski topology(WIP)"
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
TODO

## 3
TODO

## 4
TODO

## 5
TODO

## 6
TODO

## 7
TODO
