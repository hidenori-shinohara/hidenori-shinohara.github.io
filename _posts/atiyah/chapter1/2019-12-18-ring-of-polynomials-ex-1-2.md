---
layout: post
title:  "Ring of polynomials(WIP)"
date:   2019-12-18
author: Hidenori
---

# Proposition
Let $A$ be a ring and let $A[x]$ be the ring of polynomials in an indeterminate $x$, with coefficients in $A$.
Let $f = a_0 + a_1x + \cdots + a_nx^n \in A[x]$.
Prove that

1. $f$ is a unit in $A[x] \iff a_0$ is a unit in $A$ and $a_1, \cdots, a_n$ are nilpotent.
1. TODO
1. TODO
1. TODO

# Solution
## 1
Suppose $f$ is a unit in $A[x]$.
We will prove this by induction on the degree of $f$.
If $\deg(f) = 0$, we are done.
Let $n \in \mathbb{N}$.
Suppose that we have shown this proposition for degree $< n$.
Suppose $\deg(f) = n$.

Let $g = b_0 + b_1x + \cdots + b_mx^m \in A[x]$ be the inverse of $f$.
Then $a_0b_0 = 1$, so $a_0$ and $b_0$ are clearly units.
Then $fg = \sum_{i=0}^{n + m} [\sum_{j=0}^{i} a_{i - j}b_j]x^{i + j}$.
We claim that $a_{n}^{r + 1}b_{m - r} = 0$ for each $r = 0, \cdots, m$.
When $r = 0$, this is obvious because $a_nb_m = 0$.
Let $r = 1, \cdots, m$ be given.
Suppose that the proposition has been shown for $0, 1, \cdots, r - 1$.
We will show this for $r$.
Since $a_nb_{m - r} + \cdots + a_{n - r}b_m = 0$, we have $a_n^r(a_nb_{m - r} + \cdots + a_{n - r}b_m) = 0$.
Thus $a_n^{r + 1}b_{m - r} + a_n^ra_{n - 1}b_{m - r + 1} + \cdots + a_n^ra_{n - r}b_m = 0$.
Then
* $a_n^ra_{n - 1}b_{m - r + 1} = 0$ because $a_n^{(r - 1) + 1}b_{m - (r - 1)} = 0$ by the inductive hypothesis.
* $a_n^ra_{n - 2}b_{m - r + 2} = 0$ because $a_n^{(r - 2) + 1}b_{m - (r - 2)} = 0$ by the inductive hypothesis.
* $\vdots$
* $a_n^ra_{n - r}b_m = 0$ because $a_n^{0 + 1}b_{m - 0} = 0$ by the inductive hypothesis.

Therefore, $a_n^{r + 1}b_{m - r} = 0$.
This implies that $a_n^{m + 1}b_{m - m} = 0$.
Since $b_0$ is a unit, $a_n^{m + 1} = 0$, so $a_n$ is a nilpotent element.
Then $-a_nx^n$ is nilpotent, and thus $f + (-a_nx^n)$ is a unit [because it is a sum of a unit and a nilpotent element](/2019/11/22/nilpotent-ex-1-1.html).
By the inductive hypothesis, $f + (-a_nx^n)$ is a polynomial where the constant term is a unit and the coefficient of any nonzero power of $x$ is nilpotent.
Therefore, we have shown the desired proposition.

On the other hand, suppose that $a_0$ is a unit and $a_1, \cdots, a_n$ are nilpotent.
$a_0 + a_1x$ is a unit [because it is a sum of a unit and a nilpotent element](/2019/11/22/nilpotent-ex-1-1.html).
By repeatedly applying this property, we obtain that $a_0 + a_1x + \cdots + a_nx^n$ is a unit.

## 2
TODO

## 3
TODO

## 4
TODO
