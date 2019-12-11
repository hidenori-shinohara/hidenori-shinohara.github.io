---
layout: post
title:  "If $M / N_1$ and $M / N_2$ are Noetherian, so is $M / (N_1 \\cap N_2)$"
date:   2019-12-10
author: Hidenori
---

# Proposition
Let $M$ be an $A$-module and let $N_1, N_2$ be submodules of $M$.
If $M / N_1$ and $M / N_2$ are Noetherian, so is $M / (N_1 \cap N_2)$.
Similarly with Artinian in place of Noetherian.

# Solution

We have two exact sequences induced by the canonical inclusion and quotient maps.

* $0 \rightarrow (N_1 + N_2) / N_1 \rightarrow M / N_1 \rightarrow (M / N_1) / ((N_1 + N_2) / N_1) \rightarrow 0$,
* $0 \rightarrow N_2 / (N_1 \cap N_2) \rightarrow M / (N_1 \cap N_2) \rightarrow (M / (N_1 \cap N_2)) / (N_2 / (N_1 \cap N_2)) \rightarrow 0$.

Suppose that $M / N_1$ and $M / N_2$ are Noetherian (resp. Artinian).
By applying Proposition 6.3[Atiyah] to the first exact sequence, $(N_1 + N_2) / N_1$ must be Noetherian (resp. Artinian).

By [the second module isomorphism](https://en.wikipedia.org/wiki/Isomorphism_theorems#Second_isomorphism_theorem_3), $(N_1 + N_2) / N_1 \cong N_2 / (N_1 \cap N_2)$.
Therefore, $N_2 / (N_1 \cap N_2)$ is Noetherian (resp. Artinian).

By [the third module isomorphism theorem](https://en.wikipedia.org/wiki/Isomorphism_theorems#Third_isomorphism_theorem_3), $(M / (N_1 \cap N_2)) / (N_2 / (N_1 \cap N_2)) \cong M / N_2$,
Thus $(M / (N_1 \cap N_2)) / (N_2 / (N_1 \cap N_2))$ is Noetherian (resp. Artinian).

We have shown that $N_2 / (N_1 \cap N_2)$ and $(M / (N_1 \cap N_2)) / (N_2 / (N_1 \cap N_2))$ are both Noetherian (resp. Artinian).
By applying Proposition 6.3[Atiyah] to the second exact sequence, $M / (N_1 \cap N_2)$ is Noetherian (resp. Artinian).
