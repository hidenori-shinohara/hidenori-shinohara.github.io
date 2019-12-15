---
layout: post
title:  "Properties of contraction and extension"
date:   2019-12-14
author: Hidenori
---

# Proposition
If $a_1, a_2$ are ideals of $A$ and if $b_1, b_2$ are ideals of $B$, then

1. $(a_1 + a_2)^e = a_1^e + a_2^e, (b_1 + b_2)^c \supset b_1^c + b_2^c$.
1. $(a_1 \cap a_2)^2 \subset a_1^e \cap a_2^e, (b_1 \cap b_2)^c = b_1^c \cap b_2^c$.
1. $(a_1a_2)^e = a_1^ea_2^e, (b_1b_2)^c \supset b_1^cb_2^c$.
1. $(a_1:a_2)^e \subset (a_1^e:a_2^e), (b_1:b_2)^c \subset (b_1^c:b_2^c)$.
1. $r(a)^e \subset r(a^e), r(b)^c = r(b^c)$.

# Solution
## 1

Let $\sum_{i=1}^{n} y_if(x_{i, 1} + x_{i, 2}) \in (a_1 + a_2)^e$ where $y_i \in B$ and $x_{i, 1} \in a_1, x_{i, 2} \in a_2$.

$$
\begin{align*}
  \sum_{i=1}^{n} y_if(x_{i, 1} + x_{i, 2}) 
    &= \sum_{i=1}^{n} y_i(f(x_{i, 1}) + f(x_{i, 2}) ) \\
    &= \sum_{i=1}^{n} y_if(x_{i, 1}) + \sum_{i=1}^{n} y_if(x_{i, 2}) \\
    &\in a_1^e + a_2^e.
\end{align*}
$$

Therefore, $(a_1 + a_2)^e \subset a_1^e + a_2^e$.

On the other hand, let $\sum_{i=1}^{n} y_{i, 1} f(x_{i, 1}) \in a_1^e$ and $\sum_{i=1}^{m} y_{i, 2} f(x_{i, 2}) \in a_2^e$.
Then $\sum_{i=1}^{n} y_{i, 1} f(x_{i, 1}) + \sum_{i=1}^{m} y_{i, 2} f(x_{i, 2}) = \sum_{i=1}^{n + m} y_i f(x_i)$ where

$$
\begin{align*}
  y_i &= \begin{cases}
    y_{i, 1} & (i \leq n) \\
    y_{i - n, 2} & (i \geq n + 1)
  \end{cases} \\
  x_i &= \begin{cases}
    x_{i, 1} & (i \leq n) \\
    x_{i - n, 2} & (i \geq n + 1).
  \end{cases}
\end{align*}
$$

Then each $y_i$ is in $B$ and each $x_i$ is in $a_1 + a_2$.
Thus $\sum_{i=1}^{n + m} y_i f(x_i) \in (a_1 + a_2)^e$.

Let $x_1 + x_2 \in b_1^c + b_2^c$ be given.
Then $f(x_1) \in b_1$ and $f(x_2) \in b_2$.
Thus $f(x_1) + f(x_2) \in b_1 + b_2$, so $x_1 + x_2 \in (b_1 + b_2)^c$.
Therefore, $b_1^c + b_2^c \subset (b_1 + b_2)^c$.

## 2
Since $a_1 \cap a_2 \subset a_1$, $(a_1 \cap a_2)^e \subset a_1^e$.
Similarly, $(a_1 \cap a_2)^e \subset a_2^e$.
Therefore, $(a_1 \cap a_2)^e \subset a_1^e \cap a_2^e$.

$b_1 \cap b_2 \subset b_1$, so $(b_1 \cap b_2)^c \subset b_1^c$.
Similarly, $(b_1 \cap b_2)^c \subset b_2^c$.
Therefore, $(b_1 \cap b_2)^c \subset b_1^c \cap b_2^c$.

Let $x \in b_1^c \cap b_2^c$.
Then $x \in b_1^c$ and $x \in b_2^c$.
Therefore, $f(x) \in b_1$ and $f(x) \in b_2$.
Thus $f(x) \in b_1 \cap b_2$, so $x \in (b_1 \cap b_2)^c$.

## 3
$$
\begin{align*}
  (a_1a_2)^e
    &= Bf(a_1a_2) \\
    &= Bf(a_1)f(a_2) \\
    &= BBf(a_1)f(a_2) \\
    &= Bf(a_1)Bf(a_1) \\
    &= a_1^ea_2^e.
\end{align*}
$$

Since $(b_1b_2)^c$ is closed under addition and every element in $b_1^cb_2^c$ is a finite sum of elements of the form $xy$ where $x \in b_1^c$ and $y \in b_2^c$,
it suffices to show that each $xy$ is in $(b_1b_2)^c$.

* $x \in b_1^c \implies x \in f^{-1}(b_1) \implies f(x) \in b_1$.
* $y \in b_2^c \implies y \in f^{-1}(b_2) \implies f(y) \in b_2$.

Therefore, $f(xy) = f(x)f(y) \in b_1b_2$, so $xy \in f^{-1}(b_1b_2) = (b_1b_2)^c$.

## 4
Let $bf(x) \in (a_1:a_2)^e$ where $b \in B$ and $x \in (a_1:a_2)$.

$$
\begin{align*}
  xa_2 \subset a_1
    &\implies f(xa_2) \subset f(a_1) \\
    &\implies f(x)f(a_2) \subset f(a_1) \\
    &\implies B(f(x)f(a_2)) \subset Bf(a_1) \\
    &\implies f(x)(Bf(a_2)) \subset Bf(a_1) \\
    &\implies f(x)a_2^e \subset a_1^e \\
    &\implies f(x) \in (a_1^e:a_2^e) \\
    &\implies bf(x) \in (a_1^e:a_2^e).
\end{align*}
$$

$$
\begin{align*}
  x \in (b_1:b_2)^c
    &\implies f(x) \in (b_1:b_2) \\
    &\implies f(x)b_2 \in b_1 \\
    &\implies f^{-1}(f(x)b_2) \subset f^{-1}(b_1) \\
    &\implies xf^{-1}(b_2) \subset f^{-1}(f(x)b_2) \subset f^{-1}(b_1) \\
    &\implies xf^{-1}(b_2) \subset f^{-1}(b_1) \\
    &\implies x \in (f^{-1}(b_1):f^{-1}(b_2)) \\
    &\implies x \in (b_1^c:b_2^c).
\end{align*}
$$

## 5

$$
\begin{align*}
  bf(x) \in r(a)^e
    &\implies x \in r(a) \\
    &\implies x^m \in a & (m \in \mathbb{N})\\
    &\implies f(x^m) \in f(a) \\
    &\implies (f(x))^m \in f(a) \subset a^e \\
    &\implies (f(x))^m \in a^e \\
    &\implies f(x) \in r(a^e) \\
    &\implies bf(x) \in r(a^e).
\end{align*}
$$

$$
\begin{align*}
  x \in r(b)^c
    &\iff f(x) \in r(b) \\
    &\iff \exists m \in \mathbb{N}, f(x)^m \in b \\
    &\iff \exists m \in \mathbb{N}, f(x^m) \in b \\
    &\iff \exists m \in \mathbb{N}, x^m \in f^{-1}(b) \\
    &\iff \exists m \in \mathbb{N}, x^m \in b^c \\
    &\iff x \in r(b^c).
\end{align*}
$$
