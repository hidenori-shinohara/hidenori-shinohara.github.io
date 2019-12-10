---
layout: post
title:  "If $M / N_1$ and $M / N_2$ are Noetherian, so is $M / (N_1 \\cap N_2)$(WIP)"
date:   2019-12-10
author: Hidenori
---

# Proposition
Let $M$ be an $A$-module and let $N_1, N_2$ be submodules of $M$.
If $M / N_1$ and $M / N_2$ are Noetherian, so is $M / (N_1 \cap N_2)$.
Similarly with Artinian in place of Noetherian.

# Solution
If a module is finitely generated, then every submodule is finitely generated.
On the other hand, if every submodule is finitely generated, the module must be finitely generated since the module is a submodule of itself.
Therefore, by Proposition 6.2[Atiyah], an $A$-module is Noetherian if and only if it is finitely generated.

By Proposition 2.1, $N_2 / (N_1 \cap N_2) \cong (N_1 + N_2) / N_1$.
$(N_1 + N_2) / N_1$ is a submodule of $M / N_1$, which is Noetherian, so $(N_1 + N_2) / N_1$ is Noetherian.
This implies that $N_2 / (N_1 \cap N_2)$ is Noetherian.

We will consider the following exact sequence:

$$
\begin{align*}
  0 \rightarrow N_2 / (N_1 \cap N_2) \rightarrow M / (N_1 \cap N_2) \rightarrow (M / (N_1 \cap N_2)) / (N_2 / (N_1 \cap N_2)) \rightarrow 0.
\end{align*}
$$

By Proposition 2.1, $(M / (N_1 \cap N_2)) / (N_2 / (N_1 \cap N_2)) \cong M / N_2$, which is Noetherian.
By Proposition 6.3(i), $M / (N_1 \cap N_2)$ is Noetherian.

TODO: Prove the case with Artinian.
