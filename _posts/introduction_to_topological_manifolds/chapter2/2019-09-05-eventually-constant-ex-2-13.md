---
layout: post
title:  "Convergent sequences in a discrete topological space are eventually constant"
date:   2019-09-05
author: Hidenori
---

# Proposition
Let $X$ be a discrete topological space.
Show that the only convergent sequences in $X$ are the ones that are eventually constant, that is, sequences $(x_i)$ such that $x_i = x$ for all but finitely many $i$.

# Solution
It is easy to see that eventually constant sequences converge.
Let $(x_i)$ be a convergent sequence in $X$.
Let $x$ be a limit.
Then the singleton $\{ x \}$ is a neighborhood of $x$, so there must exist an $N \in \mathbb{N}$ such that $\forall n \geq N, x_n = x$.
Therefore, $(x_i)$ is eventually constant.
