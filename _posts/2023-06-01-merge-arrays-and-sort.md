---
title: Merge Two Sorted Arrays (And Sort)
category: AlgoSIG 2
link: https://leetcode.com/problems/merge-sorted-array/
author:
gh_comments_issue_id: 117
tags:
  - arrays, sorting
---

## Description

Given two sorted integer arrays `nums1` and `nums2`, return one sorted list `merged`.

The number of elements initialized in `nums1` and `nums2` are `m` and `n` respectively.

Note the LeetCode description of the problem asks to do it in place in `nums1`. This is a little bit more challenging and will make the actually sorting a bit more tricky. It's possible to pass the tests and sort without doing it in place if you set `num1[:] = merged` as shown in the example code.

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


## Solution ##

```python
def merge(nums1, m, nums2, n):
  merged = []
  # Insert code here
  
  nums1[:] = merged

  ```
  
 ## Part 2 ##
 
 Now use the function above to write the sort.
 
 ## Solution

```python
def merge_sort(nums, size):
  # Insert code here
  
  ```
