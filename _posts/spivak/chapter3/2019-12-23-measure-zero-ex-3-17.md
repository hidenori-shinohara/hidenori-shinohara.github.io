---
layout: post
title:  "Measure 0 and integration"
date:   2019-12-23
author: Hidenori
---

# Proposition
If $C$ is a bounded set of measure 0 and $\int_A \chi_C$ exists, show that $\int_A \chi_C = 0$.

# Solution
Let $P$ be a partition.
Suppose $L(f, P) \ne 0$.
Since $\chi_C(x)$ is either 0 or 1 for any $x \in A$, $m_S$ is 0 or 1 for any subrectangle $S \in P$.
If $m_S = 0$ for all subrectangles, $L(f, P) = 0$.
Thus there must exist a subrectangle $S_0 \in P$ such that $m_{S_0} = 1$.
In other words, $\forall x \in S_0, \chi_C(x) = 1$, so $S_0 \subset C$.

[As shown here](/2019/12/23/content-zero-ex-3-8.html), $S_0$ does not have content 0.
Since $S_0$ is compact and does not have content 0, it does not have measure 0 by Theorem 3-6.
Then $C$, which contains $S_0$, does not have measure 0.
This is a contradiction, so $L(f, P) = 0$.

We showed that $L(f, P) = 0$ for all partitions.
Thus $\sup\\{ L(f, P) \\} = 0$.
We know that $\int_A \chi_C$ exists, and it must be equal to $\sup\\{ L(f, P) \\}$.
Therefore, $\int_A \chi_C = 0$.
