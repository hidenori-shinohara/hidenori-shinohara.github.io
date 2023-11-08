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

# Case study
Here's the proof of the path for ETHGlobal's account.

```
[
    "0xf90211a018d6c6b28333daa5b9b0de77a587ebae880674def2a7878decb3ce8d2cbccd7da0450be2f3b4aa3f4e1b88c310134fe88533b9bbc6c5726e85efd1bfe944ac9158a0740f74da7ec67bbc0a6fc0429269e9aa9dc80db6fee96eef96db1812a0e2d327a06bc1617a8826a28f4c72ab3638f6fdba56d055b2ac3222d01e7b820f94e0eedfa0e93b21d3f73f4afc147cb9ad700110b175dad415419f9377f9f1c6b2681237efa04ff6fdabb0444d612ecc108f95d324da3e713cdbd4465a0cc71e67bff4872667a01f78e5e5eba52ec7a4a77c8af83b2325b1178f3309a4b26b1e866cfd60e1f98fa0d20a9849469d5b71edc193e5ebcea34730fe373bf4c96e45980ae26ebbc29efea002915348d9312cea04f300c49f37d4560626f78bda5f84558e6cf24589162fc2a09ec88734afaf01b65905665483ee05288436d901f973af09b9a75e3dbf992979a0902973f5cdec39260b9c9ce4f6bfd9381d37c9b85e43ebf5ebf5da2f78b12d18a026aaa39a63de4fb2bbcbe6b7df606b2f2843c959c7e123b9a4369811974dabfda08a6fadd0ec139c7c86647220e6e39a38cc5665e22b362b4936da3df733c46f22a02e3440883087c708a906e81a56610a86159e2623ef0b2e705f3a42220412af85a035c0a5ac653b5bc37648b57a49cb775940bc639bb5cae2669c8bef590d988b5aa033a23e9a565ae0a78c9c4ee36bebbbc964fce5cc4b75f4f2e32bb87d8f919b7680",
    "0xf90211a041252e075fa3ab3808a717489b0e1eada594198d7c1df5ff0fd57fa83ab9e91fa014878fa3de5b28ff2de84e850291ea8f61b27b040849525e9d0d8bbc9b8f23ada090d457c802bdeccaa3d0b2adc48ab157cca13dcd8ccd6afad511e99c614122fca0e85e0fec0094759d022334c16c08154c7c9dd8e03c6d1452f5519b7644d4ac2ba0063daa2d1aa24e342d4138b9a20d80c53e2db99066d69bc4d636a71f5fe6196da078748899234384aa7a3252d8a6d3ecc1e4c61877858aca50425827891ee97cfea0f2d97b2d1319e8f43be58f7a97bf685993a340ff79d5ded186eea82e8db1f7e1a078a3856568b05657c8719b914e53ac4ec26918b53682097ebe28ddd3a5baba5ea0ed00ae52e4ebab05a4d8a71f78bea3111757f83869dc985154666501f56c8d2fa0cadae92038de11a7f5b3e500d5b39ad925fff85f5b5e35b54925a48fa66bbce8a0bf0963f23952f8cffb505eabf5b3ac792de224737f154ff75cd8ac05ffebb557a0c0833076c017a2e903c420d184ffaad64acd5d4166a8083df2fcfdde912f9a50a054163d2a787439154d7dc77e5bbaf82645879e14f3b9b34910d93aed5a9305b4a02e849550df28ca6d1be6afade961d7da22561c32d78dac3630fdfde52215b46fa02604b09381761c60be5579d7e31b749b931ca14cb53c202e7066b89a58302714a08f7ee2ed381014ab0a2600ff4389f3b586ee39fa4ed3aa5c34a643880937b94080",
    "0xf90211a0050d77f309ad467d694d7742ef37a9c56a8fbd733943e8303905ccd2b5c5a31aa0890178cfe9134aa1efba9cb04fcb465f485614fc462fbd687d4265459f89e855a0f5657eeae46e4cc74e2313d1fdf6416f3713e5e3d8a78024cf2c17eb230b7d6ea0320c7c2d47ff89a12d7c17562f4b11358a2f0a6c295a418b86f7e1859dd15b8ea05b765613c30e1f28961e6db00738603d14bac0a2156fcd80cc3aff90faa85bc1a0f6af1af566e38c0e79dd558f33dc2191950f5419d3859c2ce14c86ed1ce86460a069ec9f67585224217f871811b278e3ac5513340ea8fb40abba9024144deb1c9ba07b4f37cf494d99d9b0f0a0c84b6b962bed6d9c50695ea01efbcb39ab7efa3feda08a671e3a2efdf64f63665f47e542b15fb0c5d4a46d18b13a303472c1e0b06cb7a0490313233bc3c1f05a7b857db9675529b77c4122afd072f6650fa4a5eb8acd50a08a9242ec83964381cd73218222e6cd8f348ae42bfd8bfb9d57646a1ef7e58e6aa09f017dd7a7003074da76ec93dbabe0937c4aac60ebe9acd6d4eee51570c20943a03dcf6e33625b70fdcbbd521777dca0f6c260fb7a054b55560c806f194588577aa02fc8ff257d0231b9decb65369f8554eb1a39d347303e69373e9baa0e96d3f892a03f4903282e362ac6b6612448bde022213af510772564079cd370c967be5b0c9ca01cded41896340d515edf0df64c2f989b2ff1b69d8e76f0ed2f780eea033c82a380",
    "0xf90211a0932b55f9eee8d7120f60ddb42b5c59271bc8794643856e61ac65044d338f8558a009e190ae5d1f4a9b056f9325aed4e91693e2aa28daf935dccf753376bbd98702a0809ba224dc09912ce1e5ce1b19031cbd9db8cdaaf8180bf6b773e0a1a0e7b0d6a04444f3f7146269776c0ff88b55592dfe09009d7dd837c4adf2b9ec800c280519a087d4322a7db7e87c97a11888d6385846851e7d34f7a9e8a948c635808bac66e1a0a2de659c14a2a7412259a23b844610b27091b88e68f39008c180c3a5e73bc1f3a03c8c395308ec72cd4488047cd49fd85afc1973879f32d18a6a78884575dce262a0e6f4c664af308354363b47d687c0a1f0b39fa44bdb4d1946e088d40e81d17604a0289b2296f9ef230b9b548141f07edd2f9afc0697e5cb13a6c052967482318db5a01b60eeee23088489b0f210b87981ad456066d81ddc7ca4831fd0d7f5684e83d5a096cb4737e61d2494bf615d204f1ab17b33a8e6cc2202d8c42d194e394c49cb8fa09a64452c574f30a68c0d0c3e8d610372375a3e6ccf6376f03dda297c362964a0a03d3f577b2b4ea7c7d1ea6b751f87b867616328dce3f3bbcc1829f5eced330d80a0f5cbe7bb776435eb78041748abea0371bcd2d743ca0f7b2945285b312f9c91a3a0b634122c093437dc70bb9f4354183e93eab37ce7e0e576048840c2b0cd55ca9ea0610727a8b4cd35e16d0296d7dccadc0a736ef62557d5dc36a828611049eaafc880",
    "0xf90211a039fb44712e438c7b8e0e3cefe57fab533424e44697abebd5184b9a796d3d9a19a042750d92bf27f6d2573210854749619ac21ce552f13b669cb6d8230ef85aa1b9a0dcf73fca6210a634d5c7ee66283155be12dd9eafe89d5e1bc141428958b380cba0aa149f6e9bf27d02783cd9c5539d5277f17e8f230772095feb103c4d073c7106a0db757353c616e0ed4146facc43089429d809b2b59a21bcee4481d0facf25daa7a0bba2aec3f6a69862e794c3ef27df5b135ff6f43e015cc1d4548fdc1c7721a5d6a0b74f10f8b31f2de595cc74e15083001ce04401285e244bf6fe990a59111b9ad7a0e69dac1014360b1a52a41c75a79db5d4f5e9581e30a477622b4f39e800272f39a0bf6371e0e8395e3da66073140d4d4284a3e10953bf50789b78959119b903e01ea0815bfac530740ff2f98f0abf4e28c020fdbe48f531b334324a78c003963e57aea0eefc05c5e110004f98ee1b7d36d67b3eb23bb232b96d17a7cae91720ed7efde4a0db8467645171691c4454555eaf81d1407c1c40620a6e0e6a8bd6af37a441970da0f861643b9e865c0a8cc68e0391219c1ea8a76c2ab78b83949b5f93e027402d06a06c09d87265fa9a2804904843dd98d95cfc48515ceb294571c0f6adcab24b03e6a03a01ee5b44c88d5e5728d3237c8d750d1dd02caff5b6903de4e31cb6eb909ce9a03bfc67659c7d7b2019b4d1fb9f434727cab270df7ab5990e53e948ddee57464180",
    "0xf90211a0c2717baa4e33cefd4fa4315bfa13d59c84fad4158113b11f3e320d9685a39d7da08bdbed90f58b09bb79e5cf8b322f595ddf8377d9ab7d3c451a7f56d663bf7377a05c67b94aacf25d1abf4d7a3f4e6c4540d81a1386ded86738c20f78c0182520c3a0a80be8e9110eeb82365bf4fd77f87d193120ca4384c99ddb1c6cb91d07b71cafa0e4ad621cf4d57986d3add88f38b0e7907130d2bbede05b067a5f1aff4ec58669a0652522234ca2bf0055749234d30ea49819e6b127029dd5c9c80c542473dbddeaa08a9be1f9a1fb6fb91114effbed5c75131dc57480ff0400550f86e7e56b851774a0a64ba35d28ffb39f920f90b5abb7ce809cbc53ab54fa3ad029a68146e4168d07a074bb4ea0440bfac93a8c40565f863acd45dcfe7d0c9534473ed295424e32ef12a0e7362a3396ecae24aaf06f50165eaf903739a2aa77effe4973373edc95d0af91a0813e366966f91e2a3f66949a2f07eaba03cfd7921c4d4d79a7874a303ec19880a082dfdd2dab55d9a4f4104d0cbde1c533504f5b23d567210b0f7ea8aa66e267f9a0b36c511f531ba943157b892f4f1b0289706d696335dbb290c48d2e361809c51da0c63d2e7e96575c78a8fdfc308254eb87944b28825c6111d18782cb9dc09b2bcea0b607a31934e8267b7dff817eeef4054d9b97260830b22bd54228c73e98fd8c18a080c6735390686d5e64384d146ccbce9af0020916a8a556d9890a8e8bfff44d3a80",
    "0xf90151808080a0eae0f9119829eb2c95ab9a7c512611dd15f865b0b6bcb79120e8baa66d41fb9fa046ec69737b80f7339615414902521dcfcdc65e2925bdbd1b7e39ceac75f17bb9a034f6eb707a84d7d369bdd53b45b92bdb807cb777dd4e38307b72597426808eeaa0ffaad9a6c4dc86c5538dcea592b211993debf94611498a4cee86b627ec7cceae80a03f84aeee6ce05e453011d0684aa4e95c1eae60ec0221f0bea08e99271977e638a044b7ec12971a2e91f5614fd5bcd1f6d5e92760f094966d731be8d9a3efe6b8b3a079690b80640075c24bed554559d5e037eac8c78c0ef6d164811127f3bc6e9761a023326ad841c693ecf304ad4f4daca45945d29997297141c3f615316169b6c78f80a0bc6ffeaf2d543e6448b061ed334362fdd22f97d1bfa630f7963d2396682cc0b8a0eca237f9f30343ac6aaf5d41501f6ae3e3272422791a2632d473bf1d872eee738080",
    "0xf8709d368c3ebf850d4896129da897b4c5d2da651431d5d0eaeda4de0ccff583b850f84e81c48908aea84b56865c19dfa056e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421a0c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470"
]
```

Then the first 6 nodes are branch nodes that have 16 branches.
The 7th branch node has only 10 branches.
The 8th node is a leaf node.
The first field is 29 bytes long, and the second field is 80 bytes long.
- Path: `0x368c3ebf850d4896129da897b4c5d2da651431d5d0eaeda4de0ccff583`
- Value: `f84e81c48908aea84b56865c19dfa056e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421a0c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470`

As the path field starts with `3`, the length is odd.
Therefore, the path is `68c3eb...583`, which is 57 letters long.
This makes sense as this path has exactly 7 branch nodes, which adds 7 letters and 57 + 7 = 64.

# What does a typical path look like?

Let `A` be an account and we are interested in the proof for that.



# More references
- I filed a bug as I found a few typos in the blog post: https://github.com/ethereum/ethereum-org-website/issues/11635
- [Ethereum Yellow Paper](https://ethereum.github.io/yellowpaper/paper.pdf)'s _Appendix D. Modified Merkle Patricia Tree_
