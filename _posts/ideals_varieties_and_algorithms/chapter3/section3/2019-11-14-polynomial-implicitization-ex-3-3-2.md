---
layout: post
title:  "Polynomial implicitization and the closure theorem"
date:   2019-11-14
author: Hidenori
---

# Proposition
When $k = \mathbb{C}$, the conclusion of Theorem 1 (P.134, Ideals, Varieties and Algorithms) can be strengthened.
Namely, one can show that there is a variety $W \subsetneq V(I_m)$ such that $V(I_m) \setminus W \subset F(\mathbb{C}^m)$.
Prove this using the Closure Theorem. (P.131, Ideals, Varieties and Algorithms).

# Solution
Let $F(t_1, \cdots, t_m) = (f_1(t_1, \cdots, t_m), \cdots, f_n(t_1, \cdots, t_m))$ be given.
Let $I = \ev{x_1 - f_1, \cdots, x_n - f_n} \subset \mathbb{C}[t_1, \cdots, t_m, x_1, \cdots, x_n]$.
Let $V = V(I) \subset \mathbb{C}^{m + n}$.
We first claim that $\pi_m(V) = F(\mathbb{C}^m)$.

Let $(x_1, \cdots, x_n) \in \mathbb{C}^n$ be given.

$$
\begin{align*}
  (x_1, \cdots, x_n) \in \pi_m(V)
    &\iff \exists (t_1, \cdots, t_m) \in \mathbb{C}^m, (t_1, \cdots, t_m, x_1, \cdots, x_n) \in V \\
    &\iff \exists (t_1, \cdots, t_m) \in \mathbb{C}^m, \forall i, f_i(t_1, \cdots, t_m) = x_i \\
    &\iff (x_1, \cdots, x_n) \in F(\mathbb{C}^m).
\end{align*}
$$

$V \ne \emptyset$ because $(0, \cdots, 0, f_1(0, \cdots, 0), \cdots, f_n(0, \cdots, 0)) \in V$.
By the Closure Theorem, there is an affine variety $W \subsetneq V(I_m)$ such that $V(I_m) \setminus W \subset \pi_m(V) = F(\mathbb{C}^m)$, which is the desired result.
