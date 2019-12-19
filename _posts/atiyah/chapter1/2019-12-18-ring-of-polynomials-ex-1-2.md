---
layout: post
title:  "Ring of polynomials"
date:   2019-12-18
author: Hidenori
---

# Proposition
Let $A$ be a ring and let $A[x]$ be the ring of polynomials in an indeterminate $x$, with coefficients in $A$.
Let $f = a_0 + a_1x + \cdots + a_nx^n \in A[x]$.
Prove that

1. $f$ is a unit in $A[x] \iff a_0$ is a unit in $A$ and $a_1, \cdots, a_n$ are nilpotent.
1. $f$ is nilpotent $\iff a_0, a_1, \cdots, a_n$ are nilpotent.
1. $f$ is a zero-divisor $\iff$ there exists $a \ne 0$ in $A$ such that $af = 0$.
1. $f$ is said to be primitive if $(a_0, \cdots, a_n) = (1)$.
   Prove that if $f, g \in A[x]$, then $fg$ is primitive $\iff f$ and $g$ are primitive.

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
First, we will prove a general statement about nilpotent elements in a ring.
We claim that the sum of two nilpotent elements is nilpotent.
Let $a, b$ be nilpotent with $a^n = b^m = 0$.
Then $$(a + b)^{n + m} = \sum_{i=0}^{n+m} \binom{n + m}{i}a^ib^{n+m-i} = 0$$ because $i \geq n$ or $n + m - i \geq m$.

By induction, the sum of finitely many nilpotent elements is nilpotent.
Therefore, if $a_0, a_1, \cdots, a_n$ are nilpotent, $f = a_0 + a_1x + \cdots + a_nx^n$ is nilpotent.

Suppose $f$ is nilpotent.
If the degree of $f$ is 0, then this is obvious.
Suppose that we have shown this property for degree $< n$ and suppose the degree of $f$ is $n$ and $f^m = 0$.

The coefficient of $x^{nm}$ in $f^m$ is $a_n^m$.
Thus the leading coefficient of $f$ must be nilpotent.
Since the sum of two nilpotent elements is nilpotent, $f + (-a_nx^n)$ is nilpotent.
By the inductive hypothesis, $a_0, \cdots, a_{n - 1}$ are nilpotent.

## 3
If $af = 0$ for some $a \ne 0$ in $A$, then $f$ is a zero divisor in $A[x]$.
Suppose $f$ is a zero divisor in $A[x]$.
Then $\Ann(f) \subset A[x]$ is nonempty and contains at least one nonzero element.
Let $g$ be a nonzero element in $\Ann(f)$ of the least degree.
Let $m = \deg(g)$.
If $m = 0$, then $g$ is an element in $A$ and we are done.
Suppose otherwise.
Let $a_0 + a_1x + \cdots + a_nx^n, b_0 + b_1x + \cdots + b_mx^m$ denote $f, g$, respectively, where $a_n \ne 0$ and $b_m \ne 0$.
We claim that $a_{n - r}g = 0$ for each $r = 0, \cdots, n$.
* Case 1: $r = 0$.
  * Then $fg = 0$, so $a_nb_m$, the coefficient of $x^{n + m}$, must be 0.
    Then the degree of $a_ng$ is at most $m - 1$.
    Then $a_ng$ must be 0 because $g$ has the least degree among all the nonzero elements in $\Ann(f)$.
* Case 2: Suppose we have shown that $a_{n - r}g = 0$ for each $r = 0, \cdots, k - 1$ for some $k$.
  * Then $a_nb_{m - k} + \cdots + a_{n - k}b_m$, the coefficient of $x^{n + m - k}$, must be 0.
    By the inductive hypothesis, $a_nb_{m - k} = \cdots = a_{n - k + 1}b_{m + 1} = 0$.
    Thus $a_{n - k}b_m$ must be 0.
    Then the degree of $a_{n - k}g$ is at most $m - 1$, so $a_{n - k}g$ must be 0 for the same reason as above.
By induction, $a_{n - r}g = 0$ for each $r = 0, \cdots, n$.
In particular, this means $a_ib_m = 0$ for each $i$.

Therefore, $b_m \ne 0$ and $b_mf = 0$.

## 4
Let $f = a_0 + a_1x + \cdots + a_nx^n$ and $g = b_0 + b_1x + \cdots + b_mx^m$.

Suppose $fg$ is primitive.
Then $(a_0b_0, a_1b_0 + a_0b_1, \cdots, a_nb_m) = (1)$.
Since $(1) = (a_0b_0, a_1b_0 + a_0b_1, \cdots, a_nb_m) \subset (a_0, a_1, \cdots, a_n)$, $f$ is primitive.
Similarly, $g$ is primitive.

On the other hand, suppose $f, g$ are both primitive.
Let $I$ be the ideal generated by all the coefficients of $fg$.
If $I = (1)$, we are done.
Suppose $I \ne (1)$.
By Corollary 1.4 [Atiyah], $I$ is contained in a maximal ideal $m$.
Let $\phi:A[x] \rightarrow (A/m)[x]$ be the map induced by the quotient map $A \rightarrow A/m$.
Then $\phi(fg) = 0$ in $(A/m)[x]$ because every coefficient of $fg$ is in $m$.
Thus $\phi(f)\phi(g) = 0$ in $(A/m)[x]$.
Since $A/m$ is a field, $(A/m)[x]$ is an integral domain.
Thus $\phi(f) = 0$ or $\phi(g) = 0$.
Without loss of generality, we assume $\phi(f) = 0$.
This implies $f \in m[x]$.

However, this is impossible because the coefficients of $f$ generate $(1)$, so no maximal ideal may contain all the coefficients of $f$.
Hence, this is a contradiction, so $I = (1)$.
