---
layout: post
title:  "The set of befouled nodes is a DSet"
date:   2020-05-17
author: Hidenori
---

# Proposition
In an FBAS with quorum intersection, the set of befouled nodes is a DSet.

# Solution
Let $\ev{V, Q}$ be an FBAS with quorum intersection.
Let $B$ be the intersection of all DSets that contain all ill-behaved nodes.
Since [the intersection of two DSets is a DSet](https://hidenori-shinohara.github.io/2020/05/17/intersection-dset.html) and $V$ is finite, $B$ is a DSet.

* $v \in B$.
    * Then there exists no DSet $B_v$ such that $B_v$ contains all ill-behaved nodes and $v \notin B_v$.
      Therefore, $v$ is not an intact node.
      In other words, $v$ is a befouled node.
* $v \notin B$.
    * Then there exists a DSet $B_v$ that contains all ill-behaved nodes and $v \notin B_v$.
      In other words, $v$ is intact and thus $v$ is not a befouled node.

Therefore, $B$ is precisely the set of befouled nodes and it is a DSet.
