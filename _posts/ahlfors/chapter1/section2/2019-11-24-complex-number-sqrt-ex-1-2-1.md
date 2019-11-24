---
layout: post
title:  "Square roots of complex numbers"
date:   2019-11-24
author: Hidenori
---

# Proposition
Compute

1. $\sqrt{i}$,
1. $\sqrt{-i}$,
1. $\sqrt{1 + i}$,
1. $\sqrt{\frac{1 - i\sqrt{3}}{2}}$.

# Solution
## 1
Let $a + bi = \sqrt{i}$.
By squaring both sides, we obtain $a^2 = b^2$ and $2ab = 1$.
* If $a = b$, then $a = \pm 1/\sqrt{2}$.
* It is impossible that $a + b = 0$ because $2ab = 1 > 0$.

Therefore, $\sqrt{i} = \pm\frac{1 + i}{\sqrt{2}}$.

## 2
$\sqrt{-i} = \sqrt{-1}\sqrt{i} = i\sqrt{i}$.
Therefore, $\sqrt{i} = \pm\frac{-1 + i}{\sqrt{2}}$.

## 3
By the formula given on P.4 (Ahlfors),

$$
\begin{align*}
  \pm \Big(\sqrt{\frac{1 + \sqrt{2}{2}}{2}} + i\sqrt{\frac{-1 + \sqrt{2}}{2}}\Big).
\end{align*}
$$

## 4
Similarly,

$$
\begin{align*}
  \pm \Big(\sqrt{\frac{1/2 + \sqrt{1/4 + 3/4}}{2}} - i\sqrt{\frac{-1/2 + \sqrt{1/4 + 3/4}}{2}}\Big)
  &= \pm \Big(\sqrt{3/4} - i\sqrt{1/4}\Big) \\
  &= \pm \frac{\sqrt{3} - i}{2}.
\end{align*}
$$
