---
layout: post
title:  "Cross products and determinants"
date:   2019-12-19
author: Hidenori
---

# Proposition
If $w_1, \cdots, w_{n - 1} \in \mathbb{R}^n$, show that

$$
\begin{align*}
  \abs{w_1 \times \cdots \times w_{n - 1}} = \sqrt{\det(g_{ij})},
\end{align*}
$$

where $g_{ij} = \ev{w_i, w_j}$.

# Solution

Suppose $w_1, \cdots, w_{n - 1}$ are linearly dependent.
Then $w_1 \times \cdots \times w_{n - 1} = 0$ because $\ev{w_1 \times \cdots \times w_{n - 1}, v} = 0$ for any $v$.

Let $a_1, \cdots, a_{n - 1} \in \mathbb{R}$ be chosen such that they are not all 0 and $a_1w_1 + \cdots + a_{n - 1}w_{n - 1} = 0$.
Then for each $i$,

$$
\begin{align*}
  0 &= \ev{a_1w_1 + \cdots + a_{n - 1}w_{n - 1}, w_i} \\
    &= a_1\ev{w_1, w_i} + \cdots + a_{n - 1}\ev{w_{n - 1}, w_i} \\
    &= a_1g_{1, i} + \cdots + a_{n - 1}g_{n - 1, i}.
\end{align*}
$$

Therefore,

$$
\begin{align*}
  a_1\begin{bmatrix} g_{1,1} \\ \vdots \\ g_{1,n - 1} \end{bmatrix} +
  \cdots
  + a_{n - 1}\begin{bmatrix} g_{n - 1,1} \\ \vdots \\ g_{n - 1,n - 1} \end{bmatrix} = 0.
\end{align*}
$$

Thus $\det(g_{ij}) = 0$, so we are done.

Suppose $w_1, \cdots, w_{n - 1}$ are linearly independent.
Let $V$ be the $(n - 1)$-dimensional vector space spanned by $w_1, \cdots, w_{n - 1}$.
Let $w_n = \frac{w_1 \times \cdots \times w_{n - 1}}{\abs{w_1 \times \cdots \times w_{n - 1}}}$.
Define 

$$
\begin{align*}
  \phi(x_1, \cdots, x_{n - 1}) = \det \begin{bmatrix} x_1 \\ \vdots \\ x_{n - 1} \\ w_n \end{bmatrix}.
\end{align*}
$$

Then $\phi$ is clearly multi-linear and alternating, so $\phi \in \Lambda^{n - 1}(V)$.
Moreover,

$$
\begin{align*}
  \phi(w_1, \cdots, w_{n - 1})
    &= \det \begin{bmatrix} w_1 \\ \vdots \\ w_{n - 1} \\ w_n \end{bmatrix} \\
    &= \ev{w_1 \times \cdots \times w_{n - 1}, w_n} \\
    &= \frac{\ev{w_1 \times \cdots \times w_{n - 1}, w_1 \times \cdots \times w_{n - 1}}}{\abs{w_1 \times \cdots \times w_{n - 1}}} \\
    &= \abs{w_1 \times \cdots \times w_{n - 1}}.
\end{align*}
$$

Thus, [by Problem 4-3(Spivak)](/2019/11/24/volume-element-det-ex-4-3.html), it suffices to show that $\phi$ is a volume element determined by $\ev{,}$ and some orientation $\mu$.  

Since $V$ is an $(n - 1)$-dimensional vector space, there exists an orthonormal basis $u_1, \cdots, u_{n - 1}$ with respect to the usual inner product $\ev{,}$.
Let $i$ be given.
Then $\ev{u_i, w_n} = \ev{\sum_{j=1}^{n-1} a_jw_j, w_n} = \sum_{j=1}^{n-1} a_j\ev{w_j,w_n} = 0$.
Moreover, $\ev{w_n, w_n} = 1$.
Therefore, $\\{ u_1, \cdots, u_{n - 1}, w_n \\}$ is an orthonormal basis of $\mathbb{R}^n$ with respect to $\ev{,}$.
This implies that $\phi(u_1, \cdots, u_{n - 1}, w_n) = \pm 1$ because $$\begin{bmatrix} u_1 \\ \vdots \\ u_{n - 1} \\ w_n \end{bmatrix}$$ is an [orthogonal matrix](https://en.wikipedia.org/wiki/Orthogonal_matrix), and the determinant of every orthogonal matrix is $\pm 1$.


If $\phi(u_1, \cdots, u_{n - 1}, w_n) = -1$, then set $u_1$ to be $-u_1$.
Then $\phi(u_1, \cdots, u_{n - 1}, w_n) = 1$.
We claim that $\phi$ is the volume element determined by $\ev{,}$ and $\mu = [u_1, \cdots, u_{n - 1}]$.

Let $v_1, \cdots, v_{n - 1}$ be an orthonormal basis of $V$ with $[v_1, \cdots, v_{n - 1}] = [u_1, \cdots, u_{n - 1}]$.
Using the exact same argument as above, $\phi(v_1, \cdots, v_{n - 1}) = \pm 1$.
By the discussion on PP.82-83 on Spivak, the sign of $\phi(v_1, \cdots, v_{n - 1})$ is equal to the sign of $\phi(u_1, \cdots, u_{n - 1})$.
Therefore, $\phi(v_1, \cdots, v_{n - 1}) = 1$.

Hence, $\phi$ is indeed the volume element determined by $\ev{,}$ and $\mu$.
[By Problem 4-3(Spivak)](/2019/11/24/volume-element-det-ex-4-3.html), $\abs{w_1 \times \cdots \times w_{n - 1}} = \sqrt{\det(g_{ij})}$.
