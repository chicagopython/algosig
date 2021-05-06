---
title: Merge Sorted Array
category: AlgoSIG 1
link: https://leetcode.com/problems/merge-sorted-array/
author:
gh_comments_issue_id: 93
tags:
  - arrays, sorting
---

## Description

Given two sorted integer arrays `nums1` and `nums2`, return one sorted list `merged`.

The number of elements initialized in `nums1` and `nums2` are `m` and `n` respectively.

Note the LeetCode description of the problem is slightly different because it asks to do it in place in `nums1`, but it will still work if you do it this way if you set `num1[:] = merged` as shown in the example code.

Example 1:
```python
Input: nums1 = [1,2,3], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
```

Example 2:
```python
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
```


## Solution

```python
def merge(nums1, m, nums2, n):
  merged = []
  # Insert code here
  
  nums1[:] = merged

  ```
