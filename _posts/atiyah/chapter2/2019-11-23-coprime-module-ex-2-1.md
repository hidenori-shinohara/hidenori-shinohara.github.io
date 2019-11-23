---
layout: post
title:  "$(\\mathbb{Z}/m\\mathbb{Z}) \\oplus (\\mathbb{Z}/n\\mathbb{Z}) = 0$ if $m, n$ are coprime"
date:   2019-11-23
author: Hidenori
---

# Proposition
$(\mathbb{Z}/m\mathbb{Z}) \oplus (\mathbb{Z}/n\mathbb{Z}) = 0$ if $m, n$ are coprime.

# Solution
If $m, n$ are coprime, there must exist integers $p, q$ such that $pm + qn = 1$.

Let $a \oplus b \in (\mathbb{Z}/m\mathbb{Z}) \oplus (\mathbb{Z}/n\mathbb{Z})$.

$$
\begin{align*}
  a \oplus b
    &= 1(a \oplus b) \\
    &= (pm + qn)(a \oplus b) \\
    &= pm(a \oplus b) + qn(a \oplus b) \\
    &= p((ma) \oplus b) + q(a \oplus (nb)) \\
    &= p(0 \oplus b) + q(a \oplus 0) \\
    &= 0 + 0 \\
    &= 0.
\end{align*}
$$
