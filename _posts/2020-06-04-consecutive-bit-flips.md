---
title: Minimum Number of K Consecutive Bit Flips
category: AlgoSIG 3
link: https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/
gh_comments_issue_id:
author:
tags:
  - Greedy
  - Events
participants:
---

## Description

In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) subarray of length K and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of K-bit flips required so that there is no 0 in the array.  If it is not possible, return -1.

1 <= A.length <= 30000

1 <= K <= A.length

## Solution

``` python
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
```
