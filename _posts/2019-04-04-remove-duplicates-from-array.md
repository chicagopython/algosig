---
title: Remove Duplicates from an Array
category: AlgoSIG 2
link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
author: Sree Prasad
tags: array, python-101
---

## Description
Given a sorted array of integers *nums* and a positive integer *n*, remove the duplicates in-place (without allocating extra memory) such that there are at most *max_count* occurrences of that number in the array. Return the new length of the array with the duplicates removed.

##### Example:

```python
>>> nums = [1,2,2,2,3,4,4]
>>> max_count = 2
>>> remove_duplicates(nums, max_count)
6
>>> nums
[1,2,2,3,4,4,4]
```

After the function runs, the value returned is `6` and the contents of the input array are `[1,2,2,3,4,4,x]` where 'x' could be anything. In the example above, it is '4'  

---
## Solution
Here is one possible solution to the problem. We iterate through `nums` keeping track of the numbers we removed as `offset` (meaning the index offset) and the number of times we've seen the number at the current index as `count`.
When we encounter consecutive elements that are equal, we increase the `count`. When they're not equal, we reset the `count` to 1.
If the `count` is greater than `max_count`, then we "remove" it by increasing the `offset` and overwriting the value at index `i - offset`.

```python
def remove_duplicates(nums, max_count):
    offset = 0
    count = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1

        if count > max_count:
            offset += 1

        nums[i - offset] = nums[i]

    return len(nums) - offset
```

The runtime is O(n), where *n* is the number of elements in the array `nums`.
