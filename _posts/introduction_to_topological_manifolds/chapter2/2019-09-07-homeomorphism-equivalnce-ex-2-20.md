---
layout: post
title:  "\"Homeomorpic\" is an equivalence relation"
date:   2019-09-05
author: Hidenori
---

# Proposition
Show that "homeomorphic" is an equivalence relation on the class of all topological spaces.

# Solution

For any topological space $X$, $\Id_X$ is a homeomorphism from $X$ to $X$.

Let $\phi: X \rightarrow Y$ be a homeomorphism.
Then $\phi^{-1}$ is a continuous bijection.
Moreover $(\phi^{-1})^{-1} = \phi$, so $\phi^{-1}$ has a continuous inverse.
Therefore, $\phi^{-1}$ is a homeomorphism from $Y$ to $X$.

Let $\phi: X \rightarrow Y, \psi: Y \rightarrow Z$ be homeomorphisms.
We claim $\psi \circ \phi$ is a homeomorphism.

* $(\phi^{-1} \circ \psi^{-1}) \circ (\psi \circ \phi) = \Id_X$.
* $(\psi \circ \phi)  \circ (\phi^{-1} \circ \psi^{-1}) = \Id_Z$.

Therefore, $\psi \circ \phi$ is a bijection.

Since $\psi \circ \phi$ is a composition of continuous functions, so it is continuous.
Since $\phi^{-1} \circ \psi^{-1}$ is a composition of continuous functions, so it is continuous.

Therefore, $\psi \circ \phi$ is a homeomorphism from $X$ to $Z$.
