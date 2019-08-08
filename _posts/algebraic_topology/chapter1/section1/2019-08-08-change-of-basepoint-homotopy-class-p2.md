---
layout: post
title:  "Change-of-basepoint homomorphism $\\beta_h$ depends only on the homotopy class of $h$"
date:   2019-08-08
author: Hidenori
---

# Proposition
Show that the change-of-basepoint homomorphism $\beta_h$ depends only on the homotopy class of $h$.

# Solution

Let $h \simeq g$.
By [the inverse lemma](inverse), $\overline{h} \simeq \overline{g}$.
The product operation respects homotopy classes, $h \cdot f \cdot \overline{h} \simeq g \cdot f \cdot \overline{g}$.
Thus $[h \cdot f \cdot \overline{h}] = [g \cdot f \cdot \overline{g}]$, so $\beta_h(f) = \beta_g(f)$.
