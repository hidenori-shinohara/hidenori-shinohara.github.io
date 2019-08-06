---
layout: post
title:  "An inclusion map of a retract induces an injective homomorphism."
date:   2019-08-06
author: Hidenori
---

# Proposition
If a space $X$ retracts onto a subspace $A$, then the homomorphism $$i_*: \pi_1(A, x_0) \rightarrow \pi_1(X, x_0)$$ induced by the inclusion $i: A \rightarrow X$ is injecive.
If $A$ is a deformation retract of $X$, then $$i_*$$ is an isomorphism.

# Solution
Let $i: A \rightarrow X$ be the inclusion.
Let $x_0 \in A$ be given.

Since $X$ retracts onto a subspace $A$, there must exist a continuous function $r: X \rightarrow A$ such that $r \circ i$ is the identity function on $A$.

For any $[f] \in \pi_1(A, x_0)$,

$$
\begin{align*}
  (r_* \circ i_*)([f])
    &= r_*(i_*([f])) \\
    &= r_*([i \circ f]) \\
    &= [r \circ (i \circ f)] \\
    &= [(r \circ i) \circ f] \\
    &= [f].
\end{align*}
$$

Therefore, $$r_* \circ i_*$$ is the identity function on $\pi_1(A, x_0)$.
Let $[f], [g] \in \pi_1(A, x_0)$ such that $$i_*([f]) = i_*([g])$$.
Then $$[f] = (r_* \circ i_*)([f]) = r_*(i_*([f])) = r_*(i_*([g])) = (r_* \circ i_*)([g]) = [g]$$.
Therefore, $i_*$ is injective.

TODO
