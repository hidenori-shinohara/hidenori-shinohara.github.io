---
layout: post
title:  "Simple example of homomorphic encryption"
date:   2023-04-03
author: Hidenori
---

This post is inspired by "Why and How zk-SNARK Works: Definitive Explanation" by Maksym Petkus.

# Homomorphic encryption

1. Pick two natural numbers $g, n$.
1. For any value $x$, encrypt it by taking $g^x \pmod n$.

In other words, this is a straightforward application of [the discrete logarithm problem](https://en.wikipedia.org/wiki/Discrete_logarithm).
It might make more sense to see this as hashing than encryption.
It is certainly possible to decrypt it with the proper setup, but it seems that we don't really decrypt the value, at least in the paper I mentioned above.

# Number theory

This doesn't really work if the pair $(g, n)$ isn't chosen well.
For instance, if $n = 1$, then $g^x \pmod n = 0$ for any $g$.
For this to make sense, the [multiplicative group of integers module n](https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n) has to be large.
Furthermore, it is important that $g$ is chosen carefully as the subgroup $\langle g \rangle$ has to be large.
For simplicity, it makes sense to pick a generator of the group as $g$.
Such a generator is called [a primitive root modulo $n$](https://en.wikipedia.org/wiki/Primitive_root_modulo_n).

It turns out that not all multiplicative groups have generators.
A simple example is when $n = 8$.
As the multiplicative group of integers module 8 consists of $\\{ 1, 3, 5, 7 \\}$.

- $\langle 1 \rangle = \\{ 1 \\}$
- $\langle 3 \rangle = \\{ 3, 1 \\}$
- $\langle 5 \rangle = \\{ 5, 1 \\}$
- $\langle 7 \rangle = \\{ 7, 1 \\}$

As discussed in [this wiki page](https://en.wikipedia.org/wiki/Primitive_root_modulo_n), the multiplicative group of integers module $n$ has a generator if and only if $n \in \\{ 1, 2, 4, p^k, 2p^k \\}$ for any odd prime $p$ and any $k \in \mathbb{N}$.
Finally, the same page discusses an efficient algorithm for finding such a prime.

# How this encryption can be useful

This encryption is useful because you can do some arithmetics on two encrypted values without decrypting.

For instance, you might have two values $a, b$ that you have encrypted.
We'll denote them $e(a), e(b)$.
Later, you might realize that you want to encrypt $a + b$.
Normally, you would calculate $a + b$ and encrypt that.

However, with the encryption method above, you just simply multiply $e(a)$ by $e(b)$.
This is because $e(a)e(b) = (g^a \pmod n) (g^b \pmod n) = g^{a + b} \pmod n = e(a + b)$.

This might seem like a subtle difference but this is extremely useful in zero knowledge proofs.
