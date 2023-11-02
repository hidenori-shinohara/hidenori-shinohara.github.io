---
layout: post
title:  "Merkle Patricia Tree in Ethereum"
date:   2023-11-02
author: Hidenori
---

Notes for [the post by Ethereum](https://ethereum.org/en/developers/docs/data-structures-and-encoding/patricia-merkle-trie/).

# Node Structure

- `NULL` is the empty string.
- A branch node is `[v0, v1, ..., v15, vt]`.
- A leaf node is `[path, value]` where the path is either `<20, XX, XX, ..., XX>` if the length of the path is even, and $<3X, XX, ..., XX>$ if odd.
- An extension node is `[path, key]` where the path is either `<00, XX, XX, ..., XX>` if the length of the path is even, and $<1X, XX, ..., XX>$ if odd.

