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

More generally, it is *believable* that, for arbitrary $f_1, f_2 \in \mathbb{C}[x_1, x_2]$, $f_1(x_1, x_2) + (F(x_1, x_2)) = f_2(x_1, x_2) + (F(x_1, x_2))$ if and only if $\forall (a, b) \in X, f_1(a, b) = f_2(a, b)$.

Therefore, $(F(x_1, x_2))$ is the ideal containing all polynomials $G(x_1, x_2) \in \mathbb{C}[x_1, x_2]$ such that $\forall (a, b) \in X, G(a, b) = 0$.
In other words, $(F(x_1, x_2))$ is the ideal of all polynomials vanishing on $X$.
The textbook claims that this is true when $F$ has no multiple factors.

# Example 2
Let $F(x_1, x_2) = (x_1 - 1)^2$.
Notice that $F$ has a multiple factor.

Then $X = V(F) = \\{ (1, b) \mid b \in \mathbb{C} \\}$.
For instance, $(1, 0), (1, 100) \in X$.

Let $g(x_1, x_2) = x_1 - 1$.
Then $g \notin (F)$.
However, $\forall (1, b) \in X, g(1, b) = 0$.

Thus, in this case, the ideal $(F)$ does not contain all polynomials vanishing on $X$.
Moreover, $(g + (F))(g + (F)) = g^2 + (F) = (x_1 - 1)^2 + (F) = 0$.
Therefore, $g + (F)$ is a nonzero nilpotent element in the quotient ring $A = \mathbb{C}[x_1, x_2] / (F)$.

# Example 3
Let $f_1 = x_1 - 1, f_2 = x_2 - 2$, and $F = f_1f_2$.

Then $f_1 + (F), f_2 + (F)$ are nonzero elements in $\mathbb{C}[x_1, x_2] / (F)$.
Since $(f_1 + (F))(f_2 + (F)) = f_1f_2 + (F) = 0$, $f_1 + (F)$ and $f_2 + (F)$ are zero divisors.

Then $X_1 = \\{ (1, b) \mid b \in \mathbb{C} \\}$, $X_2 = \\{ (a, 2) \mid a \in \mathbb{C} \\}$, and $X = \\{ (a, b) \mid a = 1 \lor b = 2 \\}$.
This means $X_1 \cup X_2 = X$.
In other words, the hypersurface $X$ is the union of two hypersurfaces $X_1, X_2$.

With this example, it is believable that $A$ has zero divisors (not nilpotents) if and only if $X$ is a union of two hypersurfaces.

This is apparently a general pattern according to Undergraduate Commutative Algebra (See P.4)

# Example 4
Let $f = x_1^2 + 3$
Let $f_1 = f, f_2 = f - 1$, and let $F = f_1f_2$.
Then $(f + (F))^2 = f^2 + (F) = f + (F)$, so $f + (F)$ is a nontrivial idempotent.

Then $X_1 = V(f_1) = \\{ (\pm \sqrt{-2}, b) \mid b \in \mathbb{C} \\}$ and $X_2 = V(f_2) = \\{ (\pm \sqrt{-3}, b) \mid b \in \mathbb{C} \\}$.
It is easy to see that $X = V(f) = X_1 \cup X_2$.
Moreover, $X_1 \cap X_2 = \emptyset$, so $X = X_1 \coprod X_2$.

$\mathbb{C}[x_1, x_2]/(f_1) \times \mathbb{C}[x_1, x_2]/(f_2)$ is isomorphic to $\mathbb{C}[x_1, x_2]/(F)$ because $\phi(f + (f_1), g + (f_2)) = fg + (F)$ is an isomorphism.

