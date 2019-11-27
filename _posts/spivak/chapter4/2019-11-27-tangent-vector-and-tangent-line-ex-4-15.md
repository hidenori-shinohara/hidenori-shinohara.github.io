---
layout: post
title:  "Tangent vectors and tangent lines"
date:   2019-11-27
author: Hidenori
---

# Proposition
Let $f: \mathbb{R} \rightarrow \mathbb{R}$ and define $c: \mathbb{R} \rightarrow \mathbb{R}^2$ by $c(t) = (t, f(t))$.
Show that the end point of the tangent vector of $c$ at $t$ lies on the tangent line to the graph of $f$ at $(t, f(t))$.

# Solution
Let $t_0 \in \mathbb{R}$ be given.
From basic algebra, we know that the point $(x, y)$ is on the tangent line at $t_0$ if and only if it satisfies $y = f'(t_0)(x - t_0) + f(t_0)$.

$$c_{\ast}((e_1)_{t_0}) = ((c^1)'(t_0), (c^2)'(t_0))_{c(t_0)} = (1, f'(t_0))_{(t_0, f(t_0))}$$.
In other words, the tangent vector of $c$ at $t_0$ is the vector $(1, f'(t_0))$ associated to the point $(t_0, f(t_0))$.
Therefore, the end point of the vector is $(t_0 + 1, f(t_0) + f'(t_0))$.
It is clear that this coordinate satisfies the equation above, so the end point of the tangent vector indeed lies on the tangent line.
