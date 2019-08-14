---
layout: post
title:  "Continuous maps from $S^n$ into $S^n$ are homotopic if $f(x) \\ne -g(x)$"
date:   2019-08-14
author: Hidenori
---

# Proposition
Suppose $f, g: S^n \rightarrow S^n$ are continuous maps such that $f(x) \ne -g(x)$ for any $x \in S^n$.
Prove that $f$ and $g$ are homotopic.

# Solution
$S^n = \\{ x \in \mathbb{R}^{n + 1} \mid \abs{x} = 1 \\}$.

Let continuous functions $f, g: S^n \rightarrow S^n$ be given such that $f(x) \ne -g(x)$.
Let $F: S^n \times I \rightarrow S^n$ be defined such that

$$
\begin{align*}
  F(x, t) = \frac{tf(x) + (1 - t)g(x)}{\abs{tf(x) + (1 - t)g(x)}}.
\end{align*}
$$

We will show that $F$ is well-defined.

* Let $t \in I, x \in S^n$ such that $tf(x) + (1 - t)g(x) = 0$.
  If $t = 0$, then $g(x) = 0$, which is impossible.
  Suppose $t \ne 0$.
  Then $f(x) = (1 - 1/t)g(x)$.
  By taking the absolute value of each side, we get $1 = \abs{1 - 1/t}$.
  This is possible if and only if $1 / t = 0, 2$.
  Thus $t$ must be $1 / 2$.
  This implies that $f(x) = -g(x)$, but we assumed at the beginning that $f(x) \ne -g(x)$.
  Thus there exists no such pair.
* $\abs{F(x, t)} = 1$ for any $x \in S^n$ and any $t \in I$, so $F(x, t)$ indeed maps $S^n$ into $S^n$.

Therefore, $F$ is well-defined.
Moreover, it is continuous since each operation (scalar multiplication, taking the absolute value, ...) is continuous.

* For any $x \in S^n$, $F(x, 0) = g(x) / \abs{g(x)} = g(x)$.
* For any $x \in S^n$, $F(x, 1) = f(x) / \abs{f(x)} = f(x)$.

Therefore, $F$ is a homotopy from $g$ to $f$, so $f$ and $g$ are homotopic.
