---
title: First Bad Version
category: AlgoSIG 1
link:
author:
tags: array, binary-search
---

# 1. Problem Link

The problem can be found [here](https://leetcode.com/problems/first-bad-version/)


# 2. Problem Description

You have *n* versions *1,2,3,...,n* and you want to find the first one that broke the code.

You are given a function `isBadVersion(version)` which will return `True` if the version is greater or equal to first broken version. Otherwise it return `False`.

**Part 2** of this problem (not shown on LeetCode) is to solve without knowing in advance how many versions *n* you have to check.

# 3. Problem Solution

This solution is for **Part 2**, solved without knowing the total number of versions *n*. Instead of finding the midpoint between the current value and the last, the index of the current is multiplied by 2.

Other solutions can be found on the LeetCode link above.

```python
def helper(left, right):
    mid = int((right+left)/2)
    if right <= left:
        return left
    if isBadVersion(mid):
        return helper(left, mid)
    else:
        return helper(mid+1, right*2)

def firstBadVersion(n):
    return helper(1,2)
```
