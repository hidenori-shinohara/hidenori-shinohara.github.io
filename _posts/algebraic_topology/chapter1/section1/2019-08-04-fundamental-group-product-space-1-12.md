---
layout: post
title:  "$\\pi_1(X \\times Y)$ is isomorphic to $\\pi_1(X) \\times \\pi_1(Y)$ if $X$ and $Y$ are path-connected."
date:   2019-08-04
author: Hidenori
---

# Proposition
$\pi_1(X \times Y)$ is isomorphic to $\pi_1(X) \times \pi_1(Y)$ if $X$ and $Y$ are path-connected.

# Solution
By Theorem 18.4 from Munkres, a function is continuous if and only if all of its coordinate functions are continuous.

Let $(x_0, y_0) \in (X \times Y)$.

Let $\phi: \pi_1(X \times Y, (x_0, y_0)) \rightarrow \pi_1(X, x_0) \times \pi_1(Y, y_0)$ be defined such that $\phi([(g, h)]) = [g] \times [h]$ for all $[(g, h)] \in \pi_1(X \times Y)$.
We claim that $\phi$ is a group isomorphism.

* Well-defined?
    * $\phi(\pi_1(X \times Y)) \subset \pi_1(X, x_0) \times \pi_1(Y, y_0)$?
        * Let $[(g, h)] \in \pi_1(X \times Y, (x_0, y_0))$.
          Then $(g, h)$ is a loop in $X \times Y$ and let $(x_0, y_0)$ denote the base point.
          Then $g$ maps $I$ into $X$ continuously and $g(0) = g(1) = x_0$.
          Thus $g$ is a loop in $X$.
          Similarly, $h$ is a loop in $Y$.
          Thus $[g] \in \pi_1(X, x_0)$ and $[h] \in \pi_1(Y, y_0)$, so $\phi([(g, h)]) \in \pi_1(X, x_0) \times \pi_1(Y, y_0)$.
    * Suppose $[(g, h)] = [(g', h')]$.
      Let $F(s, t)$ be a homotopy from $(g, h)$ to $(g', h')$.
      Then $\pi_1 \circ F$ and $\pi_2 \circ F$ are homotopies from $g$ to $g'$ and $h$ to $h'$, respectively.
      Thus $g \simeq g'$ and $h \simeq h'$, so $\phi([(g, h)]) = \phi([(g', h')])$.
* Group homomorphism?
    * Let $[(g_1, h_1)], [(g_2, h_2)] \in \pi_1(X \times Y, (x_0, y_0))$.

      $$
      \begin{align*}
        \phi([(g_1, h_1)] * [(g_2, h_2)])
          &= \phi([(g_1 * g_2, h_1 * h_2)]) \\
          &= [g_1 * g_2] \times [h_1 * h_2] \\
          &= ([g_1] \times [h_1]) * ([g_2] \times [h_2]) \\
          &= \phi([(g_1, h_1)]) * \phi([(g_2, h_2)]).
      \end{align*}
      $$

* Injective?
    * If $\phi([(g, h)]) = e$, then $[g] \times [h] = e$, so $[g] = e$ and $[h] = e$.
      This implies that $g$ and $h$ are homotopic to the constant loop in $X$ and $Y$, respectively.
      Thus $[(g, h)] = e$.
* Surjective?
    * Let $[g] \times [h] \in \pi_1(X) \times \pi_1(Y)$.
      Then $g, h$ are loops based at $x_0, y_0$.
      Thus $(g, h)$ is a loop based at $(x_0, y_0)$.
      Since $\phi([(g, h)]) = [g] \times [h]$, $\phi$ is surjective.

Thus $\phi$ is an isomorphism.
