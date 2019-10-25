---
layout: post
title:  "Two points determine a line, and two lines determine a point"
date:   2019-10-25
author: Hidenori
---

# Proposition
1. Prove that any two distinct points in $\mathbb{P}^2(\mathbb{R})$ determine a unique projective line.
1. Prove that any two distinct projective lines in $\mathbb{P}^2(\mathbb{R})$ meet at a unique point.

# Solution
We will define $\mathbb{P}^2(\mathbb{R})$ as the set containing $\mathbb{R}^2$ and one point at $\infty$ for each equivalence class of parallel lines.

## 1
Let $p_1 \ne p_2$ be given.

1. Suppose $p_1, p_2 \in \mathbb{R}^2$.
   From basic geometry, we know that $p_1, p_2$ determine a unique line in $\mathbb{R}^2$.
   This line can be extended to $\infty$ in $\mathbb{P}^2(\mathbb{R})$.
   Moreover, the line at $\infty$ does not go through $p_1$ and $p_2$.
   Therefore, $p_1, p_2$ uniquely determine a projective line.
1. Suppose $p_1 \in \mathbb{R}^2$ and $p_2$ is a point at infinity.
   We will consider the line with the slope represented by $p_2$ that goes through $p_1$.
   From basic geometry, we know that such a line exists in $\mathbb{R}^2$.
   This line can be extended to $\infty$ in $\mathbb{P}^2(\mathbb{R})$.
   Again, the line at $\infty$ does not go through $p_1$.
   Therefore, $p_1, p_2$ uniquely determine a projective line.
1. Suppose that $p_1, p_2$ are both points at infinity.
   Then the line at $\infty$ goes through both $p_1$ and $p_2$.
   Moreover, no line in $\mathbb{R}^2$ go through $p_1$ and $p_2$ at the same time because they are points at $\infty$ for different classes of parallel lines. 

## 2

Let $l_1 \ne l_2$ be given.

1. Suppose they are not the line at $\infty$.
    1. If they are parallel, they only intersect at the point at infinity for the equivalence class.
       They clearly don't intersect in $\mathbb{R}^2$ or at any other points at $\infty$.
    1. If they are not parallel, they only intersect at a unique point in $\mathbb{R}^2$.
       We know this from basic geometry, and they clearly don't intersect at any point at $\infty$.
1. Suppose that $l_1$ is the line at $\infty$ and $l_2$ is not.
   Then they intersect at the point at infinity for the equivalence class of $l_1$.
   They clearly don't intersect in $\mathbb{R}^2$ or at any other points at $\infty$.
1. It is impossible that they are both the line at infinity because $l_1 \ne l_2$.
