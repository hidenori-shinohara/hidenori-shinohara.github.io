---
layout: post
title:  "Quotient of radical ideals"
date:   2019-11-07
author: Hidenori
---

# Proposition
Let $I$ and $J$ be ideals in $k[x_1, \cdots, x_n]$.
Show that if $I$ is radical, then $I:J$ is radical and $I:J = I:\sqrt{J} = I:J^{\infty}$.

# Solution
Let $f \in k[x_1, \cdots, x_n]$ and suppose $f^m \in I:J$ for some $m \geq 1$.
Then $\forall g \in J, f^mg \in I$.
Since $I$ is an ideal, this implies $\forall g \in J, (fg)^m = (f^mg)g^{m - 1} \in I$.
Since $I$ is radical, $\forall g \in J, fg \in I$.
In other words, $f \in I:J$, so $I:J$ is radical.

Since $J \subset \sqrt{J}$, $I:\sqrt{J} \subset I:J$.
Let $f \in I:J$ and $g \in \sqrt{J}$.
Let $m \geq 1$ be given such that $g^m \in J$.
Then $fg^m \in I$.
Since $I$ is an ideal, $(fg)^m = f^{m - 1}(fg^m) \in I$.
Since $I$ is radical, $fg \in I$.
Therefore, $f\sqrt{J} \subset I$, so $I:J \subset I:\sqrt{J}$.

Clearly, $I:J \subset I:J^{\infty}$.
Let $f \in I:J^{\infty}$.
Let $g \in J$ and let $n \geq 1$ such that $fg^n \in I$.
Since $I$ is an ideal, $(fg)^n = f^{n - 1}(fg^n) \in I$.
Since $I$ is radical, $fg \in I$.
Thus $f \in I:J$, so $I:J^{\infty} \subset I:J$.
