---
layout: post
title:  "A tangent line and its multiplicity"
date:   2019-11-21
author: Hidenori
---

# Proposition
Let $C$ be the curve in $k^2$ defined by $x^3 - xy + y^2 = 1$ and note that $(1, 1) \in C$.
Now consider the straight line parametrized by

$$
\begin{align*}
  x &= 1 + ct, \\
  y &= 1 + dt.
\end{align*}
$$

Compute the multiplicity of this line when it meets $C$ at $(1, 1)$.
What does this tell you about the tangent line?

# Solution
Substituting $x = 1 + ct$ and $y = 1 + dt$ gives $c^3t^3 + (d^2 - cd + 3c^2)t^2 + (d + 2c)t = 0$.

If $d + 2c \ne 0$, then the multiplicity of the root 0 is 0.
Suppose $d + 2c = 0$.
Then substituting $d = -2c$ gives us $c^3t^2 + 9c^2t = 0$.
If $c = 0$, then $d = -2c = 0$.
However, $c, d$ cannot be both zero.
Therefore, the multiplicity of the root 0 is 2 in this case.

Therefore, $x = 1 + t, y = 1 - 2t$ is the tangent line.
