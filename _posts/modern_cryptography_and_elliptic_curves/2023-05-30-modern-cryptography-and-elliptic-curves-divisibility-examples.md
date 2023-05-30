---
layout: post
title:  "Modern Cryptography and Elliptic Curves: Examples of Division"
date:   2023-05-30
author: Hidenori
---

Exercise from P.50 of _Modern Cryptography and Elliptic Curves - A Beginner's Guide_.

* Show that $3 \mid 0$, but $0 \not\mid 3$.

$3 \mid 0 \iff 0/3 = 0 \in \mathbb{Z}$.

$3 / 0$ is undefined, so $3/0 \not\in \mathbb{Z}$.

* Show that if $a \mid b$ and $b \mid c$, then $a \mid c$.

$a \mid b = b / a = q \in \mathbb{Z}$.
$c \mid d = d / c = q' \in \mathbb{Z}$.
Then $c = a(qq')$ with $qq' \in \mathbb{Z}$, so $a \mid c$.

* Show that if $a \mid b$ and $c \mid d$, then $ac \mid bd$.

$a \mid b$ and $c \mid d$ imply $b / a = q \in \mathbb{Z}$ and $d / c = q' \in \mathbb{Z}$.
Then $bd = ac(qq')$ with $qq' \in \mathbb{Z}$, so $ac \mid bd$.

* Show that if $m \ne 0$, then $a \mid b$ if and only if $am \mid bm$.

$a \mid b \iff b / a \in \mathbb{Z} \iff (mb)/(ma) \in \mathbb{Z} \iff ma \mid mb$.
