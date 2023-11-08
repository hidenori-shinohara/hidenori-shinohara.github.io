---
layout: post
title:  "Merkle Patricia Tree in Ethereum"
date:   2023-11-02
author: Hidenori
---

Notes for [the post by Ethereum](https://ethereum.org/en/developers/docs/data-structures-and-encoding/patricia-merkle-trie/).

# Prerequisites
First and foremost, one should understand [RLP encoding](/2023/11/01/rlp-serialization.html) before jumping into MPT for a reason you might not expect.
This is not because one might want to encode the MPT.
This is because a MPT is an RLP-encodable object.

More specifically, an RLP-encodable object is defined to be:

```
enum RLPEncodableItem {
    String(Vec<u8>),
    List(Vec<RLPEncodableItem>),
}
```

One should think that a MPT is represented as an `RLPEncodableItem`.

# Node Structure

- `NULL` is the empty string.
- A branch node is `[v0, v1, ..., v15, vt]`.
- A leaf node is `[path, value]` where the path is either `<20, XX, XX, ..., XX>` if the length of the path is even, and $<3X, XX, ..., XX>$ if odd.
- An extension node is `[path, key]` where the path is either `<00, XX, XX, ..., XX>` if the length of the path is even, and $<1X, XX, ..., XX>$ if odd.

Using the language of an `RLPEncodableItem`,

- `NULL` is `String(Vec::new())`.
- A branch node is `List(vec![v0, v1, ..., vt])` where `v0`, ..., `vt` are nodes represented as `RLPEncodableItem`.
- A leaf node is `List(vec![String(path), String(val)])` where `path` and `value` are `Vec<u8>`.
- An extension node is `List(vec![String(path), key])` where `path` is `Vec<u8>` and `key` is a node represented as `RLPEncodableItem`.

Let `v` be a node represented as `RLPEncodableItem` that a branch or extension node is pointing at.

- If `len(rlp.encoding(v)) >= 32`, we will include `String(rlp.encoding(v))` to refer to `v`.
- If `len(rlp.encoding(v)) < 32`, we will include `v : RLPEncodableItem` directly to refer to `v`.


# More references
- I filed a bug as I found a few typos in the blog post: https://github.com/ethereum/ethereum-org-website/issues/11635
- [Ethereum Yellow Paper](https://ethereum.github.io/yellowpaper/paper.pdf)'s _Appendix D. Modified Merkle Patricia Tree_
