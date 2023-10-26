---
layout: post
title:  "An Introduction to Mathematical Cryptography: Quadratic Residue Mod Prime Powers"
date:   2023-10-15
author: Hidenori
---

Exercise 1.34(a) and 1.35 in _An Introduction to Mathematical Cryptography_.

These exercises are based on a special case of [Hensel's Lemma](https://en.wikipedia.org/wiki/Hensel's_lemma).

Let $p$ be an odd prime and an integer $1 \leq b \leq p - 1$ be given.
Let $S_e = \\{ 1 \leq x \leq p^e - 1 \mid x^2 \equiv b \pmod{p^e} \\}$ be the set of solutions for $x^2 \equiv b \pmod{p^e}$.
We will prove the following series of lemmas:

1. $\abs{S_1} \in \\{ 0, 2 \\}$.
1. $\forall e \in \mathbb{N}$, define $F_e(x) = x \pmod{p^e}$ on $S_{e + 1}$. Then $F_e$ maps $S_{e + 1}$ into $S_e$.
1. $\forall e \in \mathbb{N}$, $S_e$ has no multiple of $p$.
1. $\forall e \in \mathbb{N}$, $F_e$ is injective.
1. $\forall e \in \mathbb{N}$, there exists an injection $G_e: S_{e} \rightarrow S_{e + 1}$.
1. $\forall e \in \mathbb{N}$, $\abs{S_e} = \abs{S_{e + 1}}$.
1. $\forall e \in \mathbb{N}$, there exists $H_e: S_1 \rightarrow S_e$ such that $H_e(\alpha) \in S_{e}$ and $H_e(\alpha) \equiv \alpha \pmod{p}$ for each $\alpha \in S_1$.

# Lemma 1: $\abs{S_1} \in \\{ 0,2 \\}$

If it has no solution, we are done.
Suppose it has a solution $0 < \alpha < p$.
Then it is obvious that $p - \alpha$ is a solution also.
Thus if there is at least one solution, there are at least two solutions.
Let $0 < \alpha, \alpha' < p$ be solutions to $x^2 \equiv b \pmod{p}$.
Then $\alpha^2 - \alpha'^2 \equiv 0 \pmod{p}$, so $p \mid \alpha + \alpha'$ or $p \mid \alpha - \alpha'$.
Since $0 < \alpha, \alpha' < p$, $2 \leq \alpha + \alpha' < 2p$ and $-p < \alpha - \alpha' < p$.
Therefore, $\alpha + \alpha' = p$ or $\alpha - \alpha' = 0$.
Hence, $\alpha' = \alpha$ or $\alpha' = p - \alpha$.

This implies that if there is a solution, there are exactly two solutions.

# Lemma 2: $F_e$ maps $S_{e + 1}$ to $S_e$.

Let $\gamma \in S_{e + 1}$.
Since $\gamma^2 \equiv b \pmod{p^{e + 1}}$, $\gamma^2 = kp^{e + 1} + b$ for some $k$.
Therefore, $\gamma^2 \equiv b \pmod{p^e}$.
Hence, $F_e(\gamma) \in S_{e}$.

# Lemma 3: $S_e$ has no multiple of $p$.
We will prove this by induction.
It is clear that $S_1$ has no multiple of $p$.
Suppose that $S_e$ has no multiple of $p$ for some $e \in \mathbb{N}$.
Suppose that $S_{e + 1}$ has a multiple of $p$.
Let $\alpha = ap^e + F_e(\alpha)$ for some $a$ be such an element.
However, since $\alpha$ is a multiple of $p$, $F_e(\alpha)$ must be a multiple of $p$.
By Lemma 2, this would imply that $S_e$ would have a multiple of $p$.
Contradiction.

# Lemma 4: $F_e: S_{e + 1} \rightarrow S_e$ is injective.
Let $\gamma, \gamma' \in S_{e + 1}$ such that $F(\gamma) = F(\gamma')$.

