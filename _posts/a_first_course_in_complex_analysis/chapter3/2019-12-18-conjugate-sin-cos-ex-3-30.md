---
layout: post
title:  "$\\overline{\\sin(z)} = \\sin(\\overline{z})$ and $\\overline{\\cos(z)} = \\cos(\\overline{z})$"
date:   2019-12-18
author: Hidenori
---

# Proposition
Prove that $\overline{\sin(z)} = \sin(\overline{z})$ and $\overline{\cos(z)} = \cos(\overline{z})$"

# Solution
$$
\begin{align*}
  \overline{\exp(z)}
    &= \overline{\exp(x + iy)} \\
    &= \overline{\exp(x)\exp(iy)} \\
    &= \overline{\exp(x)(\cos(y) + i\sin(y))} \\
    &= \overline{\exp(x)\cos(y) + i\exp(x)\sin(y))} \\
    &= \exp(x)\cos(y) - i\exp(x)\sin(y) \\
    &= \exp(x)(\cos(y) - i\sin(y)) \\
    &= \exp(x)\exp(-iy) \\
    &= \exp(x-iy) \\
    &= \exp(\overline{z}).
\end{align*}
$$

for any $z \in \mathbb{C}$.

Therefore,

$$
\begin{align*}
  \overline{\sin(z)}
    &= \overline{\Big(\frac{\exp(iz) - \exp(-iz)}{2i}\Big)} \\ 
    &= \frac{\overline{\exp(iz)} - \overline{\exp(-iz)}}{-2i} \\ 
    &= \frac{\exp(-i\overline{z}) - \exp(i\overline{z})}{-2i} \\ 
    &= \frac{\exp(i\overline{z}) - \exp(-i\overline{z})}{2i} \\ 
    &= \sin(\overline{z}).
\end{align*}
$$

Similarly,

$$
\begin{align*}
  \overline{\cos(z)}
    &= \overline{\Big(\frac{\exp(iz) + \exp(-iz)}{2}\Big)} \\ 
    &= \frac{\overline{\exp(iz)} + \overline{\exp(-iz)}}{2} \\ 
    &= \frac{\exp(-i\overline{z}) + \exp(i\overline{z})}{2} \\ 
    &= \frac{\exp(i\overline{z}) + \exp(-i\overline{z})}{2} \\ 
    &= \cos(\overline{z}).
\end{align*}
$$
