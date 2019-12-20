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
1. $v \times w = (v^2w^3 - v^3w^2)e_1 + (v^3w^1 - v^1w^3)e_2 + (v^1w^2 - v^2w^1)e_3$.
1. $\abs{v \times w} = \abs{v} \cdot \abs{w} \cdot \abs{\sin \theta}$, where $\theta = \angle (v, w)$.
   $\ev{v \times w, v} = \ev{v \times w, w} = 0$.
1. $\ev{v, w \times z} = \ev{w, z \times v} = \ev{z, v \times w}$.
   $v \times (w \times z) = \ev{v, z}w - \ev{v, w}z$.
   $(v \times w) \times z = \ev{v, z}w - \ev{w, z}v$.
1. $\abs{v \times w} = \sqrt{\ev{v, v} \cdot \ev{w, w} - \ev{v, w}^2}$.

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

$$
\begin{align*}
  \det(\begin{bmatrix} v \\ w \\ a \end{bmatrix})
    &= (v^2w^3 - v^3w^2)a_1 + (v^3w^1 - v^1w^3)a_2 + (v^1w^2 - v^2w^1)a_3 \\
    &= \ev{a, (v^2w^3 - v^3w^2)e_1 + (v^3w^1 - v^1w^3)e_2 + (v^1w^2 - v^2w^1)e_3}.
\end{align*}
$$

## 3

Part 2 shows that in $\mathbb{R}^3$, the definition of the cross product in the textbook is the same as the cross product in elementary linear algebra.
The property that $\abs{v \times w} = \abs{v} \cdot \abs{w} \cdot \abs{\sin \theta}$ comes from elementary algebra.

$$
\begin{align*}
  \ev{v \times w, v} = \det\begin{bmatrix} v \\ w \\ v \end{bmatrix} = 0.
\end{align*}
$$

Similarly, $\ev{v \times w, w} = 0$.

## 4

$$
\begin{align*}
  \ev{v, w \times z}
    &= \det\begin{bmatrix} v \\ w \\ z \end{bmatrix} \\
    &= \det\begin{bmatrix} w \\ z \\ v \end{bmatrix} \\
    &= \ev{w, v \times z} \\
    &= \det\begin{bmatrix} w \\ z \\ v \end{bmatrix} \\
    &= \det\begin{bmatrix} z \\ v \\ w \end{bmatrix} \\
    &= \ev{z, v \times w}.
\end{align*}
$$

For each $i = 1, 2, 3$,

$$
\begin{align*}
  (v \times (w \times z))^i
    &= v^{i + 1}(w \times z)^{i - 1} - v^{i - 1}(w \times z)^{i + 1} \\
    &= v^{i + 1}(w^iz^{i + 1} - w^{i + 1}z^i) - v^{i - 1}(w^{i - 1}z^i - w^iz^{i - 1}) \\
    &= (v^{i - 1}z^{i - 1} + v^iz^i + v^{i + 1}z^{i + 1})w^i - (v^{i - 1}w^{i - 1} + v^iw^i + v^{i + 1}w^{i + 1})z^i \\
    &= \ev{v, z}w^i - \ev{v, w}z^i.
\end{align*}
$$

For each $i = 1, 2, 3$,

$$
\begin{align*}
  ((v \times w) \times z)^i
    &= (v \times w)^{i + 1}z^{i - 1} - (v \times w)^{i - 1}z^{i + 1} \\
    &= (v^{i - 1}w^i - v^iw^{i - 1})z^{i - 1} - (v^iw^{i + 1} - v^{i + 1}w^i)z^{i + 1} \\
    &= (v^{i - 1}z^{i - 1} + v^{i + 1}z^{i + 1})w^i - (w^{i - 1}z^{i - 1} + w^{i + 1}z^{i + 1})v^i \\
    &= (v^{i - 1}z^{i - 1} + v^iz^i + v^{i + 1}z^{i + 1})w^i - (w^{i - 1}z^{i - 1} + w^iz^i + w^{i + 1}z^{i + 1})v^i \\
    &= \ev{v, z}w^i - \ev{w, z}v^i.
\end{align*}
$$

Similarly,


## 5

$$
\begin{align*}
  \ev{v, v} \cdot \ev{w, w} - \ev{v, w}^2
    &= (v_1^2 + v_2^2 + v_3^2)(w_1^2 + w_2^2 + w_3^2) - (v_1w_1 + v_2w_2 + v_3w_3)^2 \\
    &= \sum_{i, j} v_i^2w_j^2 - \sum_{i, j}(v_iw_i)(v_jw_j) \\
    &= \sum_{i \ne j} v_i^2w_j^2 - 2\sum_{i < j}(v_iw_i)(v_jw_j) \\
    &= \sum_{i < j} [v_i^2w_j^2 - 2(v_iw_i)(v_jw_j) + v_j^2w_i^2] \\
    &= \sum_{i < j} (v_iw_j - v_jw_i)^2 \\
    &= (v_2w_3 - v_3w_2)^2 + (v_3w_1 - v_1w_3)^2 + (v_1w_2 - v_2w_1)^2 \\
    &= \abs{\ev{v_2w_3 - v_3w_2, v_3w_1 - v_1w_3, v_1w_2 - v_2w_1}} \\
    &= \abs{v \times w}.
\end{align*}
$$
