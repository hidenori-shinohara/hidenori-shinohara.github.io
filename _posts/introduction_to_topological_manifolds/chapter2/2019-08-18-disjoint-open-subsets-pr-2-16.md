---
layout: post
title:  "A collection of disjoint open subsets of a second countable topological space is countable"
date:   2019-08-18
author: Hidenori
---

# Proposition
Let $X$ be a second countable topological space.
Show that every collection of disjoint open subsets of $X$ is countable.

# Solution
Let $B = \\{ B_1, B_2, \cdots \\}$ be a countable basis of $X$.
Without loss of generality, assume each $B_i$ is nonempty.

It suffices to show that every collection of disjoint, *nonempty* open subsets of $X$ is countable.

Let $\\{ U_{\alpha} \\} \subset \mathcal{T}$ be given where $I$ is the index set.
Assume $U_{\alpha} \ne \emptyset$ for each $\alpha \in I$.
Suppose that $U_{\alpha} \cap U_{\beta} = \emptyset$ if $\alpha \ne \beta$.
We will show that $I$ is countable.

Let $f: I \rightarrow \mathbb{N}$ be defined such that $$B_{f(\alpha)} \subset U_{\alpha}$$ for each $\alpha \in I$.
Each $$U_{\alpha}$$ is a nonempty, open subset of $X$, so it is the union of at least one basis element.
Therefore, such a function must exist.

Let $\alpha, \beta \in I$.
If $f(\alpha) = f(\beta)$, then $B_{f(\alpha)} \subset U_{\alpha} \cap U_{\beta}$.
Since each basis element is nonempty, this is only possible if $\alpha = \beta$.

Therefore, $f$ is an injective map from $I$ into $\mathbb{N}$, so $I$ is countable.
