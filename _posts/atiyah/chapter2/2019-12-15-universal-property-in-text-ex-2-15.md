---
layout: post
title:  "An application of the universal property of a tensor product(WIP)"
date:   2019-12-15
author: Hidenori
---

# Proposition
Let $A, B$ be rings, let $M$ be an $A$-module, $P$ a $B$-module, and $N$ an $(A, B)$-bimodule.
Then $M \otimes_A N$ is naturally a $B$-module, $N \otimes_B P$ an $A$-module, and we have

$$
\begin{align*}
  (M \otimes_A N) \otimes_B P \cong M \otimes_A (N \otimes_B P).
\end{align*}
$$

# Solution
We will check if $(M \otimes_A N) \otimes_B P$ and $M \otimes_A (N \otimes_B P)$ are isomorphic as $A$-modules and $B$-modules.

Let $z \in P$ be fixed.
Construct an $A$-bilinear map $f_z: M \times N \rightarrow M \otimes_A (N \otimes_B P)$ such that $f_z(x, y) = x \otimes (y \otimes z)$.
TODO: Show $f_z$ is $A$-bilinear.

By the universal property of a tensor product, there exists a unique $A$-linear map $\tilde{f}_z$ such that the following diagram commutes:

![Universal Property 1](/assets/atiyah/chapter2/in-text-exercise-2-15-1.jpeg)

It is clear that $\tilde{f}_z$ is the map $x \otimes y \mapsto x \otimes (y \otimes z)$, so $\tilde{f}_z$ is also $B$-linear.
TODO: Show $\tilde{f}_z$ is $B$-linear.

This argument works for any $z \in P$, so we can construct $\tilde{f}_z$ for each $z \in P$.

Let $f: (M \otimes_A N) \times P \rightarrow M \otimes_A (N \otimes_B P)$ be defined such that $f((x, y), z) = \tilde{f}_z(x, y)$.
$f$ is a $B$-bilinear map.
TODO: Show $f$ is $B$-bilinear.
By the universal property of a tensor product, there exists a unique $B$-linear map $\tilde{f}$ such that the following diagram commutes:

![Universal Property 2](/assets/atiyah/chapter2/in-text-exercise-2-15-2.jpeg)

It is clear that $\tilde{f}((x \otimes y) \otimes z) = x \otimes (y \otimes z)$.
Moreover, it is easy to see that $\tilde{f}$ is $A$-linear.
TODO: Show $\tilde{f}$ is $A$-linear. Is this claim even true?

A similar argument shows that $\tilde{g}(x \otimes (y \otimes z)) = (x \otimes y) \otimes z$ is both $A$-linear an $B$-linear.
Since $f$ and $g$ are the inverse of each other, $f$ is both an $A$-module isomorphism and $B$-module isomorphism.
