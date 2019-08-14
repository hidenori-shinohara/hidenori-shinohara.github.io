---
layout: post
title:  "Isomorphisms induced by paths"
date:   2019-08-14
author: Hidenori
---

# Proposition
Suppose that $X$ is a topological space, and $g$ is any path in $X$ from $p$ to $q$.
Let $\Phi_g: \pi_1(X, p) \rightarrow \pi_1(X, q)$ denote the group isomorphism induced by $g$.

1. Show that if $h$ is another path in $X$ starting at $q$, then $\Phi_{g \cdot h} = \Phi_h \circ \Phi_g$.
1. Suppose that $\psi: X \rightarrow Y$ is continuous, and show that the following diagram commutes:

$\require{extpfeil}\Newextarrow{\xRightarrow}{5,5}{0x27f6}$

$$
\begin{gather*}
  \pi_1(X, p) & \xRightarrow{\psi_*} & \pi_1(Y, \psi(p)) \\
  \Phi_g \Big\downarrow &  & \Big\downarrow\Phi_{\psi \circ g} \\
  \pi_1(X, q) & \xRightarrow{\psi_*} & \pi_1(Y, \psi(q)).
\end{gather*}
$$

# Solution
## 1
Let $h$ be a path starting at $q$.
We claim that $\overline{g \cdot h} = \overline{h} \cdot \overline{g}$.

When $t \in [0, 1/2]$,

$$
\begin{align*}
  \overline{g \cdot h}(t)
    &= (g \cdot h)(1 - t) \\
    &= h(2(1 - t) - 1) \\
    &= h(1 - 2t) \\
    &= \overline{h}(2t) \\
    &= (\overline{h} \cdot \overline{g})(t).
\end{align*}
$$

Similarly, when $t \in [1/2, 1]$, $\overline{g \cdot h}(t) = (\overline{h} \cdot \overline{g})(t)$.

For any $[f] \in \pi_1(X, p)$,

$$
\begin{align*}
  \Phi_{g \cdot h}([f])
    &= [\overline{g \cdot h}] \cdot [f] \cdot [g \cdot h] \\ 
    &= [\overline{h} \cdot \overline{g}] \cdot [f] \cdot [g \cdot h] \\ 
    &= [\overline{h}] \cdot [\overline{g}] \cdot [f] \cdot [g] \cdot [h] \\ 
    &= [\overline{h}] \cdot \Phi_g([f]) \cdot [h] \\ 
    &= \Phi_h(\Phi_g([f])) \\
    &= (\Phi_h \circ \Phi_g)([f]).
\end{align*}
$$

Therefore, $\Phi_{g \cdot h} = \Phi_h \circ \Phi_g$.

## 2

TODO
