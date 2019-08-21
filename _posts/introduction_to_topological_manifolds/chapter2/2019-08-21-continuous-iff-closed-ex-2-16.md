---
layout: post
title:  "A map between topological spaces is continuous if and only if the preimage of every closed subset is closed."
date:   2019-08-21
author: Hidenori
---

# Proposition
A map between topological spaces is continuous if and only if the preimage of every closed subset is closed.

# Solution
Let $f: X \rightarrow Y$ be given.

For any subset $C \subset Y$ and for any $x \in X$,

$$
\begin{align*}
  x \in f^{-1}(Y \setminus C)
    &\iff f(x) \in Y \setminus C \\
    &\iff f(x) \notin C \\
    &\iff x \notin f^{-1}(C) \\
    &\iff x \in Y \setminus f^{-1}(C).
\end{align*}
$$

Therefore, $f^{-1}(Y \setminus C) = X \setminus f^{-1}(C)$.

Now, suppose that $f$ is continous.

Let $C \subset Y$ be closed.
Since $C$ is closed, $Y \setminus C$ is open.
Since $f$ is continuous, $f^{-1}(Y \setminus C) = X \setminus f^{-1}(C)$ is open, so $f^{-1}(C)$ is closed.

Suppose, on the other hand, that the preimage of every closed subset is closed.
Let $V \subset Y$ be open.
Then $Y \setminus V$ is closed.
$f^{-1}(Y \setminus V)$ is closed, and thus $X \setminus f^{-1}(V)$ is closed.
This implies that $f^{-1}(V)$ is open.
Therefore, $f$ is continuous.
