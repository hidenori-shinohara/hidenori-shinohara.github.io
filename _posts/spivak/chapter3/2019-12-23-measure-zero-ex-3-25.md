---
layout: post
title:  "$[a_1, b_1] \\times \\cdots \\times [a_n, b_n]$ does not have measure 0"
date:   2019-12-23
author: Hidenori
---

# Proposition
Use induction on $n$ to show that $[a_1, b_1] \times \cdots \times [a_n, b_n]$ is not a set of measure 0 (or content 0) if $a_1 < b_i$ for each $i$.

# Solution
By Theorem 3-6[Spivak], it suffices to prove this for measure 0.
By Theorem 3-5[Spivak], the statement is true when $n = 1$.

Suppose that we have proved this up to some $n \in \mathbb{N}$.
Let $A = [a_1, b_1] \times \cdots \times [a_n, b_n]$ and $B = [a_{n + 1}, b_{n + 1}]$.
Let $f: A \times B \rightarrow \mathbb{R}$ be defined such that $f(a, b) = 1$ for all $(a, b) \in A \times B$.
By Theorem 3.8, $f$ is integrable over $A \times B$ and $b \mapsto f(a, b)$ is integrable over $B$ for any fixed $a \in A$.

$$
\begin{align*}
  \int{A \times B} f
    &= \int{A \times B} f \\
    &= \int{A \times B} 1 \\
    &= \int_A (L \int_B dy) dx \\
    &= \int_A (\int_B dy) dx \\
    &= (\int_B dy) (\int_A dx).
\end{align*}
$$

By the inductive hypothesis, $A$ and $B$ do not have measure 0.
By taking the contrapositive of [a proposition we showed before](/2019/12/22/nonnegative-ex-3-18.html), $\int_A dx \ne 0$ and $\int_B dx \ne 0$.
Therefore, $\int_{A \times B} f \ne 0$.
By taking the contrapositive of [a proposition we showed before](/2019/12/23/measure-zero-ex-3-17.html), $A \times B$ does not have measure 0.
