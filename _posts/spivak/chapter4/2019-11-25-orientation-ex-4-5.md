---
layout: post
title:  "Orientation and $\\det$"
date:   2019-11-25
author: Hidenori
---

# Proposition
If $c:[0, 1] \rightarrow (\mathbb{R}^n)^n$ is continuous and each $(c^1(t), \cdots, c^n(t))$ is a basis for $\mathbb{R}^n$, show that $[c^1(0), \cdots, c^n(0)] = [c^1(1), \cdots, c^n(1)]$.

# Solution
Since $\\{ e_1, \cdots, e_n \\}$ is a basis of $\mathbb{R}^n$, there must exist $a_{11}, \cdots, a_{1n} \in \mathbb{R}$ such that $c_1(0) = a_{11}e_1 + \cdots + a_{1n}e_n$.
Similarly, for each $i = 2, \cdots, n$, $c_i(0) = a_{i1}e_1 + \cdots + a_{in}e_n$ for some $a_{ij}$.
We are given that $(c^1(0), \cdots, c^n(0))$ is a basis, so we can conclude that $[e_1, \cdots, e_n] = [c_1(0), \cdots, c_n(0)]$ if and only if $\det(A) > 0$ where $A = (a_{ij})$. (P.82[Spivak])
Moreover,

$$
\begin{align*}
A = \begin{bmatrix} c_1(0) \\ c_2(0) \\ \vdots \\ c_n(0) \end{bmatrix},
\end{align*}
$$

so $A = (\det \circ c)(0)$.
Therefore, $[c_1(0), \cdots, c_n(0)]$ is the usual orientation if and only if $(\det \circ c)(0) > 0$.

Using the exact same argument, we conclude that $[c_1(1), \cdots, c_n(1)]$ is the usual orientation if and only if $(\det \circ c)(1) > 0$.

If $[c_1(0), \cdots, c_n(0)] \ne [c_1(1), \cdots, c_n(1)]$, then $\det \circ c$ achieves a positive value at one end of $[0, 1]$ and a negative value at the other end of $[0, 1]$.
By the intermediate value theorem, $(\det \circ c)(t_0) = 0$ for some $t_0 \in (0, 1)$.
However, this implies that $(c^1(t_0), \cdots, c^n(t_0))$ is linearly dependent, and thus is not a basis.
This is a contradiction, so $[c_1(0), \cdots, c_n(0)] = [c_1(1), \cdots, c_n(1)]$.
