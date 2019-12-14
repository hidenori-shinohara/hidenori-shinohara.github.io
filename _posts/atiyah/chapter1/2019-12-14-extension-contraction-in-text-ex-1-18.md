---
layout: post
title:  "Properties of contraction and extension"
date:   2019-12-14
author: Hidenori
---

# Proposition
If $a_1, a_2$ are ideals of $A$ and if $b_1, b_2$ are ideals of $B$, then

1. $(a_1 + a_2)^e = a_1^e + a_2^e, (b_1 + b_2)^c \supset b_1^c + b_2^c$.
1. TODO

# Solution
## 1

Let $\sum_{i=1}^{n} y_if(x_{i, 1} + x_{i, 2}) \in (a_1 + a_2)^e$ where $y_i \in B$ and $x_{i, 1} \in a_1, x_{i, 2} \in a_2$.

$$
\begin{align*}
  \sum_{i=1}^{n} y_if(x_{i, 1} + x_{i, 2}) 
    &= \sum_{i=1}^{n} y_i(f(x_{i, 1}) + f(x_{i, 2}) ) \\
    &= \sum_{i=1}^{n} y_if(x_{i, 1}) + \sum_{i=1}^{n} y_if(x_{i, 2}) \\
    &\in a_1^e + a_2^e.
\end{align*}
$$

Therefore, $(a_1 + a_2)^e \subset a_1^e + a_2^e$.

On the other hand, let $\sum_{i=1}^{n} y_{i, 1} f(x_{i, 1}) \in a_1^e$ and $\sum_{i=1}^{m} y_{i, 2} f(x_{i, 2}) \in a_2^e$.
Then $\sum_{i=1}^{n} y_{i, 1} f(x_{i, 1}) + \sum_{i=1}^{m} y_{i, 2} f(x_{i, 2}) = \sum_{i=1}^{n + m} y_i f(x_i)$ where

$$
\begin{align*}
  y_i &= \begin{cases}
    y_{i, 1} & (i \leq n) \\
    y_{i - n, 2} & (i \geq n + 1)
  \end{cases} \\
  x_i &= \begin{cases}
    x_{i, 1} & (i \leq n) \\
    x_{i - n, 2} & (i \geq n + 1).
  \end{cases}
\end{align*}
$$

Then each $y_i$ is in $B$ and each $x_i$ is in $a_1 + a_2$.
Thus $\sum_{i=1}^{n + m} y_i f(x_i) \in (a_1 + a_2)^e$.

TODO(Finish the contraction part)

## 2
TODO
