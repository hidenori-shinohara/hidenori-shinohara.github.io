---
layout: post
title:  "Some elementary examples of topologies"
date:   2019-08-11
author: Hidenori
---

# Proposition
1. Let $X$ be any set whatsoever, and let $\mathscr{T} = \mathscr{P}(X)$ (the power set of $X$, which is the set of all subsets of $X$), so every subset of $X$ is open.
   This is called the discrete topology on $X$, and $(X, \mathscr{T})$ is called a discrete space.
1. Let $Y$ be any set, and let $\mathscr{T} = \\{ Y, \emptyset \\}$.
   This is called the trivial topology on $Y$.
1. Let $Z$ be the set $\\{ 1, 2, 3 \\}$, and declare the open subsets to be $\\{ 1 \\}, \\{ 1, 2 \\}, \\{ 1, 2, 3 \\}$, and the empty set.

# Solution
## 1
* $X$ and $\emptyset$ are open subsets.
* Any intersection of finitely many open subsets of $X$ is a subset of $X$, so it is in $\mathscr{T}$.
* Any union of arbitrarily many open subsets of $X$ is a subset of $X$, so it is in $\mathscr{T}$.

## 2
* $Y$ and $\emptyset$ are open subsets.
* The only sets in $\mathscr{T}$ are $\emptyset$ and $Y$.
  Any intersection of them is either $\emptyset$ or $Y$, so it is in $\mathscr{T}$.
* Any union of elements in $Y$ is either $\emptyset$ or $Y$, so it is in $\mathscr{T}$.

## 3
* $Z$ and $\emptyset$ are both open.
* Since $\emptyset \subset \\{ 1 \\} \subset \\{ 1, 2 \\} \subset \\{ 1, 2, 3 \\}$, any intersection of them is just the "smallest" one.
  Thus an intersection of any elements in $Z$ is in $Z$.
* Similarly, any union of them is just the "largest" one.
  Thus a union of any elements in $Z$ is in $Z$.
