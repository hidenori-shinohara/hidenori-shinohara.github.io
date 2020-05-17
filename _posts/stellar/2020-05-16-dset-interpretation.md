---
layout: post
title:  "Interpretation of the definition of a DSet"
date:   2020-05-16
author: Hidenori
---

# Quorum intersection despite $B$
This protects against nodes in $B$ making contradictory assertions that enable other nodes to externalize inconsistent values for the same slot.
If $\ev{V, Q}^B$ enjoys quorum intersection but does not enjoy quorum availability despite $B$, then $\ev{V, Q}$ will have a problem when nodes in $B$ start making contradictory assertions.

TODO

# Quorum availability despite $B$
This protects against nodes in $B$ refusing to answer requests and blocking other nodes' progress.
Suppose $\ev{V, Q}^B$ does not enjoy quorum intersection but enjoys quorum availability despite $B$.

Then
* $\ev{V, Q}$ can function if some nodes in $B$ refuse to answer requests. (e.g., power outage, network issue)
* $\ev{V, Q}$ can't function if some nodes in $B$ make contradictory statements.

Consider the FBAS in [the DSet example post](/2020/05/16/dset-examples.html).
Let $B = \\{ v_5, v_6 \\}$.
Then $V \ B$ is indeed a quorum.
As shown in the first proposition in [the DSet example post](/2020/05/16/dset-examples.html), $B$ does not enjoy quorum intersection.

We will not go into the details, but
* Even if every node in $B$ refuses to answer requests, every node has a quorum slice that doesn't contain any nodes in $B$.
  One can imagine that $V \ B$ can still keep going.
* Suppose every node in $B$ starts acting arbitrarily.
  For instance, $B$ tells $v_9$ that "Person A pays person B 10 dollars" and tells $v_{10}$ that "Person A pays person C 10 dollars" when Person A only has 10 dollars in their account.
  Since $B \cup \\{ v_9 \\}$ is a quorum slice for $v_9$ and $B \cup \\{ v_{10} \\}$ is a quorum slice for $v_{10}$, one can imagine that this will result in double spending.
