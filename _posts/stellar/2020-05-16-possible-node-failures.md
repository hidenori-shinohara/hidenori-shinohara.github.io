---
layout: post
title:  "Possible node failures in an FBAS"
date:   2020-05-16
author: Hidenori
---

A node in an FBAS can fail in many ways.
The following Venn diagram copied from P.7 of the [SDF white paper](https://www.stellar.org/papers/stellar-consensus-protocol)) shows different types of node failures.

![Venn diagram of node failures](/assets/stellar/node_failures.jpeg)

# Byzantine failures
* Examples
  * A malicious user modifies the software and attempts to double spend money.
  * A computer crashes due to a power outage.
  * The network in the area stops working.

# Blocked
TODO

# Divergent
Suppose $V = \\{ v_1, v_2, v_3, v_4 \\}$ and $Q(v_1) = Q(v_2) = \\{ v_1, v_2 \\}$ and $Q(v_3) = Q(v_4) = \\{ v_3, v_4 \\}$.
Even if all of them follow the protocol without any issues, $\\{ v_1, v_2 \\}$ and $\\{ v_3, v_4 \\}$ will end up with different ledgers.
