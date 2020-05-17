---
layout: post
title:  "The intersection of two DSets is a DSet"
date:   2020-05-17
author: Hidenori
---

# Proposition
If $B_1$ and $B_2$ are DSets in an FBAS $\ev{V, Q}$ enjoying quorum intersection, then $B = B_1 \cap B_2$ is a DSet, too.

# Solution

If $B = V$, then we are done.
Suppose otherwise.

For any $v \in V$,

$$
\begin{align*}
  v \in V \setminus B
    &\iff v \in V \land v \notin B \\
    &\iff v \in V \land (v \notin B_1 \lor v \notin B_2) \\
    &\iff (v \in V \land v \notin B_1) \lor (v \in V \land v \notin B_2) \\
    &\iff (v \in (V \setminus B_1)) \lor (v \in (V \setminus B_2)) \\
    &\iff v \in ((V \setminus B_1) \cup (V \setminus B_2)).
\end{align*}
$$

By definition, $V \setminus B_1$ and $V \setminus B_2$ are both quorums in $\ev{V, Q}$.
[We have shown that the union of two quorums is a quorum](https://hidenori-shinohara.github.io/2020/05/16/quorums-basic-properties.html), so $V \setminus B$ is a quorum in $\ev{V, Q}$.

We must now show quorum intersection despite $B$.
Let $U_a, U_b$ be quorums in $\ev{V, Q}^B$.

* $U_a \setminus B_1$ is a quorum in $(\ev{V, Q}^B)^{B_1} = \ev{V, Q}^{B_1}$ [as shown before](https://hidenori-shinohara.github.io/2020/05/17/quorum-subset.html).
* Similarly, $U_b \setminus B_1$ is a quorum in $\ev{V, Q}^{B_1}$, and $U_a \setminus B_2$ and $U_b \setminus B_2$ are both quorums in $\ev{V, Q}^{B_2}$.

$$
\begin{align*}
  (U_a \setminus B_1) \cup (U_a \setminus B_2)
    &= U_a \setminus (B_1 \cap B_2) \\
    &= U_a \setminus B \\
    &= U_a
\end{align*}
$$

because $U_a$ is a quorum in $\ev{V, Q}^B$.
In other words, $(U_a \setminus B_1) \cup (U_a \setminus B_2) \ne \emptyset$.
Similarly, $(U_b \setminus B_1) \cup (U_b \setminus B_2) \ne \emptyset$.

Without loss of generality, assume that $U_a \setminus B_1 \ne \emptyset$.

* $V \setminus B_2$ is a quorum in $\ev{V, Q}$ because $B_2$ is a DSet.
  [As shown before](https://hidenori-shinohara.github.io/2020/05/17/quorum-subset.html), $(V \setminus B_2) \setminus B_1$ is a quorum in $\ev{V, Q}^{B_1}$.
* $U_a \setminus B_1$ is a quorum in $(\ev{V, Q}^B)^{B_1} = \ev{V, Q}^{B_1}$ for the same reason.

Because $B_1$ is a DSet in $\ev{V, Q}$, $\ev{V, Q}^{B_1}$ enjoys quorum intersection.
Therefore, $(U_a \setminus B_1) \cap ((V \setminus B_2) \setminus B_1) \ne \emptyset$.

$$
\begin{align*}
  (U_a \setminus B_1) \cap ((V \setminus B_2) \setminus B_1)
    &= (U_a \cap (V \setminus B_2)) \setminus B_1 \\
    &\subset U_a \cap (V \setminus B_2) \\
    &= (U_a \cap V) \setminus B_2 \\
    &= U_a \setminus B_2.
\end{align*}
$$

Thus, $U_a \setminus B_2 \ne \emptyset$.

Using the same argument, we can show that $U_b \setminus B_1 \ne \emptyset$ and $U_b \setminus B_2 \ne \emptyset$.

Since $U_a \setminus B_1$ and $U_b \setminus B_1$ are quorums in $\ev{V, Q}^{B_1}$ and $B_1$ is a DSet, $(U_a \setminus B_1) \cap (U_b \setminus B_1) \ne \emptyset$ by the definition of a DSet.
This implies $(U_a \cap U_b) \setminus B_1 \ne \emptyset$.
Therefore, $U_a \cap U_b \ne \emptyset$.
