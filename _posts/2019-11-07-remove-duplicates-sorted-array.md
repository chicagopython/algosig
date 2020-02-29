---
title: Remove Duplicates from Sorted Array
category: AlgoSIG 9
link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
author: Chris Luedtke
tags:
---

## Description

Given a sorted array `nums`, remove the duplicates *in-place* such that each element appears only once, and return the new length.

Do not allocate extra space for another array.

```python
# example
nums = [1, 2, 2, 3, 6, 7, 7]
unq_nums_len = remove_duplicates(nums)

print(unq_nums_len, nums, sep='/n')

>>> 5
    [1, 2, 3, 6, 7]
```

[Further Reading: *How are Lists Implemented in Python?*](https://docs.python.org/3.8/faq/design.html#how-are-lists-implemented-in-cpython)

## Solution

```python
def remove_duplicates(nums: List[int]) -> int:
  if len(nums)==0:
    return 0

  i = 0
  for j in range(len(nums)):
    if nums[j] != nums[i]:
      # copy the new value to the pos in front of i
      # and increment both
      i += 1
      nums[i] = nums[j]
    # else i stays the same, increment j
  return i + 1
```
