---
layout: post
title:  "Properties of the cross product in $\\mathbb{R}^3$"
date:   2019-12-13
author: Hidenori
---

# Proposition
Deduce the following properties of the cross product in $\mathbb{R}^3$.

1. $$
   \begin{align*}
   \begin{matrix}
     e_1 \times e_1 = 0 & e_2 \times e_1 = -e_3 & e_3 \times e_1 = e_2 \\  
     e_1 \times e_2 = e_3 & e_2 \times e_2 = 0 & e_3 \times e_2 = -e_1 \\  
     e_1 \times e_3 = -e_2 & e_2 \times e_2 = e_1 & e_3 \times e_3 = 0.
   \end{matrix}
   \end{align*}
   $$
1. TODO

# Solution
## 1

For each $i = 1, 2, 3$, $e_i \times e_i = 0$ because for any $v \in \mathbb{R}^3$,

$$
\begin{align*}
  \det\begin{bmatrix} e_i \\ e_i \\ v \end{bmatrix} = 0.
\end{align*}
$$

By [the definition of $\det$](https://en.wikipedia.org/wiki/Determinant#n_×_n_matrices), given $\sigma \in S_3$,

$$
\begin{align*}
  \det\begin{bmatrix} e_{\sigma_1} \\ e_{\sigma_2} \\ v \end{bmatrix} = \sgn(\sigma) v_{\sigma_3}.
\end{align*}
$$

This shows the other 6 cases.
For instance, the permutation $(12)$ gives us $e_2 \times e_1 = \sgn((12)) e_3 =  -e_3$.

## 2

TODO
