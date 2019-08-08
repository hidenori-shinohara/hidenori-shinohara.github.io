---
layout: post
title:  "An alternative way to define an isomorphism for the fundamental group of a product space."
date:   2019-08-08
author: Hidenori
---

# Proposition
Show that the isomorphism $\pi_1(X \times Y) \approx \pi_1(X) \times \pi_1(Y)$ in [this proof]({{ site.baseurl }}{% post_url /algebraic_topology/chapter1/section1/2019-08-04-fundamental-group-product-space-1-12 %}) is given by $$[f] \mapsto (p_{1*}([f]), p_{2*}([f]))$$ where $p_1$ and $p_2$ are the projections of $X \times Y$ onto its two factors.

# Solution
In the proof, we defined  $\phi: \pi_1(X \times Y, (x_0, y_0)) \rightarrow \pi_1(X, x_0) \times \pi_1(Y, y_0)$ such that $\phi([(g, h)]) = [g] \times [h]$ for all $[(g, h)] \in \pi_1(X \times Y)$.

$$
\begin{align*}
  (p_{1*}([(g, h)]), p_{2*}([(g, h)]))
    &= ([p_1(g, h)], [p_2(g, h)]) \\
    &= ([g], [h]) \\
    &= [g] \times [h] = \phi([(g, h)]).
\end{align*}
$$

