---
title: First Bad Version
category: AlgoSIG 1
link: https://leetcode.com/problems/first-bad-version/
author:
gh_comments_issue_id: 73
tags:
  - array
  - binary-search
---

## Description

You have *n* versions *1,2,3,...,n* and you want to find the first one that broke the code.

You are given a function `isBadVersion(version)` which will return `True` if the version is greater or equal to first broken version. Otherwise it return `False`.

```
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
```

## Solution

This is the binary search approach with is `O(log(n))` instead of `O(n)` 

```python
def helper(left, right):
    mid = int((right+left)/2)
    print(left, right, mid)
    if right <= left:
        return left
    if isBadVersion(mid):
        return helper(left, mid)
    else:
        return helper(mid+1, right)
    
    
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return helper(1,n)
```
