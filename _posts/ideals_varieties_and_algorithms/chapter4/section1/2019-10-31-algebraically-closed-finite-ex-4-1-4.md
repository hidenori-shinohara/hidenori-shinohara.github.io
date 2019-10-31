---
layout: post
title:  "An algebraically closed field must be infinite"
date:   2019-10-31
author: Hidenori
---

# Proposition
Prove that an algebraically closed field $k$ must be infinite.

# Solution
Suppose $k = \\{ a_1, \cdots, a_n \\}$ is finite.
Then $f(x) = 1 + \prod_{i=1}^{n} (x - a_i)$ is a polynomial such that $f(a_i) = 1 \ne 0$ for each $i$.
Thus $f$ has no roots in $k$.
Therefore, $k$ is not algebraically closed.
