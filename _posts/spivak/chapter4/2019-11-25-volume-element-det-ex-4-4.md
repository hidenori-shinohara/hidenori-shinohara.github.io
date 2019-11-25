---
layout: post
title:  "Volume element and $\\det$"
date:   2019-11-25
author: Hidenori
---

# Proposition
If $\omega$ is the volume element of $V$ determined by $T$ and $\mu$, and $f: \mathbb{R}^n \rightarrow V$ is an isomorphism such that $f^{\ast}T = \ev{,}$ and such that $[f(e_1), \cdots, f(e_n)] = \mu$, show that $f^{\ast}\omega = \det$.

# Solution
As mentioned on P.83 [Spivak], $\det$ is the unique element in $\Lambda^n(\mathbb{R}^n)$ with the property that $\det(e_1, \cdots, e_n) = 1$.
Since $f: \mathbb{R}^n \rightarrow V$, $f^{\ast}\omega \in \Lambda^n(\mathbb{R}^n)$.
Therefore, it suffices to show that $f^{\ast}\omega(e_1, \cdots, e_n) = 1$.

By the definition of pull-back, $f^{\ast}\omega(e_1, \cdots, e_n) = \omega(f(e_1), \cdots, f(e_n))$.

We have $T(f(e_i), f(e_j)) = (f^{\ast}T)(e_i, e_j) = \ev{e_i, e_j}$ for any $i, j$.
Thus $T(f(e_i), f(e_j)) = \delta_{i, j}$.
This implies that $\{ f(e_1), \cdots, f(e_n) \}$ is an orthonormal basis of $V$ with respect to $T$ because $\dim(V) = \dim(\mathbb{R}^n) = n$.

Moreover, we are given that $[f(e_1), \cdots, f(e_n)] = \mu$.

Since $\omega$ is the volume element of $V$ determined by $T$ and $\mu$, $\omega(f(e_1), \cdots, f(e_n)) = 1$.
Therefore, we showed that $f^{\ast}\omega(e_1, \cdots, e_n) = 1$, so $f^{\ast}\omega = \det$.
