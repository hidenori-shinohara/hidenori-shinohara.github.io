---
layout: post
title:  "The set of all prime ideals of a nonzero ring contains a minimal element"
date:   2019-11-24
author: Hidenori
---

# Proposition
Let $A$ be a ring $\ne 0$.
Show that the set of prime ideals of $A$ has minimal elements with respect of inclusion.

# Solution
Let $\Spec(A)$ denote the set of all prime ideals of $A$.
By Theorem 1.3 on P.3 of Atiyah, $A$ contains at least one maximal ideal and a maximal ideal is prime, so $\Spec(A)$ is not empty.
By Zorn's lemma, it suffices to show that any chain $(P_{\alpha})$ has a lower bound.
Let $(P_{\alpha})$ be a chain in $\Spec(A)$.
Let $P = \cap P_{\alpha}$.

* $0 \in P$, so $P$ is nonempty.
* If $a, b \in P$, then $\forall \alpha, a - b \in P_{\alpha}$.
  Therefore, $a - b \in P$.
* For all $a \in P$ and $x \in A$, $ax \in P_{\alpha}$ for all $\alpha$, so $ax \in P$.

Therefore, $P$ is an ideal.
Let $ab \in P$ for some $a, b \in A$.
Suppose $a \notin P$.
There must exist $\alpha_0$ such that $a \notin P_{\alpha_0}$.
Then $b \in P_{\alpha_0}$ because $P_{\alpha_0}$ is prime.

We claim that $b \in P_{\alpha}$ for all $\alpha$.
Let $\alpha$ be given.

* If $P_{\alpha} \subset P_{\alpha_0}$, then $a \notin P_{\alpha}$.
  Therefore, $b \in P_{\alpha}$.
* If $P_{\alpha_0} \subset P_{\alpha}$, then $b \in P_{\alpha_0} \subset P_{\alpha}$.

Thus $b \in P$, so $P$ is a prime ideal.
