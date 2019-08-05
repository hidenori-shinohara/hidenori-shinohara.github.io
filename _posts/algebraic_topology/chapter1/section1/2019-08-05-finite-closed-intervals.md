---
layout: post
title:  "Given an open cover of $I$, find finitely many closed intervals each of which is contained in an open set"
date:   2019-08-05
author: Hidenori
---

# Proposition
Let $K = \\{ U_{\alpha} \\}$ be an open cover of $I$.
Then there exist $0 = s_0 < s_1 < \cdots < s_m = 1$ such that for each $i = 0, \cdots, m - 1$, there exists an $\alpha$ such that $[s_i, s_{i + 1}] \subset A_{\alpha}$.

# Solution

Choose $U_{\alpha_0} \in K$ such that $0 \in U_{\alpha}$.
Since $U_{\alpha_0}$ is open in $I$, there exists an $r_0 \in (0, 1)$ such that $[0, r_0) \subset U_{\alpha_0}$.

Choose $U_{\alpha_1} \in K$ such that $1 \in U_{\alpha}$.
Since $U_{\alpha_1}$ is open in $I$, there exists an $r_1 \in (0, 1)$ such that $(r_1, 1] \subset U_{\alpha_1}$.

For each $c \in (0, 1)$, there exists an $\alpha_c$ such that $c \in U_{\alpha_c}$.
Then there exists an $r_c$ such that $c \in (c - r_c, c + r_c) \subset U_{\alpha_c}$.

Then $K' = \\{ [0, r_0), (r_1, 1] \\} \cup \\{ (c - r_c, c + r_c) \mid c \in (0, 1) \\}$ is an open cover of $I$ where each interval is completely contained in an open set in $K$.

Since $I$ is compact, there exists a finite subcover of $K'$.
Let $\\{ [0, r_0), (r_1, 1], (a_1, b_1), \cdots, (a_n, b_n) \\}$ denote the finite subcover.
This makes sense because:

* Since $[0, r_0)$ is the only interval in $K'$ containing $0$, the subcover must contain $[0, r_0)$.
* Similarly, $(r_1, 1]$ must be in the subcover.

We will construct $s_i$'s inductively.

Since $r_0 \notin [0, r_0)$ and $r_0 \in (0, 1)$, there must exist $(a_i, b_i)$ containing $r_0$.
Without loss of generality, assume that $r_0 \in (a_1, b_1)$.
Let $s_1 = (a_1 + r_0) / 2$.
Then $0 < s_1$ and $[s_0, s_1] \subset [0, r_0) \subset U_{\alpha_0}$.

There must exist an interval containing $b_1$.
Without loss of generality, assume that $b_1 \in (a_2, b_2)$.
Let $s_2 = (a_2 + b_1) / 2$.
Then $s_1 < s_2$ and $[s_1, s_2] \subset (a_2, b_2) \subset U_{\alpha}$ for some $\alpha$.

Repeat this process until the only interval containing $b_i$ is $(r_1, 1]$.
Then let $s_{i + 1} = (b_i + r_1) / 2$, and let $s_{i + 2} = 1$.

Then such $s_i$'s are a desired sequence.
