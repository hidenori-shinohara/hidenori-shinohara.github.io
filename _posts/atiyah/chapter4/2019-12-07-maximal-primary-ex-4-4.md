---
layout: post
title:  "Maximal and primary ideals"
date:   2019-12-07
author: Hidenori
---

# Proposition
In the polynomial ring $\mathbb{Z}[t]$, the ideal $m = (2, t)$ is a maximal and the ideal $q = (4, t)$ is $m$-primary, but is not a power of $m$.

# Solution

$\mathbb{Z}[t] / (2, t) = \mathbb{Z}/(2)$, which is a field.
Therefore, $m$ is a maximal ideal.

$\mathbb{Z}[t] / q = \\{ 0 + q, 1 + q, 2 + q, 3 + q \\}$.
$(3 + q)^2 = 1 + q$, so $3 + q$ is a unit.
$1 + q$ is clearly a unit and $2 + q$ is nilpotent because $(2 + q)^2 = 0$.
Since $\mathbb{Z}[t] / q \ne 0$ and every zero divisor in $\mathbb{Z}[t] / q$ is nilpotent, $q$ is a primary ideal.

Moreover,

$$
\begin{align*}
  r(4, t)
    &= r((4) + (t)) \\
    &= r(r(4) + r(t)) & \text{(Exercise 1.13(v)[Atiyah])} \\
    &= r((2) + (t)) \\
    &= r(2, t) \\
    &= (2, t).
\end{align*}
$$

Therefore, $q$ is $m$-primary.

$q \ne m$ because $2 \notin q$.
This can be shown rigorously by considering the ring homomorphism $\phi: \mathbb{Z}[t] \rightarrow \mathbb{Z}$ that sends $t$ to $4$.
Then for every element $4a + tb$ in $q$, $\phi(4a + tb) = 4\phi(a) + 4\phi(b) = 4(\phi(a) + \phi(b))$ while $2 \in m$ gets mapped to 2.

$q \ne m^2 = (4, 2t, t^2)$ because $t \notin m^2$.
This can be shown by considering the ring homomorphism $t \mapsto 2$ because every element in $m^2$ gets mapped to a multiple of 4.

Finally, $m^n \subset m^2$ for all $n \geq 2$ by simple induction.
This implies $t \notin m^n$ for any $n \geq 2$, so $m^n \ne q$ for any $n \in \mathbb{N}$.
Therefore, $q$ is not a power of $m$.
