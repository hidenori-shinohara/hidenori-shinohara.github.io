---
layout: post
title:  "Volume element and determinant"
date:   2019-11-24
author: Hidenori
---

# Proposition
If $\omega \in \Lambda^n(V)$ is the volume element determined by $T$ and $\mu$, and $w_1, \cdots, w_n \in V$, show that

$$
\begin{align*}
  \abs{\omega(w_1, \cdots, w_n)} = \sqrt{\det(g_{ij})}.
\end{align*}
$$

where $g_{ij} = T(w_i, w_j)$.

# Solution
Let $v_1, \cdots, v_n$ be an orthonormal basis such that $[v_1, \cdots, v_n] = \mu$.
Then there exist $a_{ij}$ such that $w_i = \sum_{j} a_{ij} w_j$.

$$
\begin{align*}
  \omega(w_1, \cdots, w_n)
    &= \omega(\sum_{j} a_{1j} w_j, \cdots, \sum_{j} a_{nj} w_j) \\
    &= \det(a_{ij}) \omega(v_1, \cdots, v_n) & \text{(Theorem 4.6 [Spivak])} \\
    &= \det(a_{ij}).
\end{align*}
$$

$\omega(v_1, \cdots, v_n) = 1$ by the definition of a volume element [P.83, Spivak].

On the other hand,

$$
\begin{align*}
  g_{ij}
    &= T(w_i, w_j) \\
    &= T(\sum_k a_{ik} v_k, \sum_l a_{jl} v_l) \\
    &= \sum_{k, l} a_{ik}a_{jl} T(v_k, v_l) \\
    &= \sum_{k} a_{ik}a_{jk} \\
    &= \sum_{k} (A)_{ik}(A^T)_{kj} \\
    &= (AA^T)_{ij}.
\end{align*}
$$

Therefore, $\det(g_{ij}) = \det(AA^T) = \det(A)^2$, so $\sqrt{\det(g_{ij})} = \abs{\det(A)} = \abs{\omega(w_1, \cdots, w_n)}$.
