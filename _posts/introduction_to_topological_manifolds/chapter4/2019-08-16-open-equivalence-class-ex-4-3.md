---
layout: post
title:  "Equivalence classes and open sets"
date:   2019-08-16
author: Hidenori
---

# Proposition
Suppose $X$ is a connected topological space, and $\sim$ is an equivalence relation on $X$ such that every equivalence class is open.
Show that there is exactly one equivalence class, namely $X$ itself.

# Solution
For each $x \in X$, let $U_x = \\{ y \in X \mid x \sim y \\}$.
Let $x_0 \in X$ be given.
If $U_{x_0} = X$, we are done.
Suppose otherwise.
Let $$V = \bigcup_{x \in U_{x_0}^c} U_x$$.
Then $U_{x_0} \cup V = X$ and $U_{x_0} \cap V = \emptyset$.
$U_{x_0}$ is open since it is an equivalence class.
$V$ is open since it is a union of equivalence classes, each of which is open.

Therefore, $X$ is disconnected.
This is a contradiction, so $U_{x_0} = X$.
