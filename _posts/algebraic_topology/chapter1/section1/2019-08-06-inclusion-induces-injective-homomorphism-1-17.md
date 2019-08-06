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

We will prove the second part.
Let $A$ be a deformation retract of $X$ and $i: A \rightarrow X$ be the inclusion map.
Let $x_0 \in A$ be given.
Since $A$ is a retract of $X$, $$i_*: \pi_1(A, x_0) \rightarrow \pi_1(X, x_0)$$ is an injective homomorphism as shown above.

We will show that $$i_*$$ is surjective.
Let $[f] \in \pi_1(X, x_0)$ be given.
Let $r_t$ be a deformation retraction.
Then we claim that $F(s, t) = r_t(f(s))$ is a homotopy between $f$ and $r_1 \circ f$.

* $F(s, 0) = r_0(f(s)) = f(s)$.
* $F(s, 1) = r_1(f(s)) = (r_1 \circ f)(s)$.
* $F(0, t) = r_t(f(0)) = r_t(x_0) = x_0$ since $x_0 \in A$.
* $F(1, t) = r_t(f(1)) = r_t(x_0) = x_0$.
* Since $r_t(s)$ is continuous when seen as a function of two variables $s, t$ and $f(s)$ is continuous, $r_t(f(s))$ is continuous.

Therefore, $F$ is indeed a homotopy.
By the definition of a deformation retraction, $r_1 \circ f$ maps $I$ into $A$.
Since $r_1 \circ f$ is continuous, it is a loop in $A$.
Thus $[r_1 \circ f] \in \pi_1(A, x_0)$.
Moreover, $[r_1 \circ f] = [f]$.

Then $$i_*([r_1 \circ f]) = [i \circ (r_1 \circ f)] = [r_1 \circ f] = [f]$$, so $$i_*$$ is surjective.

Hence, $$i_*$$ is an isomorphism from $\pi_1(A, x_0)$ into $\pi_1(X, x_0)$.
