---
layout: post
title:  "Mappings of contractible spaces are homotopic to a constant map."
date:   2019-08-15
author: Hidenori
---

# Proposition
Let $X$ and $Y$ be topological spaces.
Show that if either $X$ or $Y$ is contractible, then every continuous map from $X$ to $Y$ is homotopic to a constant map.

# Solution
Suppose $X$ is contractible.

Let a continuous function $f: X \rightarrow Y$ be given.
Then there exists a fixed point $p \in X$ and a function $H: X \times I \rightarrow X$ such that

$$
\begin{align*}
  \forall x \in X, H(x, 0) &= x \\
  \forall x \in X, H(x, 1) &= p.
\end{align*}
$$

Define $G: X \times I \rightarrow Y$ by $G = f \circ H$.
Then $G$ is a composition of two continuous functions, so $G$ is continuous.

* $G(x, 0) = f(H(x, 0)) = f(x)$.
* $G(x, 1) = f(H(x, 1)) = f(p)$.

Thus $G$ is a homotopy from $f$ to the constant function that maps every element of $X$ to $f(p)$.
Thus $f$ is homotopic to a constant function.

On the contrary, suppose $Y$ is contractible.
Let a continuous function $f: X \rightarrow Y$ be given.
Then there exists a fixed point $q \in Y$ and a function $H: Y \times I \rightarrow Y$ such that

$$
\begin{align*}
  \forall y \in Y, H(y, 0) &= y \\
  \forall y \in Y, H(y, 1) &= q.
\end{align*}
$$

Define $G: X \times I \rightarrow Y$ such that $G(x, t) = H(f(x), t)$.

$x \mapsto f(x)$ is continuous, and $t \mapsto t$ is continuous.
Therefore, $x \times t \mapsto f(x) \times t$ is continuous.
A composition of two continuous functions is continuous, so $G$ is continuous.

Moreover,

* $\forall x \in X, G(x, 0) = H(f(x), 0) = f(x)$.
* $\forall x \in X, G(x, 1) = H(f(x), 1) = q$.

Therefore, $G$ is a homotopy from $f$ to the constant map that maps every element in $X$ to $q$.
Thus $f$ is indeed homotopic to a constant map.
