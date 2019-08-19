---
layout: post
title:  "Sequence Lemma"
date:   2019-08-18
author: Hidenori
---

# Proposition
Suppose $X$ is a first-countable space, $A$ is any subset of $X$, and $x$ is any point of $X$.

1. $x \in \overline{A}$ if and only if $x$ is a limit point of a sequence of points in $A$.
1. $x \in \Int{A}$ if and only if every sequence in $X$ converging to $x$ is eventually in $A$.
1. $A$ is closed in $X$ if and only if $A$ contains every limit of every convergent sequence of points in $A$.
1. TODO

# Solution
## 1
Let $\\{ x_n \\}$ be a sequence of points in $A$.
Suppose $x_n$ converges to $x$.
Suppose $x \notin \overline{A}$.
Then there exists a closed set $C \subset X$ such that $x \notin C$ and $A \subset C$.
Then $C^c$ is a neighborhood of $x$ that contains no points from $\\{ x_n \mid n \in \mathbb{N} \\}$.
This implies that $x_n$ does not converge to $x$.
This is a contradiction, so $x \in \overline{A}$.

On the contrary, suppose that $x \in \overline{A}$.
Since $X$ is first countable, $x$ has a countable neighborhood basis.
Let $\\{ B_1, B_2, \cdots \\}$ denote such a countable neighborhood basis.

We claim that $A \cap B_1 \cap B_2 \cap \cdots \cap B_n \ne \emptyset$ for each $n \in \mathbb{N}$.

Suppose that $A \cap B_1 \cap \cdots \cap B_n = \emptyset$.

$B_1 \cap \cdots \cap B_n$ is the intersection of finitely many open sets.
Thus it is open.
Then $(B_1 \cap \cdots \cap B_n)^c$ is a closed set containing $A$.
Thus $\overline{A} \subset (B_1 \cap \cdots \cap B_n)^c$.
* $x \in \overline{A}$.
* Each $B_i$ is a neighborhood of $x$, so $x \in B_1 \cap \cdots \cap B_n$.
  Therefore, $x \notin (B_1 \cap \cdots \cap B_n)^c$.

This is a contradiction, so $A \cap B_1 \cap \cdots \cap B_n \ne \emptyset$.

For each $n \in \mathbb{N}$, let $x_n \in A \cap B_1 \cap \cdots \cap B_n$.
This is possible because we showed that the intersection is nonempty.
Then $\\{ x_n \\}$ is a sequence in $A$.

Let $U$ be a neighborhood of $x$.
Then $B_k \subset U$ for some $k \in \mathbb{N}$.
For all $n \geq k$, $x_n \in A \cap B_1 \cap \cdots \cap B_k \cap \cdots \cap B_n \subset B_k \subset U$.
Thus $x_n$ converges to $x$.

Note that the first part that states a limit of a sequence is in the boundary can be proved without first countability.
This is true for any topological space.
This lemma is important because of the other direction.
When we say $x \in \overline{A}$, we expect that $x$ is in or "right next to" $A$.
However, this is not always true.
Consider $\mathbb{R}$ with the co-countable topology.
Let $A = [0, 1]$.
Let $C$ be a closed set containing $A$.
Then $C^c$ is an open set disjoint from $A$.
Since the complement of an non-empty open set must be countable, $C^c = \emptyset$.
Thus the only closed set covering $A$ is $\mathbb{R}$, so the closure of $A$ is $\mathbb{R}$.
This is "much bigger" than $A$.

$2 \in \overline{A}$.
Let $\\{ a_n \\}$ be a sequence in $A$.
Let $U = \mathbb{R} \setminus \\{ a_n \mid n \in \mathbb{N} \\}$.
Then $U$ is open because its complement is countable.
$U$ must contain $2$ because $2 \notin \\{ a_n \mid n \in \mathbb{N} \\}$.
Therefore, we found a neighborhood of $2$ which contains no term of $\\{ a_n \\}$, so no sequence in $A$ converges to $2$.

## 2
Suppose that every sequence in $X$ converging to $x$ is eventually in $A$.
Let $B = \\{ B_1, B_2, \cdots \\}$ be a neighborhood basis for $X$ at $x$.
We claim that there exists an $n \in \mathbb{N}$ such that $B_1 \cap B_2 \cap \cdots \cap B_n \subset A$.
Suppose otherwise.

That means that $\forall n \in \mathbb{N}$, $(B_1 \cap B_2 \cap \cdots \cap B_n) \setminus A \ne \emptyset$.
For each $n \in \mathbb{N}$, let $a_n \in (B_1 \cap B_2 \cap \cdots \cap B_n) \setminus A$.
Then we have a sequence $\\{ a_n \\}$.
Let $U$ be a neighborhood of $x$.
Since $B$ is a neighborhood basis for $X$ at $x$, there exists a $k \in \mathbb{N}$ such that $B_k \subset U$.
Then $\forall n \geq k$, $a_n \in B_1 \cap B_2 \cap \cdots \cap B_n \subset B_k \subset U$.
Therefore, $\\{ a_n \\}$ converges to $x$.
This implies that $\\{ a_n \\}$ is eventually in $A$.
However, we specially picked each $a_n$ from the complement of $A$.
This is a contradiction, so there must exist an $n \in \mathbb{N}$ such that $B_1 \cap B_2 \cap \cdots \cap B_n \subset A$.
$B_1 \cap \cdots \cap B_n$ is the intersection of $n$ open sets, so it is open.
Thus it is a neighborhood of $x$ that is contained in $A$, so $x \in \Int{A}$.

## 3
Suppose $A$ is closed in $X$.
Then $A = \overline{A}$.
Let $\\{ a_n \\}$ be a convergent sequence in $A$.
Let $x$ denote $\\{ a_n \\}$'s limit.
By (1), $x \in \overline{A}$.
Thus $x \in A$.
Therefore, every limit of every convergent sequence of points in $A$ is in $A$.

Suppose that $A$ contains every limit of every convergent sequence of points in $A$.
Let $x \in \overline{A}$.
By (1), $x$ is a limit point of a sequence of points in $A$.
Thus $x \in A$.
This implies that $\overline{A} \subset A$.
By definition, $A \subset \overline{A}$, so $A = \overline{A}$.
Therefore, $A$ is closed.


## 4
TODO
