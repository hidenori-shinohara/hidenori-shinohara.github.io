---
layout: post
title:  "A disjoint union of manifolds is manifolds if and only if it is countable"
date:   2019-08-23
author: Hidenori
---

# Proposition
Suppose $$(X_{\alpha})_{\alpha \in A}$$ is an indexed family of nonempty $n$-manifolds.
Show that the disjoint union $$\coprod_{\alpha \in A} X_{\alpha}$$ is an $n$-manifold if and only if $A$ is countable.

# Solution
Suppose $A$ is countable.

By [the properties of disjoint unions that we know]({% post_url introduction_to_topological_manifolds/chapter3/2019-08-22-disjoint-union-space-properties-ex-3-43 %}),

* Since each $X_{\alpha}$ is Hausdorff, $\coprod X_{\alpha}$ is Hausdorff.
* Since each $X_{\alpha}$ is second countable and $A$ is countable, $\coprod X_{\alpha}$ is second countable.

We will show that $\coprod X_{\alpha}$ is locally Euclidean.
Let $(x_0, \alpha_0) \in \coprod X_{\alpha}$ be given.
Then $x_0 \in X_{\alpha_0}$.
Therefore, there exists a neighborhood $U_0$ of $x_0$ with a homeomorphism $\phi_0: U_0 \rightarrow V_0$ where $V_0$ is an open subset of $\mathbb{R}^n$.

Since [$i_{\alpha_0}$ is an open map]({% post_url introduction_to_topological_manifolds/chapter3/2019-08-22-disjoint-union-space-properties-ex-3-43 %}), $i_{\alpha_0}(U_0)$ is a neighborhood of $(x_0, \alpha_0)$.
Since $i_{\alpha_0}$ is a topological embedding, $i_{\alpha_0}^{-1}$ is a homeomorphism from $i_{\alpha_0}(U_0)$ to $U_0$.
Therefore, $\phi_0 \circ i_{\alpha_0}^{-1}$ is a homeomorphism from $i_{\alpha_0}(U_0)$ to $V_0$.

Hence, $\coprod X_{\alpha}$ is locally Euclidean.

Suppose that $A$ is uncountable.
Let $\mathscr{B}$ be be a basis for $$\coprod_{\alpha \in A} X_{\alpha}$$.
For each $\alpha_0 \in A$, $i_{\alpha_0}(X_{\alpha_0})$ is a nonempty open subset of $\coprod X_{\alpha}$.
Then $i_{\alpha_0}(X_{\alpha_0})$ is a union of basis elements.
Since $i_{\alpha_0}(X_{\alpha_0})$ is nonempty, at least one of the basis elements must be nonempty.
Let $B_{\alpha_0}$ denote such an element.

TODO

