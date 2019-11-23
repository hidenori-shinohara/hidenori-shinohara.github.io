---
layout: post
title:  "$(A/a) \\otimes M \\cong M/aM$"
date:   2019-11-23
author: Hidenori
---

# Proposition
Let $A$ be a ring, $a$ an ideal, $M$ an $A$-module.
Show that $(A / a) \otimes M$ is isomorphic to $M / aM$.

# Solution
$a \rightarrow A \rightarrow A / a \rightarrow 0$ is an exact sequence with the inclusion map $i: a \rightarrow A$ and the canonical quotient map $q: A \rightarrow A / a$.
By Proposition 2.18 on P.28 of Atiyah, $a \otimes M \rightarrow A \otimes M \rightarrow A / a \otimes M \rightarrow 0$ is exact with $i \otimes \Id$ and $q \otimes Id$.
This exact sequence gives us that 

$$
\begin{align*}
  (A / a) \otimes M
    &= \im{q \otimes \Id} \\
    &\cong (A \otimes M) / \ker{q \otimes \Id} \\
    &= (A \otimes M) / \im{i \otimes \Id} \\
    &= (A \otimes M) / (a \otimes M).
\end{align*}
$$

Let $\phi: A \otimes M \rightarrow M / aM$ be defined such that $x \otimes y \mapsto xy + aM$.
Then $\phi$ is a composition of the isomorphism $A \otimes M$ described in Prposition 2.14 (iv) on P.26 of Atiyah and the canonical quotient map $M \mapsto M / aM$.
Therefore, $\phi$ is a surjective module homomorphism.

We claim that $\ker{\phi} =  a \otimes M$.

* Suppose $\phi(x \oplus y) = 0$.
  Then $xy + aM = 0$ and thus $xy \in aM$.
  This implies $xy = x'y'$ for some $x' \in a$ and $y' \in M$.
  $$
  \begin{align*}
    x \otimes y
      &= x(1 \otimes y) & \text{(since $A$ is a commutative ring with 1)} \\
      &= 1 \otimes xy & \text{(since $M$ is an $A$-module)} \\
      &= 1 \otimes x'y' \\
      &= x'(1 \otimes y') & (x' \in A) \\
      &= x' \otimes y' \\
      &\in a \otimes M.
  \end{align*}
  $$
* On other hand, if $x \otimes y \in a \otimes M$, $\phi(x \otimes y) = xy + aM = 0$.

Therefore, $\ker{\phi} = a \otimes M$.

This implies that $(A \otimes M) / (a \otimes M) \cong M / aM$.

Hence, $(A / a) \otimes M \cong M / aM$.
