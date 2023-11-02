---
layout: post
title:  "Recursive-length prefix serialization"
date:   2023-11-01
author: Hidenori
---

Summary of [the post by Ethereum](https://ethereum.org/en/developers/docs/data-structures-and-encoding/rlp/)

An item is defined to be:
- a byte array, or
- a list of items.

# How to encode a byte array
1. An array containing a single byte in the range of `[0x00, 0x7f]` is its own encoding.
    1. `0x11` is `0x11`.
    1. Note that `0x11` is technically a shorthand for `{0x11}`.
1. If a byte array has $\leq 55$ elements, the first byte is `0x80 + length` and the byte array will follow.
    1. `0x111111` is `0x83111111`.
    1. `0x111111` is technically a shorthand for the array `{0x11, 0x11, 0x11}`.
    1. `0x83` because `0x80 + 3` where 3 is the length of the byte array.
1. If the byte array has $\geq 56$ elements, the first byte is `0xb7 + length in bytes of the length`, the second byte is the length and the rest is the byte array.
    1. `0x11111...11` where we have 100 `11`'s.
    1. In other words, the byte array `{0x11, 0x11, ..., 0x11}` (100 bytes).
    1. This is encoded as `0xb864` followed by 100 `11`'s.
    1. The length 100 is 64 in hex decimals.
    1. 64 is 1-byte long.
    1. `0xb8 = 0xb7 + 1`.

# How to encode a list of items
First, you must encode every item in the list.

1. If the combined length of all the encoded items is $\leq 55$, then the first byte is `0xc0 + combined length` and the encoded items will follow.
    1. `[0x11, 0x111111]`.
    1. The elements are encoded as `0x11` and `0x83111111`.
    1. This is 5 bytes.
    1. So, the encoding is `0xc51183111111`.
1. If the combined length of all the encoded items is $\geq 56$, then the first byte is `0xf7 + length in bytes of the combined lengths`, the second byte is the combined length and the encoded items will follow.
    1. `[0x11, 0x111111, 0x11...11]` where the last byte array is the 100-byte array.
    1. The total length is `1 + 4 + 102 = 107`.
    1. 107 is `6b` in hex decimals, which is 1 byte.
    1. Therefore, we obtain `0xf86b1183111111b86411...11`.





