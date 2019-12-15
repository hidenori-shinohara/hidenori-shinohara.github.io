---
layout: post
title:  "Divergence, curl, and gradient"
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
1. Use (1) to prove that

   $$
   \begin{align*}
     \curl \grad f &= 0, \\
     \div \curl f &= 0.
   \end{align*}
   $$

1. If $F$ is a vector field on a star-shaped open set $A$ and $\curl F = 0$, show that $F = \grad f$ for some function $f: A \rightarrow R$.
   Similarly, if $\div F = 0$, show that $F = \curl G$ for some vector field $G$ on $A$.

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

$$
\begin{align*}
  \omega^2_{\curl(\grad F)}
    &= d(\omega^1_{\grad F}) \\
    &= d(dF) \\
    &= d^2F = 0. \\
  \div(\curl F) dx \wedge dy \wedge dz
    &= d(\omega^2_{\curl F}) \\
    &= d(d(\omega^1_F)) \\
    &= d^2(\omega^1_F) \\
    &= 0.
\end{align*}
$$

## 3
Let $F$ be a vector field such that $\curl F = 0$.
Then $$d(\omega^{1}_{F}) = \omega^2_{\curl F} = \omega^2_0 = 0$$.
Therefore, $$\omega^1_{F}$$ is closed.
By Poincare Lemma[Theoem 4-11, Spivak], $$\omega^1_{F}$$ is exact.
Let $$f: A \rightarrow \mathbb{R}$$ be a 0-form such that $$df = \omega^{1}_F$$.
In Part 1, we showed that $$df = \omega^{1}_{\grad f}$$.
Therefore, $$F = \grad f$$.

Similarly, suppose $$\div F = 0$$.
Then $$d(\omega^2_{F}) = (\div F)dx \wedge dy \wedge dz = 0$$.
Therefore, $$\omega^2_F$$ is a closed 2-form.
By Poincare Lemma, there exists a 1-form $$G^1dx + G^2dy + G^3dz$$ such that $$d(G^1dx + \cdots + G^3dz) = \omega^2_F$$.
Let $$G$$ be a vector field such that $$G(p) = (G^1(p)e^1 + G^2(p)e^2 + G^3(p)e^3)_{(p)}$$.
Then $$\omega^2_F = d(G^1dx + \cdots + G^3dz) = d(\omega^1_G) = \omega^2_{\curl G}$$.
Therefore, we found a vector field $$G$$ such that $$F = \curl G$$.
