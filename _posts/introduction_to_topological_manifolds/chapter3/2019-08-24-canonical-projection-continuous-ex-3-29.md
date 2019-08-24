---
layout: post
title:  "Each canonical projection is continuous"
date:   2019-08-24
author: Hidenori
---

# Proposition
If $X_1, \cdots, X_n$ are topological spaces, each canonical projection $\pi_i: X_1 \times \cdots \times X_n \rightarrow X_i$ is continuous.

# Solution
We will use the Characteristic Property of the Product Topology (Theorem 3.27, Introduction to Topological Manifolds).
The identity function $f: X_1 \times \cdots \times X_n \rightarrow X_1 \times \cdots \times X_n$ is continuous because any identity function is continuous.

By the Characteristic Property of the Property Topology, $f$'s continuity implies the continuity of $\pi_i \circ f$ for each $i$.
Since $f$ is the identity map, $\pi_i \circ f = \pi_i$ for each $i$.
Therefore, each $\pi_i$ is continuous.
