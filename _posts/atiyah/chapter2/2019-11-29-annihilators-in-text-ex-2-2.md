---
layout: post
title:  "Properties of annihilators of modules"
date:   2019-11-29
author: Hidenori
---

# Proposition
Prove

1. $\Ann(M + N) = \Ann(M) \cap \Ann(N)$.
1. $(N:P) = \Ann((N + P) / N)$.

# Solution

## 1

$\Ann(M + N) = (0:M + N)$, and $\Ann(M) \cap \Ann(N) = (0:M) \cap (0:N)$.
We showed that $(0:M + N) = (0:M) \cap (0:N)$ in [a previous post](/2019/11/25/ideal-quotient-properties-in-text-ex-1-22).

## 2

$$
\begin{align*}
  \Ann((N + P) / N)
    &= (0:(N + P) / N) \\
    &= \{ a \in A \mid a((N + P) / N) = 0 \} \\
    &= \{ a \in A \mid a(N + P) \subset N \} \\
    &= (N:N + P) \\
    &= (N:N) \cap (N:P) \\
    &= A \cap (N:P) \\
    &= (N:P).
\end{align*}
$$
