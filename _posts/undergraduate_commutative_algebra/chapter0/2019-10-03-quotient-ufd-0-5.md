---
layout: post
title: "Geometric interpretation when a polynomial ring quotient by a principal ideal is not a UFD"
date:   2019-10-03
author: Hidenori
---


# Example

Let $F(x, y, z) = xy - z^2 \in \mathbb{C}[x, y, z]$.
Since $\mathbb{C}$ is a field, it is a UFD.
By Theorem 7 on P.304 of Dummit and Foote, $\mathbb{C}[x]$ is a UFD.
By applying the same theorem repeatedly, we have that $\mathbb{C}[x, y, z]$ is a UFD.
By Proposition 12 on P.286 of Dummit and Foote, $(F)$ is a prime ideal if and only if $F$ is irreducible.

$xy - z^2$ is a quadratic polynomial of $z$ with coefficients in $\mathbb{C}[x, y]$.
Thus $xy - z^2$ is irreducible if and only if $\delta = 0^2 - 4 \cdot (-1) \cdot (xy) = 4xy$ is in $(\mathbb{C}[x, y])^2$.
Let $p \in (\mathbb{C}[x])[y]$ be given.
Then $p$ is a polynomial of $y$.
Then $\deg(p^2) = \deg(p) + \deg(p) = 2\deg(p)$ because $\mathbb{C}[x]$ is an integral domain.
However, the degree of $4xy \in (\mathbb{C}[x])[y]$ is 1, so there exists no $p \in (\mathbb{C}[x])[y]$ such that $p^2 = 4xy$.
Hence, $4xy \notin (\mathbb{C}[x, y])^2$ and this is irreducible.

Since $(F)$ is a prime ideal, $A = \mathbb{C}[x, y, z] / (F)$ is an integral domain.

However, $(y + (F))^2 = (x + (F))(z + (F))$ in $A$, so $A$ is not a UFD.
(TODO: How can we show that $x + (F), y + (F), z + (F)$ are all irreducibles in $A$?)

Consider $X = \\{ (x, y, z) \in \mathbb{C}^3 \mid F(x, y, z) = 0 \\}$.
Then $X$ is a quadric cone.
(I think this is generated by rotating the $x$-axis around the line $x = z, y = 0$.)

The line $L: x = y = 0$ is a subset of $X$.
Then $L = V(x + (F), y + (F)) = \\{ (x, y, z) \in \mathbb{C}^3 \mid x = 0 \land y = 0 \\}$.
But there exists no principal ideal of $A$ whose vanishing set equals $L$.
Similarly, the line $L': y = z = 0$ is a subset of $X$, and there exists no principal ideal of $A$ whose vanishing set equals $L'$.
