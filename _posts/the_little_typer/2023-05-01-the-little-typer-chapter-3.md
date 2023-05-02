---
layout: post
title:  "My Solutions for The Little Typer (Chapter 3)"
date:   2023-05-01
author: Hidenori
---

```
#lang pie

(claim +
  (-> Nat Nat
      Nat))

(define +
  (lambda (a b)
    (iter-Nat a
      b
      (lambda (res)
        (add1 res))
      )
    )
  )

(claim gauss
  (-> Nat
      Nat))

(define gauss
  (lambda (a)
    (rec-Nat a
      0
      (lambda (aminus1)
        (+ (add1 aminus1)))
      )
    )
  )


(claim *
  (-> Nat Nat
      Nat)
  )


(define *
  (lambda (a b)
    (rec-Nat
      a
      0
      (lambda (aminus1)
        (+ b))
      )
    )
  )

```
