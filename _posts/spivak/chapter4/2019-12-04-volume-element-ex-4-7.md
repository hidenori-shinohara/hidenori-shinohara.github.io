---
layout: post
title:  "Every nonzero $n$-form is a volume element"
date:   2019-12-04
author: Hidenori
---

# Proposition
Show that every non-zero $\omega \in \Lambda^n(V)$ is the volume element determined by some inner product $T$ and orientation $\mu$ for $V$.

# Solution
Let $v_1, \cdots, v_n$ be a basis of $V$.
Suppose $\omega(v_1, \cdots, v_n) = 0$.
Then $\omega(v_{\sigma_1}, \cdots, v_{\sigma_n}) = 0$ for all $\sigma \in S_n$.
For any $a_{ij}$, $\omega(\sum a_{1i} v_i, \cdots, \sum a_{ni} v_i) = \sum_{\sigma} a_{1\sigma_1} \cdots a_{n\sigma_n} \omega(v_{\sigma_1}, \cdots, v_{\sigma_n}) = 0$.
However, this means $\omega = 0$.
Therefore, $\omega(v_1, \cdots, v_n) \ne 0$.
Without loss of generality, $\omega(v_1, \cdots, v_n) = 1$.
Let $T(v_i, v_j) = \delta_{ij}$.
Then there exists a unique 2-tensor extending $T$.
Moreover, $T$ is clearly symmetric and positive definite.
Thus $T$ is an inner product of $V$.
Finally, let $\mu = [v_1, \cdots, v_n]$.
We claim that $\omega$ is the volume element determined by $T$ and $\mu$.

Let $w_1, \cdots, w_n$ be an orthonormal basis of $V$ with respect to $T$.
Moreover, assume $[w_1, \cdots, w_n] = \mu$.
In other words, this means $\det(A) > 0$ where $[w_1 \cdots w_n] = A[v_1 \cdots v_n]$.
Since $w_i$ and $v_i$ are both orthonormal bases, $\det(A) = \pm 1$ by the argument on P.83 [Spivak].
Therefore, $\det(A) = 1$.

By Theorem 4-6[Spivak], $\omega(w_1, \cdots, w_n) = \det(A)\omega(v_1, \cdots, v_n) = 1 \cdot 1 = 1$.
