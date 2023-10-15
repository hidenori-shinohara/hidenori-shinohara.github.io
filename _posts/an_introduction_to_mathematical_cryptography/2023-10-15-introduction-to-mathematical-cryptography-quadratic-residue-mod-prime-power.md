---
layout: post
title:  "An Introduction to Mathematical Cryptography: Quadratic Residue Mod Prime Powers"
date:   2023-10-15
author: Hidenori
---

Exercise 1.35 in _An Introduction to Mathematical Cryptography_.
Let $p$ be an odd prime and let $b$ be chosen such that $x^2 \equiv b \pmod p$ has a solution $\alpha$.

For every positive integer $e$, let $P(e)$ be the statement there exists a $\beta$ such that

- $\beta^2 \equiv b \pmod{p^e}$, and
- $\alpha \equiv \beta \pmod p$.

$P(1)$ is obviously true.
We assume that $P(e)$ is true for some $e \in \mathbb{N}$ and we will prove that $P(e + 1)$ is true.

Let $\beta$ be given such that $\beta^2 \equiv b \pmod{p^e}$ and $\alpha \equiv \beta \pmod p$.
This means that $\beta^2 = mp^e + b$ and $\beta = np + \alpha$ for some $m, n \in \mathbb{Z}$.

Let $\gamma = lp^e + \beta$ where $l = \frac{-m}{2\alpha}$.
Note that $\gcd(\alpha, p) = \gcd(2, p) = 1$, so the inverse of $2\alpha$ exists.

$$
\begin{align*}
    \gamma^2
        &= l^2p^{2e} + 2l\beta p^e + \beta^2 \\
        &\equiv 2l\beta p^e + \beta^2 \\
        &\equiv 2l(np + \alpha)p^e + mp^e + b \\
        &\equiv 2l\alpha p^e + mp^e + b \\
        &\equiv (2l\alpha + m)p^e + b \\
        &\equiv (-m + m)p^e + b \\
        &\equiv b & \pmod{p^{e + 1}}.
\end{align*}
$$

Furthermore, $\gamma \equiv \beta \equiv \alpha \pmod p$.
Therefore, $P(e + 1)$ is true, and by mathematical induction, the statement is true for any positive integer.
This proves Part (a) and (b).

We will quicky discuss how to come up with $\gamma = lp^e + \beta$.
The first realization is that $\gamma \equiv \beta \pmod{p^e}$.
Since $\gamma^2 \equiv b \pmod{p^{e + 1}}$, $\gamma^2 = kp^{e + 1} + b$.
Therefore, $\gamma^2 \equiv b \pmod{p^e}$.
Then $\gamma = lp^e + \beta$.
By solving $\gamma^2 = (lp^e + \beta)^2 \equiv b \pmod{p^{e + 1}}$ for $l$, we obtain the formula for $\gamma$.




TODO: Finish (c) and (d).


