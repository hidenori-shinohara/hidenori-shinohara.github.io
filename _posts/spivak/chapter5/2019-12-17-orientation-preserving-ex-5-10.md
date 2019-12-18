---
layout: post
title:  "Orientation preserving(WIP)"
date:   2019-12-17
author: Hidenori
---

# Proposition
Suppose $\mathcal{C}$ is a collection of coordinate systems for $M$ such that

1. For each $x \in M$, there is $f \in \mathcal{C}$ which is a coordinate system around $x$;
1. if $f, g \in \mathcal{C}$, then $\det(f^{-1} \circ g)' > 0$.

Show that there is a unique orientation of $M$ such that $f$ is orientation-preserving if $f \in \mathcal{C}$.

# Solution
Let $x \in M$.
Let $f \in \mathcal{C}$ be a coordinate system around $x$ such that $f:W \rightarrow \mathbb{R}^n$.
Let $a = f^{-1}(x) \in \mathbb{R}^k$.
Let $$\mu_x = [f_*((e_1)_a), \cdots, f_*((e_k)_a)]$$.

Using the procedure above, we can define $\mu_x$ for each $x \in M$.

* Is this independent of the choice of $f$?

Let $x \in M$ and $f, g \in \mathcal{C}$ be coordinate systems around $x$.
Let $a, b$ be chosen such that $f(a) = g(b) = x$.
Then $f^{-1} \circ g$ maps $\mathbb{R}^k$ into itself and $\det(f^{-1} \circ g)' > 0$, so

$$
\begin{align*}
  &[(f^{-1} \circ g)_*((e_1)_b), \cdots, (f^{-1} \circ g)_*((e_k)_b)] = [(e_1)_{f^{-1}(g(b))}, \cdots, (e_1)_{f^{-1}(g(b))}] \\
  &\implies [f_*(f^{-1} \circ g)_*((e_1)_b), \cdots, f_*(f^{-1} \circ g)_*((e_k)_b)] = [f_*((e_1)_{f^{-1}(g(b))}), \cdots, f_*((e_1)_{f^{-1}(g(b))})] \\
  &\implies [g_*((e_1)_b), \cdots, g_*((e_k)_b)] = [f_*((e_1)_{a}), \cdots, f_*((e_1)_{a})]

\end{align*}
$$

Therefore, the choice of orientation $\mu_x$ is independent of the choice of a coordinate system.

* Is the orientation consistent?

Let $f: W \rightarrow \mathbb{R}^n$ and $a, b \in W$ be given.
Then $f$ is a coordinate system around $a$ and $b$.
Thus by the definition of $\mu$ and the above argument regarding independence of a choice, $$[f_*((e_1)_a), \cdots, f_*((e_1)_a)] = \mu_{f(a)}$$ and $$[f_*((e_1)_b), \cdots, f_*((e_1)_b)] = \mu_{f(b)}$$.
Therefore, the orientation is consistent.

* Is $f$ orientation preserving for each $f \in \mathcal{C}$?

TODO
