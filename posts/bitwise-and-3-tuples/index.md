---
title: Bitwise and 3-tuples
slug: bitwise-and-3-tuples
date: 2019-05-02 00:00:00 UTC-05:00
tags: 
category: "AlgoSIG 3"
link: https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/
description:
type: text
author: "Kevin Nasto"
---

# Description
Given an array of numbers, `A`, find the number of 3-tuples `(i, j, k)` indices in `A`, where the bitwise AND is equal to `0`. Assume the numbers in `A` are between 0 and 2^16.

```
0 <= i < A.length
0 <= j < A.length
0 <= k < A.length
A[i] & A[j] & A[k] == 0, where & represents the bitwise-AND operator.
```

Example:
```
Input: arr = [1,2,3]
Output: 12
```

# Solution

```python
import collections


def countTriplets(A):
   """
   :type A: List[int]
   :rtype: int
   """
   cnt = collections.defaultdict(int)
   for x in A:
       for y in A:
           cnt[x & y] += 1
   res = 0
   for num in A:
       for key in cnt.keys():
           if num & key == 0:
               res += cnt[key]
   return res
```