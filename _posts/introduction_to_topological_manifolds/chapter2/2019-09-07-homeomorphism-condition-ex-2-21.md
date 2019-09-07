---
layout: post
title:  "Condition for a homeomorphism to become a bijection"
date:   2019-09-07
author: Hidenori
---

# Proposition
Let $(X_1, \mathcal{T}_1)$ and $(X_2, \mathcal{T}_2)$ be topological spaces and let $f: X_1 \rightarrow X_2$ be a bijective map.
Show that $f$ is a homeomorphism if and only if $f(\mathcal{T}_1) = \mathcal{T}_2$ in the sense that $U \in \mathcal{T}_1$ if and only if $f(U) \in \mathcal{T}_2$.

# Solution

Suppose $f$ is a homeomorphism.
Since $f$ is open, $f(U) \in \mathcal{T}_2$ for any $U \in \mathcal{T}_1$.
Let $U \subset X_1$.
Suppose $f(U) \in \mathcal{T}_2$.
Since $f$ is continuous, $f^{-1}(f(U)) \in \mathcal{T}_1$.
Since $f$ is bijective, $f^{-1}(f(U)) = U$.
Thus $U \in \mathcal{T}_1$.

Suppose $U \in \mathcal{T}_1$ if and only if $f(U) \in \mathcal{T}_2$.
Then $f$ is open because $f(U)$ is open for each open $U$.
Let $U \in \mathcal{T}_2$.
Then $f(f^{-1}(U)) = U$ since $f$ is bijective.
Since $f(f^{-1}(U))$ is open in $\mathcal{T}_2$, $f^{-1}(U)$ is open in $\mathcal{T}_1$.
Thus $f$ is continuous.
Therefore, $f$ is a homeomorphism.
