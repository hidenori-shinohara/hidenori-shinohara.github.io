---
layout: post
title:  "Inclusion reversing properties of ideals and varieties"
date:   2019-11-05
author: Hidenori
---

# Proposition
Prove that $I$ and $V$ are inclusion-reversing and $V(\sqrt{I}) = V(I)$ for any ideal $I$.

# Solution
Let $V_1 \subset V_2$.
Then $I(V_2) \subset I(V_1)$ because every polynomial that vanishes on $V_2$ must vanish on $V_1$.

Similarly, if $I_1 \subset I_2$, then $V(I_2) \subset V(I_1)$ because if every polynomial in $I_2$ vanishes at a certain pint, then so does every polynomial in $I_1$.

Since $I \subset \sqrt{I}$, $V(\sqrt{I}) \subset V(I)$.
Let $x \in V(\sqrt{I})$, and $f \in I$.
Then $f^m \in \sqrt{I}$ for some $m \geq 1$.

This implies that $f^m(x) = 0$, but this implies $f(x) = 0$ because $k$ is a field.
Therefore, $x \in V(I)$.
