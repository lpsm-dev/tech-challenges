# -*- coding: utf-8 -*-

tam = int(input())
nums = input().split()
if tam == len(nums):
  a, b, c, d = 0, 0, 0, 0
  for n in nums:
    value = int(n)
    if value % 2 == 0: a += 1
    if value % 3 == 0: b += 1
    if value % 4 == 0: c += 1
    if value % 5 == 0: d += 1
  print(f"{a} Multiplo(s) de 2")
  print(f"{b} Multiplo(s) de 3")
  print(f"{c} Multiplo(s) de 4")
  print(f"{d} Multiplo(s) de 5")
