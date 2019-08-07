---
layout: post
title:  "The fundamental group of a path component"
date:   2019-08-07
author: Hidenori
---

# Proposition
If $X_0$ is the path-component of a space $X$ containing the basepoint $x_0$, show that the inclusion $i: X_0 \rightarrow X$ induces an isomorphism $\pi_1(X_0, x_0) \rightarrow \pi_1(X, x_0)$.

# Solution
Since the inclusion $i$ is a continuous function, $$i_*$$ is a homomorphism.
We will show that it is bijective.

* Injective?

Choose $[f] \in \pi_1(X_0, x_0)$ such that $$i_*([f]) = [e_{x_0}]$$ where $e_{x_0}$ denotes the constant loop at $x_0$.
Since $$i_*([f]) = [f]$$, $f$ and $e_{x_0}$ are homotopic in $X$.
Let $f_t: I \rightarrow X$ be a homotopy between $f$ and $e_{x_0}$ in $X$.
Let $t_0 \times s_0 \in I \times I$ be given.
Then the point $f_{t_0}(s_0)$ is path-connected to $f_{0}(s_0)$ by the path $t \mapsto f_{tt_0}(s_0)$.
The point $f_0(s_0)$ is path-connected to $f_0(0) = f(0) = x_0$ by the path $t \mapsto f_0(ts_0)$.
Therefore, $f_{t_0}(s_0)$ is path-connected to $x_0$, so $f_{t_0}(s_0) \in X_0$.

This means that $f_t$ maps $I$ into $X_0$.
Thus $f_t$ is a homotopy in $X_0$, so $f$ is homotopic to the constant loop at $x_0$ in $X_0$.
Therefore, $$i_*$$ is injective.

* Surjective?

Let $[f] \in \pi_1(X, x_0)$.
Then for each $t_0 \in I$, $f(t_0)$ is path-connected to $f(0)$ by the path $t \mapsto f(tt_0)$.
Thus $f$ maps $I$ into $X_0$.
Let $g: I \rightarrow X_0$ such that $g(t) = f(t)$.
Then $$i_*([g]) = [i \circ g] = [f]$$.
Therefore, $$i_*$$ is surjective.

Hence, $$i_*$$ is bijective.



