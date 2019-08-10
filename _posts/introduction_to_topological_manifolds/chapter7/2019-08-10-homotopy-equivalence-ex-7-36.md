---
layout: post
title:  "Homotopy equivalence is an equivalence relation on the class of all topological spaces."
date:   2019-08-10
author: Hidenori
---

# Proposition
Homotopy equivalence is an equivalence relation on the class of all topological spaces.

# Solution

Let $X, Y, Z$ be given.

The identity mapping $i_X$ on $X$ is continuous.
Moreover, $i_X \circ i_X = i_X$, so $i_X \circ i_X \simeq i_X$.
Therefore, $X \simeq X$.

Suppose $X \simeq Y$.
Then there exist continuous functions $\phi: X \rightarrow Y, \psi: Y \rightarrow X$ such that $\phi \circ \psi \simeq i_Y$ and $\psi \circ \phi \simeq i_X$.
This means we have $\psi$ and its homotopy inverse, so $Y$ is homotopic equivalent to $X$.


Suppose $X \simeq Y$ and $Y \simeq Z$.
Then there exist continuous functions $\phi: X \rightarrow Y, \phi': Y \rightarrow Z$ and their homotopy inverses $\psi: Y \rightarrow X, \psi': Z \rightarrow Y$, respectively.

$\phi' \circ \phi$ is a continuous map from $X$ to $Z$ and we claim that $\psi \circ \psi'$ is a homotopy inverse for $\phi' \circ \phi$.
Let $F, F'$ be homotopies connecting $\phi \circ \psi$ to $i_Y$, and $\phi' \circ \psi'$ to $i_Z$, respectively.

Let $G: Z \times I \rightarrow Z$ such that

$$
\begin{align*}
  G(z, t) &=
  \begin{cases}
    \phi'(F(\psi'(z), 2t)) & (t \in [0, 1/2]) \\
    F'(z, 2t - 1) & (t \in [1/2, 1]).
  \end{cases}
\end{align*}
$$

$G$ is continuous by [the pasting lemma](https://en.wikipedia.org/wiki/Pasting_lemma).

* $G(z, 0) = \phi'(F(\psi'(z), 0)) = \phi'(\phi(\psi(\psi'(z))))$.
* $G(z, 1) = F'(z, 1) = i_Z(z) = z$.

Thus $G$ is a homotopy connecting $\phi' \circ \phi \circ \psi \circ \psi'$ to $i_Z$.

Now let $F, F'$ be homotopies connecting $\psi \circ \phi$ to $i_X$, and $\psi' \circ \phi'$ to $i_Y$, respectively.
(Overriding the notations since I'm running out of suitable letters.)

Similarly, let $H: X \times I \rightarrow X$ such that

$$
\begin{align*}
  H(x, t) &=
  \begin{cases}
    \psi(F'(\phi(x), 2t)) & (t \in [0, 1/2]) \\
    F(x, 2t - 1) & (t \in [1/2, 1]).
  \end{cases}
\end{align*}
$$

$H$ is continuous by [the pasting lemma](https://en.wikipedia.org/wiki/Pasting_lemma).

* $G(z, 0) = \phi'(F(\psi'(z), 0)) = \phi'(\phi(\psi(\psi'(z))))$.
* $G(z, 1) = F'(z, 1) = i_Z(z) = z$.

Thus $H$ is a homotopy connecting $\psi \circ \psi' \circ \phi' \circ \phi$ to $i_X$.

Therefore, $\psi \circ \psi'$ is a homotopy inverse of $\phi' \circ \phi$, so $X \simeq Z$.
