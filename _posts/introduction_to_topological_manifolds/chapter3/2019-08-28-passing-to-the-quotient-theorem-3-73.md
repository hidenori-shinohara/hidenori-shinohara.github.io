---
layout: post
title:  "Passing to the Quotient"
date:   2019-08-28
author: Hidenori
---

# Proposition
Suppose $q: X \rightarrow Y$ is a quotient map, $Z$ is a topological space, and $f: X \rightarrow Z$ is any continuous map that is constant on the fibers of $q$
(i.e., if $q(x) = q(x')$, then $f(x) = f(x')$).
Then there exists a unique continuous map $\tilde{f}: Y \rightarrow Z$ such that $f = \tilde{f} \circ q$.

# Solution
Let $y \in Y$ be given.
Since $q$ is surjective, there exists an $x \in X$ such that $q(x) = y$.
Let $\tilde{f}(y) = f(x)$.

This is well defined because for any $x, x' \in X$ such that $q(x) = y = q(x')$, we know that $f(x) = f(x')$.

Let $g$ be another function that satisfies $f = g \circ q$.
Let $y \in Y$.
Then there exists an $x \in X$ such that $q(x) = y$ because $q$ is surjective.
Then $\tilde{f}(q(x)) = f(x) = g(q(x))$.
Thus $\tilde{f}(y) = g(y)$, so $\tilde{f} = g$.

Thus we have shown that there exists a unique map $\tilde{f}: Y \rightarrow Z$ such that $f = \tilde{f} \circ g$.
Let $U \subset Z$.
Then $f^{-1}(U)$ is open in $X$ because $f$ is continuous.
Then $f^{-1}(U) = q^{-1}((\tilde{f})^{-1}(U))$ is open.
Since $q$ is a quotient map, this implies $(\tilde{f})^{-1}(U)$ is open.
Therefore, $\tilde{f}$ is continuous.
