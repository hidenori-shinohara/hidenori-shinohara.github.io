---
layout: post
title:  "A necessary and sufficient condition for an ideal to be prime"
date:   2019-11-10
author: Hidenori
---

# Proposition
Show that an ideal $I$ is prime if and only if for any ideals $J$ and $K$ such that $JK \subset I$, either $J \subset I$ or $K \subset I$.

# Solution
Let ideals $J, K$ be given such that $J \not\subset I$ and $K \not\subset I$.
Let $j \in J \setminus I$ and $k \in K \setminus I$.
Since $I$ is a prime ideal, $j, k \notin I$ implies that $jk \notin I$.
Therefore, $JK \not\subset I$.
By taking the contrapositive, we have $JK \subset I \implies J \subset I \lor K \subset I$.

On the other hand, suppose that $JK \subset I$ implies $J \subset I$ or $K \subset I$.
Let $ab \in I$.
Let $A = \ev{a}$ and $B = \ev{b}$.
Therefore, $AB = \ev{ab}$ by Proposition 6 on P.191 (Ideals, Varieties and Algorithms)
Then $AB \subset I$, so $A \subset I$ or $B \subset I$.
Specifically, $a \in I$ or $b \in I$.
