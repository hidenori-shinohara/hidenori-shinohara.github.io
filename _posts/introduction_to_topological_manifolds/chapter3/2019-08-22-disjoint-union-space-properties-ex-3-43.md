---
layout: post
title:  "Properties of Disjoint Union Spaces"
date:   2019-08-22
author: Hidenori
---

# Proposition
Let $$(X_{\alpha})_{\alpha \in A}$$ be an indexed family of topological spaces.

1. A subset of $$\coprod_{\alpha \in A} X_{\alpha}$$ is closed if and only if its intersection with each $X_{\alpha}$ is closed.
1. Each canonical injection $$i_{\alpha}: X_{\alpha} \rightarrow \coprod_{\alpha \in A} X_{\alpha}$$ is a topological embedding and an open and closed map.
1. If each $X_{\alpha}$ is Hausdorff, then so is $\coprod_{\alpha \in A} X_{\alpha}$.
1. TODO
1. TODO

# Solution

First, we will show some properties of disjoint union spaces.
Let $$C \subset \coprod_{\alpha \in A} X_{\alpha}$$.
For each $\alpha$, let $C_{\alpha} = i_{\alpha}(C)$.
Then $C_{\alpha}$ denotes the intersection of $C$ with each $X_{\alpha}$.
Moreover, $$C = \coprod_{\alpha \in A} C_{\alpha}$$ because

$$
\begin{align*}
  (x_0, \alpha_0) \in C
    &\iff x_0 \in C_{\alpha_0} \\
    &\iff (x_0, \alpha_0) \in \coprod_{\alpha \in A} C_{\alpha}.
\end{align*}
$$

We claim that $(\coprod X_{\alpha}) \setminus (\coprod C_{\alpha}) = \coprod (X_{\alpha} \setminus C_{\alpha})$.

$$
\begin{align*}
  (x_0, \alpha_0) \in (\coprod X_{\alpha}) \setminus (\coprod C_{\alpha}) 
    &\iff (x_0, \alpha_0) \notin \coprod C_{\alpha} \\
    &\iff x_0 \notin C_{\alpha_0} \\
    &\iff x_0 \in X_{\alpha_0} \setminus C_{\alpha_0} \\
    &\iff (x_0, \alpha_0) \in \coprod (X_{\alpha} \setminus C_{\alpha}).
\end{align*}
$$

These properties are true for any subset $C$ of $$\coprod_{\alpha \in A} X_{\alpha}$$.


## 1
Let $C \subset \coprod X_{\alpha}$ be a closed subset.
Then $(\coprod X_{\alpha}) \setminus C$ is open.
Let $C_{\alpha}$ defined as above.
$(\coprod X_{\alpha}) \setminus C = (\coprod X_{\alpha}) \setminus (\coprod C_{\alpha}) = \coprod (X_{\alpha} \setminus C_{\alpha})$.

Since $(\coprod X_{\alpha}) \setminus C$ is open, the intersection with each $\alpha$ is open.
The intersection with each $\alpha$ is $X_{\alpha} \setminus C_{\alpha}$.
Thus each $C_{\alpha}$ is closed.
Moreover, the intersection of $C = \coprod C_{\alpha}$ with each $X_{\alpha}$ is $C_{\alpha}$.
Therefore, if $C$ is a closed subset, the intersection of $C$ with each $X_{\alpha}$ is closed.

On the other hand, suppose that the intersection of a subset $C$ with each $X_{\alpha}$ is closed.
Then $C_{\alpha}$ is closed in $X_{\alpha}$ for each $\alpha$, so $X_{\alpha} \setminus C_{\alpha}$ is open for each $\alpha$.
This implies that $\coprod (X_{\alpha} \setminus C_{\alpha})$ is open.
This is equivalent to saying $(\coprod X_{\alpha}) \setminus C$ is open, so $C$ is closed.


## 2
Let $\alpha_0$ be given.

* Injective?
    * For any $x, y \in X_{\alpha_0}$, $i_{\alpha_0}(x) = i_{\alpha_0}(y) \implies (x, \alpha_0) = (y, \alpha_0) \implies x = y$.
* Continuous?
    * Let $U \subset \coprod_{\alpha \in A} X_{\alpha}$ be an open subset.
      Then the intersection $U_{\alpha}$ of $U$ with each $X_{\alpha}$ is open.
      In particular, $U_{\alpha_0}$ is open in $X_{\alpha_0}$.

      $$
      \begin{align*}
        (i_{\alpha_0})^{-1}(U)
          &= (i_{\alpha_0})^{-1}(\coprod_{\alpha \in A} U_{\alpha}) \\
          &= U_{\alpha_0}.
      \end{align*}
      $$

      Therefore, $i_{\alpha_0}$ is continuous.

Hence, $i_{\alpha_0}$ is a topological embedding.

Let $U \subset X_{\alpha_0}$ be an open subset.
Then $i_{\alpha_0}(U) = \coprod_{\alpha \in A} U_{\alpha}$ where

$$
\begin{align*}
  U_{\alpha} &= \begin{cases}
    U & (\alpha = \alpha_0) \\
    \emptyset & (\alpha \ne \alpha_0).
  \end{cases}
\end{align*}
$$

Since each $U_{\alpha}$ is open in their space, $i_{\alpha_0}$ is an open map.

Let $C \subset X_{\alpha_0}$ be a closed subset.
Then $i_{\alpha_0}(C) = \coprod_{\alpha \in A} C_{\alpha}$ where

$$
\begin{align*}
  C_{\alpha} &= \begin{cases}
    C & (\alpha = \alpha_0) \\
    \emptyset & (\alpha \ne \alpha_0).
  \end{cases}
\end{align*}
$$

Since each $C_{\alpha}$ is closed in their space, $i_{\alpha_0}(C)$ is closed by (1).
Therefore, $i_{\alpha_0}$ is a closed map.

## 3
Suppose that each $X_{\alpha}$ is Hausdorff.
Let $(x_1, \alpha_1) \ne (x_2, \alpha_2) \in \coprod X_{\alpha}$ be given.

* Case 1: $\alpha_1 \ne \alpha_2$.
  We claim that $i_{\alpha_1}(X_{\alpha_1}), i_{\alpha_2}(X_{\alpha_2})$ separate $(x_1, \alpha_1), (x_2, \alpha_2)$.
    * By (2), the inclusion maps are open.
      Therefore, $i_{\alpha_1}(X_{\alpha_1}), i_{\alpha_2}(X_{\alpha_2})$ are open.
    * Since $\alpha_1 \ne \alpha_2$, $i_{\alpha_1}(X_{\alpha_1}), i_{\alpha_2}(X_{\alpha_2})$ are disjoint.
* Case 2: $\alpha_1 = \alpha_2$.
  Then $x_1 \ne x_2$.
  Since $X_{\alpha_1}$ is Hausdorff, there exist disjoint neighborhoods $U_1, U_2$ of $x_1, x_2$.
  By (2), $i_{\alpha_1}(U_1), i_{\alpha_1}(U_2)$ are open.
  Since $U_1, U_2$ are disjoint, $i_{\alpha_1}(U_1), i_{\alpha_1}(U_2)$ are disjoint.
  Thus we found disjoint neighborhoods of $(x_1, \alpha_1), (x_2, \alpha_1)$.

Therefore, $\coprod X_{\alpha}$ is Hausdorff.



## 4
TODO

## 5
TODO
