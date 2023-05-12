---
layout: post
title:  "Solutions to $y'' - y = 0$"
date:   2023-05-12
author: Hidenori
---

Exercise from P.34 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

> Let $V$ be the set of functions $f: \mathbb{R} \rightarrow \mathbb{R}$ which satisfy the differential equation $f'' - f = 0$. Show that $V$ is a vector space over $\mathbb{R}$ and, assuming its dimension is 2, find a basis for $V$.

It's easy to see $e^x$ and $e^{-x}$ are solutions to $f'' - f = 0$.
$ae^x + be^{-x} = 0$ implies $a = b = 0$ by letting $x \rightarrow \infty$ and $x \rightarrow -\infty$.
It's easy to see that any linear combination of $e^x$ and $e^{-x}$ is a solution to the equation, so $\\{ e^x, e^{-x} \\}$ forms a basis for $V$.

