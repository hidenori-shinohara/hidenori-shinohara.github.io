---
layout: post
title:  "Continuous maps preserve the path homotopy relation"
date:   2019-08-12
author: Hidenori
---

# Proposition
The path homotopy relation is preserved by composition with continuous maps.
That is, if $f_0, f_1: I \rightarrow X$ are path-homotopic and $\phi:X \rightarrow Y$ is continuous, then $\phi \circ f_0$ and $\phi \circ f_1$ are path-homotopic.

# Solution
Suppose $f_0$ and $f_1$ are paths from $x_0$ to $x_1$, and they are path-homotopic.
Let $F: I \times I \rightarrow X$ be a path homotopy from $f_0$ to $f_1$.
We claim that $\phi \circ F$ is a path homotopy from $\phi \circ f_0$ to $\phi \circ f_1$.

* $\phi \circ F$ is a composition of continuous functions, so it is continuous.
* $(\phi \circ F)(0, t) = \phi(f_0(t))$.
* $(\phi \circ F)(1, t) = \phi(f_1(t))$.
* $(\phi \circ F)(s, 0) = \phi(x_0)$.
* $(\phi \circ F)(s, 1) = \phi(x_1)$.

Therefore, $\phi \circ F$ is indeed a path homotopy from $\phi \circ f_0$ to $\phi \circ f_1$.
