---
layout: post
title:  "Basic properties of the interior, exterior, and boundary of a topological space"
date:   2019-09-01
author: Hidenori
---

# Proposition
Let $X$ be a topological space and let $A \subset X$ be any subset.

1. A point is in $\Int{A}$ if and only if it has a neighborhood contained in $A$.
1. A point is in $\Ext{A}$ if and only if it has a neighborhood contained in $X \setminus A$.
1. A point is in $\partial A$ if and only if every neighborhood of it contains both a point of $A$ and a point of $X \setminus A$.

# Solution
## 1
Let $x \in X$.

Suppose $x \in \Int{A}$.
Since $\Int{A}$ is the union of all open subsets of $X$ that are contained in $A$, there must exist an open $U \subset X$ such that $x \in U \subset A$.
Then $U$ is a neighborhood of $x$ contained in $A$.

On the other hand, suppose that $x$ has a neighborhood contained in $A$.
Let $U$ denote such a neighborhood.
Then $U$ is an open subset of $X$ contained in $A$, so $U \subset \Int{A}$.
Therefore, $x \in \Int{A}$.

## 2

Let $x \in X$.

Suppose $x \in \Ext{A}$.
Then $x \notin \overline{A}$.
Since $\overline{A}$ is the intersection of all closed sets containing $A$, there exists a closed set $C \subset X$ such that $x \notin C$ and $A \subset C$.
Then $C^c$ is a neighborhood of $x$ that is disjoint from $A$.
In other words, $x \in C^c \subset X \setminus A$.

On the other hand, suppose that $x$ has a neighborhood contained in $X \setminus A$.
Let $U$ denote such a neighborhood.
Then $U^c$ is a closed subset of $X$ containing $A$.
Therefore, $\overline{A} \subset U^c$.
This implies that $x \notin \overline{A}$, so $x \in \Ext{A}$.

## 3

Let $x \in X$.
* $x \notin \Int{A}$ if and only if every neighborhood of $x$ is not contained in $A$ by (1).
  In other words, $x \notin \Int{A}$ if and only if every neighborhood of $x$ contains a point in $X \setminus A$.
* Since $x \notin \Ext{A}$, every neighborhood of $x$ is not contained in $X \setminus A$.
  In other words, $x \notin \Ext{A}$ if and only if every neighborhood of $x$ contains a point in $A$.

Let $x \in \partial A$.
Then $x \notin \Int{A}$ and $x \notin \Ext{A}$.
Therefore, every neighborhood of $x$ contains a point in $A$ and a point in $X \setminus A$.

On the other hand, if every neighborhood of $x$ contains both a point of $A$ and a point of $X \setminus A$.
Then $x \notin \Int{A}$ and $x \notin \Ext{A}$, so $x \notin \partial A$.

