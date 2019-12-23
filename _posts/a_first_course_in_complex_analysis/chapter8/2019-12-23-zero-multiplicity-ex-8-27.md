---
layout: post
title:  "Zero of multiplicity 1"
date:   2019-12-23
author: Hidenori
---

# Proposition
Suppose that $f$ is holomorphic at $z_0$, $f(z_0) = 0$, and $f'(z_0) \ne 0$.
Show that $f$ has a zero of multiplicity 1 at $z_0$.

# Solution
By Theorem 8.14[A first course in complex analysis], $f$ is either identically 0 on some open disk around $z_0$ or $f(z) = (z - a)^mg(z)$ for some $m$ and holomorphic $g$.
If $f$ is identically 0, then $f'(z_0) = 0$, so this is not the case.

If $m \geq 2$, then $f'(z_0) = (z_0 - z_0)^{m - 1}g(z_0) + (z_0 - z_0)^{m}g(z_0) = 0$, so this is a contradiction.
Therefore, $f(z) = (z - a)g(z)$ with $g(z_0) \ne 0$, so $f$ has a zero of multiplicity 1 at $z_0$.
