---
layout: post
title:  "Divergence, curl, and gradient(WIP)"
date:   2019-12-14
author: Hidenori
---

# Proposition
If $F$ is a vector field on $\mathbb{R}^3$, define the forms

$$
\begin{align*}
  \omega^1_F &= F^1dx + F^2dy + F^3dx \\
  \omega^2_F &= F^1dy \wedge dx + F^2dz \wedge dx + F^3 dx \wedge dy
\end{align*}
$$

1. Prove that

   $$
   \begin{align*}
     df &= \omega^1_{\grad f}, \\
     d(\omega^1_p) &= \omega^2_{\curl F}, \\
     d(\omega^2_p) &= (\div F) dx \wedge dy \wedge dz.
   \end{align*}
   $$
1. TODO
1. TODO

# Solution
## 1

Let $f: \mathbb{R}^3 \rightarrow \mathbb{R}$.

$$
\begin{align*}
  df
    &= D_1fdx^1 + D_2fdx^2 + D_3fdx^3 \\
    &= \omega^1_{\grad f}
\end{align*}
$$

where $\grad f = D_1f \cdot e_1 + D_2f \cdot e_2 + D_3f \cdot e_3$.


$$
\begin{align*}
  d\omega^1_F
    &= d(F^1dx + F^2dy + F^3dz) \\
    &= (D_2F^3 - D_3F^2)dy \wedge dz + (D_1F^3 - D_3F^1)dx \wedge dz + (D_1F^2 - D_2F^1)dy \wedge dz \\
    &= \omega^2_{\curl F}
\end{align*}
$$

where $\curl F = (D_2F^3 - D_3F^2)e_1 + (D_1F^3 - D_3F^1)e_2 + (D_1F^2 - D_2F^1)e_3$.

$$
\begin{align*}
  d(\omega^2_F)
    &= d(F^1 dy \wedge dz + F^2 dz \wedge dx + F^3 dx \wedge dy) \\
    &= D_1F^1 dx \wedge dy \wedge dz + D_2F^2 dy \wedge dz \wedge dx + D_3F^3 dz \wedge dx \wedge dy \\
    &= (D_1F^1 + D_2F^2 + D_3F^3) dx \wedge dy \wedge dz \\
    &= (\div F) dx \wedge dy \wedge dz.
\end{align*}
$$

## 2
TODO

## 3
TODO
