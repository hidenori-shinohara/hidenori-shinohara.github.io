---
layout: post
title:  "Definition of free products of groups"
date:   2019-08-09
author: Hidenori
---

Let $\\{ G_{\alpha} \\}$ be a collection of groups.
We will define the free product $$*_{\alpha} G_{\alpha}$$.

# Definition of a word
Let $m$ be a non-negative integer.
Let $G_{\alpha_1}, \cdots, G_{\alpha_m}$ be given.

A function $f: \\{ 1, 2, \cdots, m \\} \rightarrow G_{\alpha_1} \times \cdots \times G_{\alpha_m}$ is called a word.

Note that $m$ is not fixed and it can be $0$.

In the following, we will simply write $g_1g_2 \cdots g_m$ instead of treating a word as a function where $g_i = f(i)$ for each $i = 1, 2, \cdots, m$.
This improves readability.

Defining a equivalence relation on words leads to potentially counter-intuitive situations.
Let $e_{\alpha_0}$ be the identity element in the group $G_{\alpha_0}$.
Consider the words $e_{\alpha_0}$ and $e_{\alpha_0}e_{\alpha_0}$.

* $e_{\alpha_0}$ represents the function that maps $1$ to $e_{\alpha_0}$.
* $e_{\alpha_0}e_{\alpha_0}$ represents the function that maps both $1$ and $2$ to $e_{\alpha_0}$.

Thus they are different functions, but that is counter intuitive.
Therefore, we will define a *reduced* word.

# Definition of a reduced word

A word is considered reduced if:

* Each $g_i$ is not the identity in the group it belongs to.
* For each $i = 1, 2, \cdots, m - 1$, $g_i$ and $g_{i + 1}$ belong to different groups.

By only dealing with reduced words, we can avoid the problem that we mentioned above.

# Definition of a free product
Let $$*_{\alpha} G_{\alpha}$$ be the set of all reduced words.
We will define the product inductively.

First, define the product of two empty words to be the empty word.
Suppose that we have defined products of a word of length $m' \leq m$ and a word of length $n' \leq n$ where $m, n$ are non-negative integers.
Let $$g_1g_2 \cdots g_{m + 1}, h_1h_2 \cdots h_n \in *_{\alpha} G_{\alpha}$$.
We define the product to be

* If $n = 0$, then $g_1g_2 \cdots g_{m + 1}$.
* Suppose $n \geq 1$. 
    * If $g_{m + 1}$ and $h_1$ belong to different groups, then $g_1g_2 \cdots g_mg_{m + 1}h_1h_2 \cdots h_n$.
    * Suppose $g_{m + 1}$ and $h_1$ belong to the same group.
        * If $g_{m + 1}h_1 = e$, then $g_1g_2 \cdots g_mh_2 \cdots h_n$.
        * If $g_{m + 1}h_1 \ne e$, then $g_1g_2 \cdots g_m(g_{m + 1}h_1)h_2 \cdots h_n$.

Similarly, define the product of $$g_1g_2 \cdots g_m$$ and $$h_1h_2 \cdots h_{n + 1}$$.


# Proposition
$$*_{\alpha} G_{\alpha}$$ with the binary operation defined above is indeed a group.

# Proof

* Closed under the binary operation?
    * The empty word is in $$*_{\alpha} G_{\alpha}$$.
      Suppose that a product of a word of length $m' \leq m$ and length $n' \leq n$ is always in $$*_{\alpha} G_{\alpha}$$.
      Let $$g_1g_2 \cdots g_{m + 1}, h_1h_2 \cdots h_n \in *_{\alpha} G_{\alpha}$$.
        * If $n = 0$, then the product is $g_1g_2 \cdots g_{m + 1}$, which is in $$*_{\alpha} G_{\alpha}$$.
        * Suppose $n \geq 1$. 
            * If $g_{m + 1}$ and $h_1$ belong to different groups, then $g_1g_2 \cdots g_mg_{m + 1}h_1h_2 \cdots h_n$.
                * This satisfies all the requirements of a reduced group, so it is in $$*_{\alpha} G_{\alpha}$$.
            * Suppose $g_{m + 1}$ and $h_1$ belong to the same group.
                * If $g_{m + 1}h_1 = e$, then $g_1g_2 \cdots g_mh_2 \cdots h_n$.
                  This is a product of two reduced words of length $m$ and $n - 1$, so it is in $$*_{\alpha} G_{\alpha}$$.
                * If $g_{m + 1}h_1 \ne e$, then $g_1g_2 \cdots g_m(g_{m + 1}h_1)h_2 \cdots h_n$.
                  This satisfies all the requirements of a reduced group, so it is in $$*_{\alpha} G_{\alpha}$$.

      Similarly, $$(g_1g_2 \cdots g_m)(h_1h_2 \cdots h_{n + 1})$$ is also a reduced word.
      By mathematical induction, $$*_{\alpha} G_{\alpha}$$ is closed under the binary operation.
* Associativity?
    * TODO
* Identity?
    * The empty word is the identity element.
* Inverse?
    * Let $$g_1g_2 \cdots g_m \in *_{\alpha} G_{\alpha}$$.
      Then $$(g_1g_2 \cdots g_m)^{-1} = g_m^{-1} \cdots g_1^{-1}$$.

