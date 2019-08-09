---
layout: post
title:  "Every homomorphism of $\\pi_1(S^1)$ is induced by a map from $S^1$ into $S^1$."
date:   2019-08-09
author: Hidenori
---

# Proposition
Show that every homomorphism $\pi_1(S^1) \rightarrow \pi_1(S^1)$ can be realized as the induced homomorphism $$\phi_*$$ of a map $\phi: S^1 \rightarrow S^1$.

# Solution
Instead of $\mathbb{R}^2$, we will regard the plane as $\mathbb{C}$.
Then the loop $f(t) = e^{2\pi it}$ is a generator by Theorem 1.7 (Hatcher).

Let a homomorphism $F: \pi_1(S^1) \rightarrow \pi_1(S^1)$ be given.
Then $F([f]) = [f]^k$ for some $k \in \mathbb{Z}$.
This is because every element in $\pi_(S^1)$ is an integer power of $[f]$.

Then $[f]^k = [e^{2k\pi it}]$ because $[f]^k = [w]^k$ and $[e^{2k\pi it}] = [(\cos 2\pi kt, \sin 2\pi kt)]$ as mentioned in the proof for Theorem 1.7 (Hatcher).
Consider $G: \mathbb{C} \rightarrow \mathbb{C}$ such that $G(x) = x^k$.
Let $[f]^l \in \pi_1(S^1)$ be given.

* For any $[f]^l \in \pi_1(S^1)$, $F([f]^l) = (F([f]))^l = ([f]^k)^l = [f]^{kl} = [e^{2kl\pi it}]$.
* For any $[f]^l \in \pi_1(S^1)$, $$G_*([f]^l) = G_*([e^{2l\pi it}]) = [G(e^{2l\pi it})] = [e^{2kl\pi it}]$$ 

Therefore, $$F = G_*$$.


