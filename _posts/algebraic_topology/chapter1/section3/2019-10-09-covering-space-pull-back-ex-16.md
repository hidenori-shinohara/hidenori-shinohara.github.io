---
layout: post
title:  "If $q \\circ p$ and $q$ are covering maps and $Z$ is locally path connected, $p$ is a covering map"
date:   2019-10-09
author: Hidenori
---

# Problem
Given maps $X \rightarrow Y \rightarrow Z$ such that both $Y \rightarrow Z$ and the composition $X \rightarrow Z$ are covering spaces, show that $X \rightarrow Y$ is a covering space if $Z$ is locally path-connected, and show that this covering space is normal if $X \rightarrow Z$ is a normal covering space.

# Questions

* What is the hypothesis?
    * $X, Y, Z$ are topological spaces.
    * $Z$ is locally path-connected.
    * $p: X \rightarrow Y, q: Y \rightarrow Z$ are maps.
    * $q \circ p$ and $q$ are covering maps.
* What is the conclusion?
    * $p$ is a covering space.
* Separate the various parts of the hypothesis.
    * Covering maps are probably used to find a bunch of copies of $U$.
* Find the connection between the hypothesis and the conclusion.
    * The problem sorta makes sense because we are thinking of doing something like $p = q^{-1} \circ (q \circ p)$, which is a covering map.
      Of course, it's not that simple because $q$ may not be bijective, and even if that's true, the composition of two covering maps may not be a covering map.
* Look at the conclusion! And try to think of a familiar theorem having the same or a similar conclusion.
* Keep only a part of the hypothesis, drop the other part; is the conclusion still valid?
* Could you derive something useful from the hypothesis?
    * Since $Z$ is locally path connected, we can always pick a small path-connected neighborhood.
    * Let $y_0 \in Y$ be given.
      Pick $z_0 \in Z$ such that $p(z_0) = y_0$ and let $x_0 = p(y_0)$.
      Then $x_0 = (q \circ p)(z_0)$.
      Let $U$ be a path-connected neighborhood of $x_0$ that is evenly covered by $q \circ p$.
      Then $(q \circ p)^{-1}(U) = \coprod_{\beta} W_{\beta}$ where each $W_{\beta}$ is an open set such that $q \circ p$ maps each $W_{\beta}$ homeomorphically to $U$.
      Let $W_{\beta_0}$ be the one that contains $z_0$.
      Let $V = p(W_{\beta_0})$.
      Then $V$ is a neighborhood of $y_0$ that is evenly covered by $p$?
      How can I use the local path connectedness of $U$?
* Could you think of another hypothesis from which you could easily derive the conclusion?
* Could you change the hypothesis, or the conclusion, or both if necessary, so that the new hypothesis and the new conclusion are nearer to each other?
    * If $p$ is the identity map, this problem is trivial.
    * If $q$ is the identity map, this problem is trivial.
    * If $X, Y, Z$ are specific, this problem becomes easier.
      For instance, if $X = S^1 \vee S^1 \vee S^1 \vee S^1 \vee S^1, Y = S^1 \vee S^1 \vee S^1$ and $Z = S^1 \vee S^1$, we can simply show what $p$ is.
* Did you use the whole hypothesis?
    * I forgot to use that $Z$ is locally path-connected at first.
