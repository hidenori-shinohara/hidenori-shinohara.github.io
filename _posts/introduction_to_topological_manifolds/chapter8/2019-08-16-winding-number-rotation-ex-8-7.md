---
layout: post
title:  "Rotation does not affect the winding number of $f$"
date:   2019-08-16
author: Hidenori
---

# Proposition
A rotation of $S^1$ is a map $\rho: S^1 \rightarrow S^1$ of the form $\rho(z) = e^{i\theta}z$ for some fixed $e^{i\theta} \in S^1$.
Show that if $\rho$ is a rotation, then $N(\rho \circ f) = N(f)$ for every loop $f$ in $S^1$.

# Solution
Let $\rho(z) = e^{i\theta_0}z$ be a rotation in the format specified in the Proposition.
Let $f$ be a loop in $S^1$.
Let $\tilde{f}$ be any lift of $f$.

Then $N(f) = \tilde{f}(1) - \tilde{f}(0)$.

Let $g: S^1 \rightarrow S^1$ be defined such that 

$$
\begin{align*}
  g(e^{i\theta}) = \frac{\theta_0}{2\pi} + \tilde{f}(e^{i\theta}).
\end{align*}
$$

Then 

$$
\begin{align*}
  \epsilon(g(e^{i\theta}))
    &= \epsilon(\frac{\theta_0}{2\pi} + \tilde{f}(e^{i\theta})) \\
    &= \exp(2\pi i(\frac{\theta_0}{2\pi} + \tilde{f}(e^{i\theta}))) \\
    &= \exp(\theta_0 i + 2\pi_i\tilde{f}(e^{i\theta})) \\
    &= \exp(\theta_0 i)\exp(2\pi_i\tilde{f}(e^{i\theta})) \\
    &= \exp(\theta_0 i)\epsilon(\tilde{f}(e^{i\theta})) \\
    &= \rho(\epsilon(\tilde{f}(e^{i\theta}))) \\
    &= \rho(f(e^{i\theta})) \\
    &= (\rho \circ f)(e^{i\theta}).
\end{align*}
$$

Therefore, $g$ is a lift of $\rho \circ f$.
Then 

$$
\begin{align*}
  N(\rho \circ f)
    &= g(1) - g(0) \\
    &= (\frac{\theta_0}{2\pi} + \tilde{f}(1)) - (\frac{\theta_0}{2\pi} + \tilde{f}(0)) \\
    &= \tilde{f}(1) - \tilde{f}(0) \\
    &= N(f).
\end{align*}
$$

Therefore, $N(\rho \circ f) = N(f)$ for every loop in $S^1$.
