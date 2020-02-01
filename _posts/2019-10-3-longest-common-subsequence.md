---
title: Longest Common Subsequence
slug: longest-common-subsequence
date: 2019-10-03 00:00:00 UTC-05:00
tags: Dynamic programming
category: AlgoSIG 1
link: 
description:
type: text
---

# 1. Problem Link

The problem can be found [here](https://leetcode.com/problems/longest-common-subsequence/)


# 2. Problem Description

Given two strings *text1* and *text2*, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return `0`.


# 3. Problem Solution


Other solutions can be found on the LeetCode link above.

```python
class Solution:

    def __init__(self):
        self.matrix = {}

    def longestCommonSubsequence(self, P: str, Q: str) -> int:

        n = len(P)
        m = len(Q)

        result = 0
        keyy = f'{n - 1},{m - 1}'
        if keyy in self.matrix.keys():
            return self.matrix[keyy]

        # BASE CASE
        if n == 0 or m == 0:
            result = 0

        # CASE 1
        elif P[n - 1] == Q[m - 1]:
            result = 1 + self.longestCommonSubsequence(P[:-1], Q[:-1])

        # CASE 2
        elif P[n - 1] != Q[m - 1]:
            tmp1 = self.longestCommonSubsequence(P[:-1], Q)
            tmp2 = self.longestCommonSubsequence(P, Q[:-1])
            result = max(tmp1, tmp2)

        self.matrix[f'{n - 1},{m - 1}'] = result
        return result
```