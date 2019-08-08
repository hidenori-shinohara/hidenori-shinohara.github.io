---
layout: post
title:  "Cancellation property of the composition of paths"
date:   2019-08-08
author: Hidenori
---


# Problem Statement
Show that composition of paths satisfies the following cancellation property:
If $f_0 \cdot g_0 \simeq f_1 \cdot g_1$ and $g_0 \simeq g_1$ then $f_0 \simeq f_1$.

# Solution

By [the inverse lemma](inverse), $\overline{g_0} \simeq \overline{g_1}$.

We know that $f_0 \cdot g_0 \simeq f_1 \cdot g_1$.
As mentioned on P.26, the product operation respects homotopy classes.

$$
\begin{align*}
  (f_0 \cdot g_0) \cdot \overline{g_0} \simeq (f_1 \cdot g_1) \cdot \overline{g_1}
    &\implies f_0 \cdot (g_0 \cdot \overline{g_0}) \simeq f_1 \cdot (g_1 \cdot \overline{g_1}) \\
    &\implies f_0 \cdot c \simeq f_1 \cdot c \\
    &\implies f_0 \simeq f_1 & \text{(By reparametrization)} \\
\end{align*}
$$
