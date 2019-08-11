---
layout: post
title:  "$f(\\mathcal{B})$ is a basis if and only if $f$ is surjective and open"
date:   2019-08-11
author: Hidenori
---

# Proposition

Let $f: X \rightarrow Y$ be a continuous map between topological spaces, and let $\mathcal{B}$ be a basis for the topology of $X$.
Let $f(\mathcal{B})$ denote the collection $\\{ f(B) : B \in \mathcal{B} \\}$ of subsets of $Y$.
Show that $f(\mathcal{B})$ is a basis for the topology of $Y$ if and only if $f$ is surjective and open.

# Solution
Suppose that $f(\mathcal{B})$ is a basis for $Y$.
Let $U \subset X$.
Then $U = \bigcup B_{\alpha}$ for some $\\{ B_{\alpha} \\} \subset \mathcal{B}$.
$f(U) = f(\bigcup B_{\alpha}) = \bigcup f(B_{\alpha})$.
For each $\alpha$, $f(B_{\alpha})$ is a basis element for $Y$, so $\bigcup f(B_{\alpha})$ is open in $Y$.
Therefore, $f$ is an open map.

$Y$ is open in $Y$, so there exists a subset $\\{ f(B_{\alpha}) \\} \subset f(\mathcal{B})$ such that $\bigcup f(B_{\alpha}) = Y$.
Thus $Y = \bigcup f(B_{\alpha}) = f(\bigcup B_{\alpha}) \subset f(X) \subset Y$, so $f(X) = Y$.

Therefore, $f$ is both surjective and open.

On the contrary, suppose that $f$ is both surjective and open.
We will show that $f(\mathcal{B})$ is a basis for $Y$.
Let $V \subset Y$ be an open set and $y \in V$.
Since $f$ is surjective, there exists an $x \in X$ such that $f(x) = y$.
Since $f$ is continuous, $f^{-1}(V)$ is open in $X$.
Since $f(x) = y \in V$, $x \in f^{-1}(V)$.

$\mathcal{B}$ is a basis for $X$, so there must exist a basis element $B \in \mathcal{B}$ such that $x \in B \subset f^{-1}(V)$.
Then $f(x) \in f(B) \subset f(f^{-1}(V)) = V$.
Therefore, $f(\mathcal{B})$ is a basis for $Y$ by [this exercise](hello).
