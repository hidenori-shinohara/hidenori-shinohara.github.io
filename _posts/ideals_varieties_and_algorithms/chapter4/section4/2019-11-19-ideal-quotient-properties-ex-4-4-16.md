---
layout: post
title:  "Basic properties of ideal quotients"
date:   2019-11-19
author: Hidenori
---

# Proposition
Let $I, J, K \subset k[x_1, \cdots, x_n]$ be ideals.
Prove the following:

1. $IJ \subset K$ if and only if $I \subset K:J$.
1. $(I:J):K = I:JK$.

# Solution

## 1
Suppose $IJ \subset K$.
Let $x \in I$.
Since $IJ \subset K$, $xJ \subset K$.
Therefore, $x \in K:J$.
Therefore, $I \subset K:J$.

Suppose $I \subset K:J$.
Let $x \in IJ$.
Then $x = \sum_{i=1}^{n} a_ib_i$ for some $n \in \mathbb{N}$, $a_i \in I$, $b_i \in J$.
Let $i$ be given.
Since $a_i \in I \subset K:J$, $a_iJ \subset K$.
Since $b_i \in J$, $a_ib_i \in K$.
This implies that $x \in K$ because $K$ must be closed under finite addition.
Therefore, $IJ \subset K$.

Hence, $IJ \subset K \iff I \subset K:J$.

## 2
Let $x \in k[x_1, \cdots, x_n]$.

$$
\begin{align*}
  x \in (I:J):K
    &\iff xK \subset I:J \\
    &\iff (xK)J \subset I & \text{(by part 1)}\\
    &\iff x(KJ) \subset I \\
    &\iff x(JK) \subset I \\
    &\iff x \in I:(JK).
\end{align*}
$$

Therefore, $(I:J):K = I:(JK)$.
