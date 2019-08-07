---
layout: post
title:  "A homotopy equivalence induces an isomorphism."
date:   2019-08-07
author: Hidenori
---

# Proposition
If $\phi: X \rightarrow Y$ is a homotopy equivalence, then the induced homomorphism $$\phi_{*}: \pi_1(X, x_0) \rightarrow \pi_1(Y, \phi(x_0))$$ is an isomorphism for all $x_0 \in x$.

# Solution
Since $\phi: X \rightarrow Y$ is a homotopy equivalence, the following functions must exist:

* $\psi: Y \rightarrow X$, and $\psi$ is continuous.
* $\alpha_t: X \rightarrow X$.
    * The associated map $(x, t) \rightarrow \alpha_t(x)$ is continuous.
    * $\alpha_0 = \psi \circ \phi$.
    * $\alpha_1 = \mathbb{1}$.
* $\beta_t: Y \rightarrow Y$.
    * The associated map $(y, t) \rightarrow \beta_t(x)$ is continuous.
    * $\beta_0 = \phi \circ \psi$.
    * $\beta_1 = \mathbb{1}$.

Let $x_0 \in X$ be given.
We will show that $$\phi_*: \pi_1(X, x_0) \rightarrow \pi_1(Y, \phi(x_0))$$ is an isomorphism.

$$\phi_*$$ is [induced by a continuous map](https://en.wikipedia.org/wiki/Induced_homomorphism), so it is a homomorphism.
Similarly, $$\psi_*: \pi_1(Y, \phi(x_0)) \rightarrow \pi_1(X, \psi(\phi(x_0)))$$ is a homomorphism.

Consider $$\psi_* \circ \phi_*$$.
For any $[f] \in \pi_1(X, x_0)$, $$(\psi_* \circ \phi_*)([f]) = [(\psi \cdot \phi)(f)] = [\alpha_0(f)] = \alpha_{0*}([f])$$.
By [this lemma]({{ site.baseurl }}{% post_url /algebraic_topology/chapter1/section1/2019-08-06-homotopy-and-change-of-basepoint-1-19 %}), 
$$\alpha_{0*} = \beta_h \alpha_{1*}$$ where $h$ is the path such that $h(t) = \alpha_t(x_0)$.
Since $\alpha_{1}$ is the identity function on $X$, $\alpha_{1*}$ is the identity function on $\pi_1(X, x_0)$.
Therefore, $$\alpha_{0*} = \beta_h$$.
[We have proved that a change-of-basepoint map is an isomorphism.]({{ site.baseurl }}{% post_url /algebraic_topology/chapter1/section1/2019-08-07-change-of-basepoint-isomorphism-1-5 %}), so $$\alpha_{0*}$$ is an isomorphism.
Thus $$\psi_* \circ \phi_*$$ is an isomorphism.
This implies that $$\phi_*: \pi_1(X, x_0) \rightarrow \pi_1(Y, \phi(x_0))$$ is injective.

Using the same argument with $$\psi_*: \pi_1(Y, \phi(x_0)) \rightarrow \pi_1(X, \psi(\phi(x_0)))$$ and $$\phi_*: \pi_1(X, \psi(\phi(x_0))) \rightarrow \pi_1(Y, \phi(\psi(\phi(x_0))))$$,
$$\phi_* \circ \psi_*$$ is an isomorphism, so $$\psi_*: \pi_1(Y, \phi(x_0)) \rightarrow \pi_1(Y, \psi(\phi(x_0)))$$ is injective.

Lastly, we will show that $$\phi_*: \pi_1(X, x_0) \rightarrow \pi_1(Y, \phi(x_0))$$ is surjective.
Let $[f] \in \pi_1(Y, \phi(x_0))$.
Then $$\psi_*([f]) = [\psi \circ f] \in \pi_1(Y, \psi(\phi(x_0)))$$.
Since $$\psi_*  \circ \phi_*$$ is an isomorphism, there exists $$(\psi_* \circ \phi_*)^{-1}(\psi_*([f])) \in \pi_1(X, x_0)$$.
Thus $\pi_1(X, x_0)$ contains $$\phi_*^{-1}([f])$$, so $$\phi_*$$ is surjective.

Therefore, $$\phi_*$$ is an isomorphism.