Let $\beta = F(\gamma) = F(\gamma') \in S_e$.
Then $\gamma = kp^e + \beta$ and $\gamma' = k'p^e + \beta$ for some $k, k'$.
Note that $k, k'$ must be integers in the range of $[0, p - 1]$ since $1 \leq \gamma \leq p^{e + 1} - 1$.
If $k = k'$, we are done.
We will consider the case that $k \ne k'$.

Since $\gamma, \gamma' \in S_{e + 1}$, $p^{e + 1} \mid (\gamma^2 - \gamma'^2)$.
Then $p^{e + 1} \mid ((kp^e + \beta)^2 - (k'p^e + \beta)^2)$, and thus $p^{e + 1} \mid [(k^2 - k'^2)p^{2e} + 2p^e\beta(k - k')]$.
$p^{2e}$ is divisible by $p^{e + 1}$, so $p^{e + 1} \mid 2p^e \beta (k - k')$.
Considering the range of $k, k'$, $k - k'$ cannot be divisible by $p$.
Thus, we can conclude that $p \mid \beta$.
However, by Lemma 3, we know that $\beta \in S_e$ cannot be a multiple of $p$.

# Lemma 5: There exists an injection $G_e: S_{e} \rightarrow S_{e + 1}$.
Let $e \in \mathbb{N}$ be given.
Let $\beta \in S_e$.
Let $\alpha = (F_1 \circ \cdots \circ F_{e - 1})(\beta)$.
By Lemma 2, $\alpha \in S_1$, so $\alpha^2 \equiv b \pmod p$.

Let $m = \frac{\beta^2 - b}{p^e}$ and $n = \frac{\beta - \alpha}{p}$.
Note that $m, n$ are both integers as $\beta^2 \equiv b \pmod{p^e}$ and $\beta \equiv \alpha \pmod{p}$.

Let $\gamma = (lp^e + \beta) \pmod{p^e}$ with $l = \frac{-m}{2\alpha} \pmod{p^e}$.
We don't mean integer division here.
This means that we will take the inverse of $2\alpha \pmod{p^e}$ and multiply it by $-m$.
Since $\gcd(\alpha, p) = \gcd(\alpha, 2) = 1$, so the inverse exists.
Technicall, it suffices to take the inverse $\pmod p$, but for simplicity, we will take the inverse $\pmod{p^e}$.

$$
\begin{align}
    \gamma^2
        &\equiv (lp^e + \beta)^2 \\
        &\equiv l^2p^{2e} + 2lp^e\beta + \beta^2 \\
        &\equiv 2lp^e\beta + \beta^2 \\
        &\equiv 2lp^e(np + \alpha) + (p^em + b) \\
        &\equiv 2lnp^{e + 1} + 2\alpha lp^e + (p^em + b) \\
        &\equiv 2\alpha lp^e + (p^em + b) \\
        &\equiv (2\alpha l + m)p^e + b \\
        &\equiv (-m + m)p^e + b \\
        &\equiv b & \pmod {p^{e + 1}}.
\end{align}
$$

By setting $G_e(\beta) = \gamma$, we proved the existence of a function $G_e: S_e \rightarrow S_{e + 1}$.

Notice that $F_e \circ G_e$ is the identify map on $S_e$.
Thus $G_e$ is injective.

# Lemma 6: $\abs{S_e} = \abs{S_{e + 1}}$.
Let $e \in \mathbb{N}$ be given.
By Lemma 4, $\abs{S_{e + 1}} \leq \abs{S_{e}}$.
By Lemma 5, $\abs{S_{e}} \leq \abs{S_{e + 1}}$.
Therefore, $\abs{S_{e}} = \abs{S_{e + 1}}$.

# Lemma 7: There exists $H_e: S_1 \rightarrow S_e$ such that $H_e(\alpha) \in S_{e}$ and $H_e(\alpha) \equiv \alpha \pmod{p}$ for each $\alpha \in S_1$.

Let $H_e = G_{e - 1} \circ G_{e - 2} \circ \cdots G_2 \circ G_1$.
By Lemma 5, $H_e(\alpha) \in S_e$.
Furthermore, $(F_1 \circ F_2 \circ \cdots \circ F_{e - 2} \circ F_{e - 1}) \circ H_e$ is the identify function on $S_1$.
Since $F_1 \circ \cdots \circ F_{e - 1}: S_{e} \rightarrow S_1$ simply takes $\pmod p$, this proves that $H_e(\alpha) \equiv \alpha \pmod{p}$.