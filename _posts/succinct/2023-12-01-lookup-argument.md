---
layout: post
title:  "Lookup argument (Jolt)"
date:   2023-12-01
author: Hidenori
---

Summary of Appendix B of [Jolt: SNARKs for Virtual Machines via Lookups](https://eprint.iacr.org/2023/1217.pdf)

# Permutation-invariant fingerprinting

Let $\mathbb{F}$ be a finite field.
Let $a, b \in \mathbb{F}^m$.

The main idea is that for _almost all_ $r \in \mathbb{F}$, $\prod (a_i - r) = \prod (b_i - r)$ if and only if $a = b$.

$\prod (a_i - r_i) - \prod(b_i - r_i) = \sum_{i = 1}^m c_ir^i$ for some $c_i$'s.
Each $c_i$ consists of $a_j$'s and $b_j$'s.

Since $\sum_{i = 1}^m c_ix^i$ is a polynomial of degree $\leq m$ over $\mathbb{F}$, it cannot have more than $m$ roots.
This is a well-known result in algebra.
The idea is that for any root $r_0$, $x - r_0$ is a factor.
See, for instance, Dummit and Foote's Proposition 17, in Chapter 9.5 Polynomial Rings over Fields II for more details.

Therefore, except for up to $m$ elements in $\mathbb{F}$, $\prod (a_i - r) = \prod (b_i - r)$ if and only if $a = b$.

For a sufficiently large finite field with a sufficiently small polynomial, this gives a secure way for a verifier to challenge the claim.

# Lasso lookup argument (read-only table)

Let $T$ be a read-only table with $N$ cells.
Suppose we perform $m$ read operations.

1. For each cell $j$, we maintain a tuple $(j, v_j, c_j)$ = (cell number, value, read count).
   Note that we don't write this tuple to $T$.
   This is something that we keep track of outside of $T$.
1. Whenever we read cell $j$, we increment $c_j$ by 1.
1. After the $m$ read operations, we read every cell once without incrementing $c_j$.

Then we create read set $RS$, which is the set of tuples returned by the $m + N$ read operations.
We also create write set $WS$, which is the set of tuples returned by the initial write operations and the increment operations.

The claim is that $RS$ and $MS$ are permutations of each other if and only if all the reads were correct.

# Lasso lookup argument example

Let's say $T = \\{1: ab, 2: cd, 3: xy, 4: z \\}$.
Suppose that we:

1. read 2
1. read 3
1. read 2
1. read 1


Then the RS will be:

1. $(2, cd, 0)$
1. $(3, xy, 0)$
1. $(2, cd, 0)$
1. $(1, ab, 0)$
1. $(1, ab, 1)$
1. $(2, cd, 2)$
1. $(3, xy, 1)$
1. $(4, z, 0)$

The WS will be:

1. $(1, ab, 0)$
1. $(2, cd, 0)$
1. $(3, xy, 0)$
1. $(4, xy, 0)$
1. $(2, cd, 1)$
1. $(3, xy, 1)$
1. $(2, cd, 2)$
1. $(1, ab, 1)$

And indeed, they are permutations of each other.

This process can be converted into an equality involving three vectors:

1. $a \in \mathbb{F}^m$ representing the $m$ values returned by the first $m$ read operations.
1. $b \in \mathbb{F}^m$ representing the $m$ locations accessed by the first $m$ read operations.
1. $c \in \mathbb{F}^{m + N}$ representing the $m$ counters returned by all the read operations including the final pass.

Note that $a, b$ don't need the results of the final pass involving $N$ reads as we can simply use the indices $0, 1, \cdots, N - 1$ and the values stored in $T$.

Finally, a tuple of $(a, b, c)$ can be converted into one number by evaluating $a + b \gamma + c \gamma^2$ for a random $\gamma$.

Therefore, for given $\gamma, \alpha$,

$$
\begin{align*}
    \prod_{i=0}^{m - 1}(\alpha - (b_i + \gamma a_i + \gamma^2 c_i))
    \prod_{i=0}^{N - 1}(\alpha - (i + \gamma T[i] + \gamma^2 c_{m + i}))
    =
    \prod_{i=0}^{N - 1}(\alpha - (i + \gamma T[i]))
    \prod_{i=0}^{m - 1}(\alpha - (b_i + \gamma a_i + \gamma^2 (c_i + 1))).
\end{align*}
$$

