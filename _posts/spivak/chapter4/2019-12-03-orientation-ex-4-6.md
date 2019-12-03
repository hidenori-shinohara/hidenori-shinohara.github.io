---
layout: post
title:  "Cross product and orientation"
date:   2019-12-03
author: Hidenori
---

# Proposition
1. If $v \in \mathbb{R}^2$, what is $v \times$?
1. If $v_1, \cdots, v_{n - 1} \in \mathbb{R}^n$ are linearly independent, show that $[v_1, \cdots, v_{n - 1}, v_1 \times \cdots \times v_{n - 1}]$ is the usual orientation of $\mathbb{R}^n$.

# Solution
## 1
Let $v = (a, b) \in \mathbb{R}^2$.
We claim that $z = (-b, a)$.
For all $w = (c, d) \in \mathbb{R}^2$, $$\phi(w) = \det{\begin{bmatrix} a & b \\ c & d \end{bmatrix}} = ad - bc$$, and $\ev{(c, d), (-b, a)} = -bc + ad$.

## 2
Let $z = v_1 \times \cdots \times v_{n - 1}$.

$$
\begin{align*}
  \det(v_1, \cdots, v_{n - 1}, z)
    &= \ev{z, z} \\
    &\geq 0.
\end{align*}
$$

Suppose $\det(v_1, \cdots, v_{n - 1}, z) = 0$.
Then $\ev{z, z} = 0$, so $z = 0$.
Since $v_1, \cdots, v_{n - 1}$ are linearly independent in $\mathbb{R}^n$, there must exist a $v_n \in \mathbb{R}^n$ such that $v_1, \cdots, v_n$ are linearly independent.

Then $\ev{v_n, z} = 0$ because $z = 0$, but $\det(v_1, \cdots, v_n) \ne 0$ because they are linearly independent. 
This is a contradiction because $z$ is chosen such that $\det(v_1, \cdots, v_n) = \ev{v_n, z}$.

Therefore, $\ev{z, z} \ne 0$, so $\ev{z, z} > 0$.

Since $\det \in \Lambda^n(\mathbb{R}^n)$ and $\det(v_1, \cdots, v_{n - 1}, z) > 0$ and $\det(e_1, \cdots, e_n) = 1 > 0$, $[v_1, \cdots, v_{n - 1}, z] = [e_1, \cdots, e_n]$.
