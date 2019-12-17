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
Let $\mu_x = [f_*((e_1)_a), \cdots, f_*((e_k)_a)]$.

Using the procedure above, we can define $\mu_x$ for each $x \in M$.

* Is this independent of the choice of $f$?
Let $x \in M$ and $f, g \in \mathcal{C}$ be coordinate systems around $x$.
Then $f^{-1} \circ g$ maps $\mathbb{R}^k$ into itself and $\det(f^{-1} \circ g)' > 0$, so

$$
\begin{align*}
  &[(f^{-1} \circ g)_*((e_1)_a), \cdots, (f^{-1} \circ g)_*((e_k)_a)] = [(e_1)_{f^{-1}(g(a))}, \cdots, (e_1)_{f^{-1}(g(a))}] \\
  &\implies [f_*(f^{-1} \circ g)_*((e_1)_a), \cdots, f_*(f^{-1} \circ g)_*((e_k)_a)] = [f_*(e_1)_{f^{-1}(g(a))}, \cdots, f_*(e_1)_{f^{-1}(g(a))}] \\
  &\implies [g_*((e_1)_a), \cdots, g_*((e_k)_a)] = [f_*(e_1)_{f^{-1}(g(a))}, \cdots, f_*(e_1)_{f^{-1}(g(a))}]

\end{align*}
$$

TODO(Finish this!)

* Is the orientation consistent?

TODO

* Is $f$ orientation preserving for each $f \in \mathcal{C}$?

TODO
