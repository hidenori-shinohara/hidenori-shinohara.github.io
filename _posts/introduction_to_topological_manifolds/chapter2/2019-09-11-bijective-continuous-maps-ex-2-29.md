---
layout: post
title:  "A bijective continuous map is a homeomorphism if and only if it is open or closed"
date:   2019-09-05
author: Hidenori
---

# Proposition
Suppose $f: X \rightarrow Y$ is a bijective continuous map.
Show that the following are equivalent:

1. $f$ is a homeomorphism.
1. $f$ is open.
1. $f$ is closed.

# Solution

## $1 \rightarrow 2$

$f$ is a homeomorphism, so it must be open.

## $2 \rightarrow 3$
Let $C \subset X$ be closed.
Then $f(X \setminus C)$ is open in $Y$ because $f$ is open.
Since $f$ is bijective, $f(X \setminus C) = f(X) \setminus f(C)$.
Thus $f(C)$ is closed in $Y$.

## $3 \rightarrow 1$
Let $U \subset X$ be open.
Then $f(X \setminus U)$ is closed in $Y$ because $f$ is closed.
Since $f$ is bijective, $f(X \setminus U) = f(X) \setminus f(U)$.
Thus $f(U)$ is open in $X$.
