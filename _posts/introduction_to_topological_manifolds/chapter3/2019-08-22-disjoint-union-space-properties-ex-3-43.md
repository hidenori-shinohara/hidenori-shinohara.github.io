---
layout: post
title:  "Properties of Disjoint Union Spaces"
date:   2019-08-22
author: Hidenori
---

# Proposition
Let $$(X_{\alpha})_{\alpha \in A}$$ be an indexed family of topological spaces.

1. A subset of $$\coprod_{\alpha \in A} X_{\alpha}$$ is closed if and only if its intersection with each $X_{\alpha}$ is closed.
1. TODO
1. TODO
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
TODO

## 3
TODO

## 4
TODO

## 5
TODO
