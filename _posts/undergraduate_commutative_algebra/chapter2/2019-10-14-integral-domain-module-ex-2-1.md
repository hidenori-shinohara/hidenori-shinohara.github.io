---
layout: post
title:  "Determine whether $A[1/f]$ is a finite $A$-module"
date:   2019-10-14
author: Hidenori
---

# Proposition
Let $A$ be an integral domain with field of fractions $K$, and suppose that $f \in A$ is nonzero and not a unit.
Prove that $A[1/f]$ is not a finite $A$-module.

# Solution
Suppose $A[1/f]$ is a finite $A$-module.

Let $\{ \frac{a_1}{f^{b_1}}, \cdots, \frac{a_n}{f^{b_n}} \}$ be a generating set where $a_i \in A$ and $b_i \geq 0$ for each $i$.
Then $\{ \frac{1}{f^{b_1}}, \cdots, \frac{1}{f^{b_n}} \}$ generates $A[1/f]$.
Let $b = \max\{ b_1, \cdots, b_n \}$.
Then $\{ 1, \frac{1}{f^{1}}, \cdots, \frac{1}{f^{b}} \}$ generates $A[1/f]$.

Therefore, there exist $c_i$ such that

$$
\begin{align*}
  c_0 + \frac{c_1}{f^1} + \cdots + \frac{c_b}{f^b} = \frac{1}{f^{b + 1}}.
\end{align*}
$$

Then $f(c_0f^b + \cdots + c_b) = 1$.
Therefore, $f$ is a unit.
However, we chose $f$ to be a non-unit element.
This is a contradiction, so $A[1/f]$ is not a finite $A$-module.
