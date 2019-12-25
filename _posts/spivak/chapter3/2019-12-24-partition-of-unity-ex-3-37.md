---
layout: post
title:  "$\\int_{(0, 1)} f$ exists $\\iff \\lim_{\\epsilon \\rightarrow 0} \\int_{\\epsilon}^{1-\\epsilon} f$ exists(WIP)"
date:   2019-12-24
author: Hidenori
---

# Proposition
1. Suppose that $f: (0, 1) \rightarrow \mathbb{R}$ is a non-negative continuous function.
   Show that $\int_{(0, 1)} f$ exists if and only if $\lim_{\epsilon \rightarrow 0} \int_{\epsilon}^{1-\epsilon} f$ exists.
1. Let $A_n = [1 - 1 / 2^n, 1 - 1 / 2^{n + 1}]$.
   Suppose that $f: (0, 1) \rightarrow \mathbb{R}$ satisfies $\int_{A_n} f = (-1)^n / n$ and $f(x) = 0$ for $x \notin$ any $A_n$.
   Show that $\int_{(0, 1)} f$ does not exist, but $\lim_{\epsilon \rightarrow 0} \int_{(\epsilon, 1 - \epsilon)} f = \log 2$.

# Solution
## 1
Let $\mathcal{O} = \\{ (\frac{1}{10n}, 1 - \frac{1}{10n}) \mid n \in \mathbb{N} \\}$.
Let $\Phi$ be a partition of unity for $(0, 1)$ subordinate to the cover $\mathcal{O}$.
Without loss of generality, we assume that $\Phi = \\{ \phi_1, \phi_2, \cdots, \\}$ such that $\forall n \in \mathbb{N}$ $\phi_n = 0$ outside of some closed set contained in $(\frac{1}{10n}, 1 - \frac{1}{10n})$.

This is possible because for each $\phi$, we can associate $n_{\phi} \in \mathbb{N}$ such that $\phi = 0$ outside $(\frac{1}{10n_{\phi}}, 1 - \frac{1}{10n_{\phi}})$.
Then we can define $\phi_n$ to be the sum of $\phi$ whose $n_{\phi}$ equals $n$.
It is easy to see that $\\{ \phi_i \\}$ is indeed a partition of unity for $(0, 1)$ subordinate to $\mathcal{O}$.

Let $\epsilon \in (0, 1/2)$ be given.
$f$ is continuous and $[\epsilon, 1 - \epsilon]$ is compact.
Thus $f$ is bounded on $[\epsilon, 1 - \epsilon]$.
By Theorem 3-8[Spivak], $\int_{\epsilon}^{1-\epsilon} f$ exists.
Similarly, $\forall N \in \mathbb{N}$, $\int_{1/10N}^{1 - 1/10N} f$ exists.

We claim that $\int_{(0, 1)} f$ exists if and only if $\lim_{N \rightarrow \infty} (\int_{1/10N}^{1-1/10N} (\sum_{i=1}^{N} \phi_i) f)$ exists.
This is because:

* $\int_{(0, 1)} f$ exists
* $\iff \sum_{i \in \mathbb{N}} \int_{(0,1)} \phi_i f$ exists
* $\iff \sum_{i \in \mathbb{N}} \int_{1/10i}^{1-1/10i} \phi_i f$ exists because each $\phi_i = 0$ outside $(1/10i, 1-1/10i)$
* $\iff \lim_{N \rightarrow \infty} \sum_{i=1}^{N} \int_{1/10i}^{1-1/10i} \phi_i f$ exists
* $\iff \lim_{N \rightarrow \infty} \sum_{i=1}^{N} \int_{1/10N}^{1-1/10N} \phi_i f$ exists
* $\iff \lim_{N \rightarrow \infty} \int_{1/10N}^{1-1/10N} (\sum_{i=1}^{N} \phi_i) f$ exists.

Thus it suffices to show that $\lim_{N \rightarrow \infty} \int_{1/10N}^{1-1/10N} (\sum_{i=1}^{N} \phi_i) f$ exists if and only if $\lim_{\epsilon \rightarrow 0} \int_{\epsilon}^{1 - \epsilon} f$ exists.

Suppose $\lim_{\epsilon \rightarrow 0} \int^{1 - \epsilon}_{\epsilon} f$ exists.
For any $N \in \mathbb{N}$,

$$
\begin{align*}
  \int_{1/10N}^{1-1/10N} (\sum_{i=1}^{N} \phi_i) f
    &\leq \int_{1/10N}^{1-1/10N} f \\
    &\leq \lim_{\epsilon \rightarrow 0} \int_{\epsilon}^{1 - \epsilon} f.
\end{align*}
$$

Therefore, $\lim_{N \rightarrow \infty} \int_{1/10N}^{1-1/10N} (\sum_{i=1}^{N} \phi_i) f \leq \lim_{\epsilon \rightarrow 0} \int_{\epsilon}^{1 - \epsilon} f$.
Since $f$ is non-negative, $\lim_{N \rightarrow \infty} \int_{1/10N}^{1-1/10N} (\sum_{i=1}^{N} \phi_i) f$ exists because it is bounded.

Suppose $\lim_{N \rightarrow \infty} \int_{1/10N}^{1-1/10N} (\sum_{i=1}^{N} \phi_i) f$ exists.
Let $\epsilon \in (0, 1/2)$ be given.
Choose $N \in \mathbb{N}$ such that $\frac{1}{10N} < \epsilon$.

$$
\begin{align*}
  \int_{\epsilon}^{1 - \epsilon} f
    &= \int_{\epsilon}^{1 - \epsilon} (\sum_{i=1}^{N} \phi_i) f \\
    &\leq \int_{1/10N}^{1 - 1/10N} (\sum_{i=1}^{N} \phi_i) f \\
    &\leq \lim_{N \rightarrow \infty} \int_{1/10N}^{1 - 1/10N} (\sum_{i=1}^{N} \phi_i) f.
\end{align*}
$$

Thus $\int_{\epsilon}^{1 - \epsilon} f$ is bounded as $\epsilon \rightarrow \infty$ and $f$ is non-negative, so the limit exists.

## 2
TODO(Finish this!)
