---
layout: post
title:  "Basic properties of radical ideals"
date:   2019-11-16
author: Hidenori
---

# Proposition
For an arbitrary field, show that $\sqrt{IJ} = \sqrt{I \cap J}$.
Give an example to show that the product of radical ideals need not be radical.
Also give an example to show that $\sqrt{IJ}$ can differ from $\sqrt{I}\sqrt{J}$.

# Solution
Since $IJ \subset I \cap J$, $\sqrt{IJ} \subset \sqrt{I \cap J}$.

Let $f \in \sqrt{I \cap J}$.
Then $f^m \in I \cap J$ for some $m \geq 1$.
This implies $f^m \in I$ and $f^m \in J$.
Therefore, $(f^m)(f^m) \in IJ$, so $f^{2m} \in IJ$.
Hence, $f \in \sqrt{IJ}$.

Let $I = J = \ev{x}$.
Then $IJ = \ev{x^2}$, and $IJ$ is clearly not radical.
Similarly, $\sqrt{IJ} = \ev{x} \ne \ev{x^2} = \sqrt{I}\sqrt{J}$.
