---
layout: post
title:  "Properties of topological groups"
date:   2019-08-17
author: Hidenori
---

# Proposition
Let $G$ be a [topological group](https://en.wikipedia.org/wiki/Topological_group).

1. Prove that up to isomorphism, $\pi_1(G, g)$ is independent of the choice of the base point $g \in G$.
1. Prove that $\pi_1(G, g)$ is abelian.

# Solution

## 1
Let $g_1, g_2 \in G$.
Let $\phi: G \rightarrow G$ be defined such that $\phi(g) = g_2g_1^{-1}g$.
We claim that $\phi$ is a homeomorphism.

* Is $\phi$ continuous?
    * Let $f_1:G \rightarrow G \times G$ be defined such that $f_1(g) = (g, g)$.
      Then $f_1$ is continuous since each coordinate function is the identity map.
      Let $f_2: G \times G \rightarrow G \times G$ be defined such that $f_2(g, h) = (g_2g_1^{-1}, h)$.
      Then $f_1$ is continuous since the first coordinate function is a constant function, and the second coordinate function is the identity.
      The multiplication operation is continuous because $G$ is a topological group.
      Then a composition of those functions must be continuous, and $\phi$ is precisely the composition of multiplication, $f_2$ and $f_1$.
* Is $\phi$ injective? 
    * Let $g, h \in G$.
      Suppose $\phi(g) = \phi(h)$.
      Then $g_2g_1^{-1}g = g_2g_1^{-1}h$, so $g = h$.
* Is $\phi$ surjective?
    * Let $g \in G$.
      Then $g_1g_2^{-1}g \in G$, and $\phi(g_1g_2^{-1}g) = (g_2g_1^{-1})(g_1g_2^{-1})g = g$.
* Is $\phi^{-1}$ continuous?
    * Since $\phi$ is bijective, $\phi$ indeed has an inverse.
      The inverse is defined by $\psi(g) = g_1g_2^{-1}g$.
      (This can be verified by confirming that $\phi \circ \psi$ and $\psi \circ \phi$ are both the identity map.)
      Using the same logic as above, we can confirm that $\psi$ is continuous.

Therefore, $\phi$ is indeed a homeomorphism.
It is known that a homeomorphism induces an isomorphism between the fundamental groups.
For instance, see Proposition 7.26 of Introduction to Topological Manifolds.

## 2
By 1, it suffices to show that $\pi_1(G, e)$ is abelian.
Let $[f], [g] \in \pi_1(G, e)$.

Then both $f$ and $g$ map $I$ into $G$ continuously.

* $(s, t) \mapsto (f(s), g(t))$ is continuous since each component function is continuous.
* $(f(s), g(t)) \mapsto f(s)g(t)$ is continuous since multiplication is continuous.

Therefore, $F(s, t) = f(s)g(t)$ is continuous.

* $F(s, 0) = f(s)e = f(s)$.
* $F(1, s) = f(1)g(s) = g(s)$.
* $F(0, s) = f(0)g(s) = g(s)$.
* $F(s, 1) = f(s)g(1) = f(s)$.

Therefore, by [the square lemma]({{ site.baseurl }}{% post_url /introduction_to_topological_manifolds/chapter7/2019-08-15-square-lemma-pr-7-4 %}), $[f \cdot g] = [g \cdot f]$.
Hence, $[f][g] = [g][f]$, so $\pi_1(G, e)$ is abelian.
