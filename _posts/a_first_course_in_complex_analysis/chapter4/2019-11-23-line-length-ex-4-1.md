---
layout: post
title:  "Line length of paths"
date:   2019-11-23
author: Hidenori
---

# Proposition
Find the length of the following paths:

1. $\gamma(t) = 3t + i, -1 \leq t \leq 1$.
1. $\gamma(t) = i + e^{i\pi t}, 0 \leq t \leq 1$.
1. $\gamma(t) = i\sin(t), -\pi \leq t \leq \pi$.
1. $\gamma(t) = t - ie^{-it}, 0 \leq t \leq 2\pi$.

# Solution
![line length](/assets/a_first_course_in_complex_analysis/chapter4/ex-4-1.jpeg)
## 1
$\int_{-1}^{1} \abs{\gamma'(t)}dt = \int_{-1}^{1} 3dt = 6$.

## 2
$\int_{0}^{1} \abs{\gamma'(t)}dt = \int_{0}^{1} \pi dt = \pi$.

## 3
$\int_{-\pi}^{\pi} \abs{\gamma'(t)}dt = \int_{-\pi}^{\pi} \cos(t) dt = 4\int_{0}^{\pi/2} \cos(t)dt = 4$.

## 4
$\int_{0}^{2\pi} \abs{\gamma'(t)}dt = \int_{0}^{2\pi} \abs{1 - e^{-it}} dt = \int_{0}^{2\pi} \abs{2 - 2\cos t} dt = 8$.
(I'm not sure how to integrate this, but [this is what Wolfram Alpha says](https://www.wolframalpha.com/input/?i=integrate+abs%281+-+e%5E%28-it%29%29+from+t+%3D+0+to+2+pi).)
