---
layout: post
title:  "Prove $L(X)$ is subexponential"
date:   2023-09-20
author: Hidenori
---


Let $L(X) = e^{\sqrt{(\ln X)(\ln \ln X)}}$.
We claim that $L(X)$ is subexponential.


$$
\begin{align*}
    e^{\sqrt{(\ln X)(\ln \ln X)}}
        &> e^{\sqrt{(\ln \ln X)(\ln \ln X)}} \\
        &= e^{\ln \ln X} \\
        &= \ln X.
\end{align*}
$$

$$
\begin{align*}
    e^{\sqrt{(\ln X)(\ln \ln X)}}
        &< e^{\sqrt{(ln X)(\ln X)}} \\
        &= e^{\ln X} \\
        &= X.
\end{align*}
$$
