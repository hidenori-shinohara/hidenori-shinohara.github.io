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
- A leaf node is `[path, value]` where the path is either `<20, XX, XX, ..., XX>` if the length of the path is even, and `<3X, XX, ..., XX>` if odd.
- An extension node is `[path, key]` where the path is either `<00, XX, XX, ..., XX>` if the length of the path is even, and `<1X, XX, ..., XX>` if odd.

Using the language of an `RLPEncodableItem`,

- `NULL` is `String(Vec::new())`.
- A branch node is `List(vec![v0, v1, ..., v15, vt])` where `v0`, ..., `v15`, `vt` are nodes represented as `RLPEncodableItem`.
- A leaf node is `List(vec![String(path), String(val)])` where `path` and `value` are `Vec<u8>`.
- An extension node is `List(vec![String(path), key])` where `path` is `Vec<u8>` and `key` is a node represented as `RLPEncodableItem`.

Let `v` be a node represented as `RLPEncodableItem` that a branch or extension node is pointing at.

- If `len(rlp.encoding(v)) >= 32`, we will include `String(rlp.encoding(v))` to refer to `v`.
- If `len(rlp.encoding(v)) < 32`, we will include `v : RLPEncodableItem` directly to refer to `v`.

# Other constraints
- A branch node may not have `>= 15 NULL`'s.
  It's explicitly prohibited in the yellow paper.
  _no branch nodes may exist that contain only a single non-zero entry_.

# How big is an MPT node?
1. Each `v_i` and `v_t` in a branch node and also the `key` in an extension node is either `String(hash_32_bytes)` or `List` whose RLP-encoding is <= 32 bytes.
1. The `path` in `String(path)` is <= 32 bytes as Ethereum uses a 32-byte hash as the key.

The only field that is not bounded is `value`, and `value` could easily be bigger than 32 bytes.

In fact, here is an example RLP-encoded leaf node: `0xf86d9d205b08a40657ab3ecac33746bb9e15e4e9ebfd48407936042c79d5e88eb84df84b0187266437d6c63228a056e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421a0c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470`

This decodes into:

```
[
    "0x205b08a40657ab3ecac33746bb9e15e4e9ebfd48407936042c79d5e88e",
    "0xf84b0187266437d6c63228a056e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421a0c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470"
]
```

In other words, this leaf node is `List(vec![String(0x205b...), String(0xf84b...)])`.

The first argument is `0x205b08a40657ab3ecac33746bb9e15e4e9ebfd48407936042c79d5e88e`, which is the path.
As it starts with 20, the path length is even.
More specifically, the path is `5b08a4...e88e` and it is 28-bytes long.

The second argument is a 77-byte RLP-encoded list.
It decodes into:

```
[
    "0x01",
    "0x266437d6c63228",
    "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470"
]
```

This corresponds to: nonce, balance, storage hash, code hash.

After decoding everything, we can see that the node is:

```
[
    "0x205b08a40657ab3ecac33746bb9e15e4e9ebfd48407936042c79d5e88e",
    [
        "0x01",
        "0x266437d6c63228",
        "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
        "0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470"
    ]
]
```

However, note that encoding this will *NOT* give our first encoded byte string `0xf86d9d205b08a40657ab3ecac33746bb9e15e4e9ebfd48407936042c79d5e88eb84df84b0187266437d6c63228a056e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421a0c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470`.

This is because we would first have to RLP-encode the `value` part and stick it into the leaf node as a `String(byte_array)` object, and then decode the node.


# More references
- I filed a bug as I found a few typos in the blog post: https://github.com/ethereum/ethereum-org-website/issues/11635
- [Ethereum Yellow Paper](https://ethereum.github.io/yellowpaper/paper.pdf)'s _Appendix D. Modified Merkle Patricia Tree_
