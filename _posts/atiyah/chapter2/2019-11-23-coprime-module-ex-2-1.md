---
layout: post
title:  "$(\\mathbb{Z}/m\\mathbb{Z}) \\otimes (\\mathbb{Z}/n\\mathbb{Z}) = 0$ if $m, n$ are coprime"
date:   2019-11-23
author: Hidenori
---

# Proposition
$(\mathbb{Z}/m\mathbb{Z}) \otimes (\mathbb{Z}/n\mathbb{Z}) = 0$ if $m, n$ are coprime.

# Solution
If $m, n$ are coprime, there must exist integers $p, q$ such that $pm + qn = 1$.

Let $a \otimes b \in (\mathbb{Z}/m\mathbb{Z}) \otimes (\mathbb{Z}/n\mathbb{Z})$.

$$
\begin{align*}
  a \otimes b
    &= 1(a \otimes b) \\
    &= (pm + qn)(a \otimes b) \\
    &= pm(a \otimes b) + qn(a \otimes b) \\
    &= p((ma) \otimes b) + q(a \otimes (nb)) \\
    &= p(0 \otimes b) + q(a \otimes 0) \\
    &= 0 + 0 \\
    &= 0.
\end{align*}
$$
