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
1. A point is in $\overline{A}$ if and only if every neighborhood of it contains a point of $A$.
1. $\overline{A} = A \cup \partial A = \Int{A} \cup \partial A$.
1. $\Int{A}$ and $\Ext{A}$ are open in $X$, while $\overline{A}$ and $\partial{A}$ are closed in $X$.
1. The following are equivalent:
    * $A$ is open in $X$.
    * $A = \Int{A}$.
    * $A$ contains none of its boundary points.
    * Every point of $A$ has a neighborhood contained in $A$.

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

## 4
A point is in $\overline{A}$ if and only if it is not in $\Ext{A}$.
A point is not in $\Ext{A}$ if and only if it does not have a neighborhood contained in $X \setminus A$ by (2).
A point does not have a neighborhood contained in $X \setminus A$ if and only if every neighborhood of it contains a point in $A$.

## 5
We will first show that $\overline{A} = \Int{A} \cup \partial A$.

* $\overline{A} \subset \Int{A} \cup \partial A$.

Let $x \in \overline{A}$.
Suppose $x \notin \Int{A}$.
Then $x$ has no neighborhood contained in $A$.
In other words, every neighborhood of $x$ contains a point of $X \setminus A$.

Suppose that $x$ has a neighborhood $U$ that does not contain a point of $A$.
Then $U^c$ is a closed subset of $X$ that contains $A$.
Thus $\overline{A} \subset U^c$.
However, $x \in \overline{A}$ and $x \notin U^c$, so this is impossible.
Thus every neighborhood of $x$ contains a point of $A$.
By (3), $x \in \partial A$.
Therefore, $\overline{A} \subset \Int{A} \cup \partial A$.

* $\Int{A} \cup \partial A \subset \overline{A}$.

$\Int{A} \subset A \subset \overline{A}$.
Let $x \in (\partial A) \setminus \Int{A}$.
If there exists no such element, we are done.

Suppose $x \notin \overline{A}$.
Then there exists a closed set $C$ such that $A \subset C$ and $x \notin C$.
Then $C^c$ is a neighborhood of $x$ that contains no points of $A$.
However, this is impossible by (3) since $x$ is in $\partial A$.
Therefore, $x \in \overline{A}$.

Since $\Int{A} \subset A \subset \overline{A}$, $\Int{A} \cup \partial A \subset A \cup \partial A \subset \overline{A}$.
Since $\Int{A} \cup \partial A = \overline{A}$, the three sets are equal to each other.

## 6
$\Int{A}$ is the union of open sets, so it is open.
$\overline{A}$ is the intersection of closed sets, so it is closed.

$\Ext{A} = X \setminus \overline{A}$, so $\Ext{A}$ is open.
This implies $\Int{A} \cup \Ext{A}$ is open, so $\partial A = X \setminus (\Int{A} \cup \Ext{A})$ is open.

## 7
If $A$ is open in $X$, every point has a neighborhood contained in $A$.
Thus every point of $A$ is in $\Int{A}$, so $A = \Int{A}$.

Suppose $A = \Int{A}$.
Let $x$ be a boundary point of $A$.
By (3), every neighborhood of $x$ contains both a point of $A$ and a point of $X \setminus A$.
By (1), $x$ is not a point of $\Int{A}$.
Thus $A$ contains none of its boundary point.

Suppose $A$ contains none of its boundary points.
Let $x \in A$.
Then every neighborhood of $x$ contains $x$, which is a point of $A$.
Since $x$ is not a boundary point, there exists a neighborhood of $x$ that doesn't contain a point of $X \setminus A$.
In other words, there exists a neighborhood of $x$ that is completely contained in $A$.
Therefore, $A$ is open.
