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
Let $\phi: A \rightarrow \mathscr{B}$ be defined such that for all $\alpha \in A$

* $\phi(\alpha) \ne \emptyset$.
* $\phi(\alpha) \subset i_{\alpha}(X_{\alpha})$.

Since $i_{\alpha}$ is an open map, $i_{\alpha}(X_{\alpha})$ is open.
Since $X_{\alpha}$ is nonempty, $i_{\alpha}(X_{\alpha})$ is nonempty.
Thus, there must exist a nonempty basis element that is contained in $i_{\alpha}(X_{\alpha})$.
This guarantees the existence of $\phi$.

We claim that $\phi$ is injective.
If it is, that implies that the cardinality of $\mathscr{B}$ is greater than or equal to that of $A$.

Suppose $\phi(\alpha_1) = \phi(\alpha_2)$ for some $\alpha_1, \alpha_2 \in A$.

Let $(x, \alpha) \in \phi(\alpha_1)$ be given.
This is possible because $\phi(\alpha_1)$ must be nonempty.
Since $\phi(\alpha_1) \subset i_{\alpha_1}(X_{\alpha_1})$, $\alpha = \alpha_1$.

Using the same logic, since $(x, \alpha) \in \phi(\alpha_1) = \phi(\alpha_2)$, $\alpha = \alpha_2$.

Therefore, $\alpha_1 = \alpha_2$.

Since $\phi$ is injective and $A$ is uncountable, $\mathscr{B}$ must be uncountable.
