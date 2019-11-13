---
layout: post
title:  "Verify that a diagram commutes"
date:   2019-11-13
author: Hidenori
---

# Proposition
Prove that the diagram (3) on P.134 (Ideals, Varieties, and Algorithms) commutes and $i(k^m) = V$.

# Solution
For any $(t_1, \cdots, t_m) \in k^m$,

$$
\begin{align*}
  (\pi_m \circ i)(t_1, \cdots, t_m)
    &= \pi_m(t_1, \cdots, t_m, f_1(t_1, \cdots, t_m), \cdots, f_n(t_1, \cdots, t_m)) \\
    &= (f_1(t_1, \cdots, t_m), \cdots, f_n(t_1, \cdots, t_m)) \\
    &= F(t_1, \cdots, t_m).
\end{align*}
$$

$i(k^m) \subset V$ because each $x_i - f_i$ vanishes at $(f_1(t_1, \cdots, t_m), \cdots, f_n(t_1, \cdots, t_m))$ for any $(t_1, \cdots, t_m) \in k^m$.
$V \subset i(k^m)$ because if $x_i - f_i$ vanishes at $(t_1, \cdots, t_{m + n})$, then $t_{m + i} = f_i(t_1, \cdots, t_m)$.
Therefore, $i(k^m) = V$.
