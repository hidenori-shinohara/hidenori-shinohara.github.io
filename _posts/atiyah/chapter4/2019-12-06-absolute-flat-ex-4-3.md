---
layout: post
title:  "Every primary ideal of an absolutely flat ring $A$ is maximal"
date:   2019-12-06
author: Hidenori
---

# Proposition
If $A$ is absolutely flat, every primary ideal is maximal.

# Solution

Let $q$ be a primary ideal of $A$.
It suffices to show that $A / q$ is a field.
By the definition of a primary ideal, $A / q \ne 0$.
Let $x \in A \setminus q$.
By Exercise 2.27[Atiyah], every principal ideal of $A$ is idempotent.

Therefore, $(x) = (x^2)$.
This implies $x \in (x^2)$, so $\exists a \in A, x = ax^2$, which implies $x(ax - 1) = 0$.

Since $0 \in q$, $x(ax - 1) \in q$.
Since $x \notin q$, $(ax - 1)^m \in q$ for some $m \geq 1$.
Therefore, $(ax - 1) + q$ is nilpotent in $A / q$.
By [Exercise 1.1(Atiyah)](/2019/11/22/nilpotent-ex-1-1), $((ax - 1) + q) + (1 + q) = ax + q$ is a unit in $A / q$.
Therefore, $x + q$ is a unit in $A / q$.

