---
layout: post
title:  "Examples of Hypersurfaces"
date:   2019-09-24
author: Hidenori
---

# Simplified definition
Let $F \in \mathbb{C}[x_1, x_2]$ be given.
Then the locus $X = V(F) = \\{ (a, b) \in \mathbb{C}^2 \mid F(a, b) = 0 \\}$ is a hypersurface.

This is not the correct definition, but this is sufficient for this post.
See P.3 of Undergraduate Commutative Algebra for the correct definition.

# Example 1
Let $F(x_1, x_2) = x_1 + x_2$.
Then $X = V(F(x_1, x_2)) = \{ (a, -a) \mid a \in \mathbb{C} \}$.
For instance, $(3, -3), (-7, 7) \in X$.

Let $g_1(x_1, x_2) = 2x_1 + 3x_2, g_2(x_1, x_2)= 3x_1 + 4x_2$.

Then $g_1(x_1, x_2) + (F(x_1, x_2)) = g_2(x_1, x_2) + (F(x_1, x_2)) \in \mathbb{C}[x_1, x_2] / (F(x_1, x_2))$.

Then $g_1(3, -3) = 6 - 9 = -3$ and $g_2(3, -3) = 9 - 12 = -3$.
Moreover, $g_1(-7, 7) = 7$ and $g_2(-7, 7) = -21 + 28 = 7$.

This makes sense because for every $(a, b) \in X, F(a, b) = 0$.
If $g_1(x_1, x_2) + (F(x_1, x_2)) = g_2(x_1, x_2) + (F(x_1, x_2))$, then $g_1(x_1, x_2) - g_2(x_1, x_2) + (F(x_1, x_2)) = 0$.
Thus $g_1(a, b) - g_2(a, b) = 0$ for all $(a, b) \in X$.

Moreover, $(F(x_1, x_2))$ is the ideal containing all polynomials $G(x_1, x_2) \in \mathbb{C}[x_1, x_2]$ such that $\forall (a, b) \in X, G(a, b) = 0$.
In other words, $(F(x_1, x_2))$ is the ideal of all polynomials vanishing on $X$.
The textbook claims that this is true when $F$ has no multiple factors.

# Example 2
