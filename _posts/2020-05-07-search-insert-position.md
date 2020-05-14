---
title: Search Insert Position
category:
link: https://leetcode.com/problems/search-insert-position/
author:
gh_comments_issue_id: 37
tags:
  - unsolved
---

## Description

Given a sorted array, `nums`, and a value, `target`, return the index if the target is found. Otherwise, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
```python
nums   = [1,3,5,6]
target = 5

return 2
```
Example 2:
```python
nums   = [1,3,5,6]
target = 2

return 1
```

## Solution

```python
from typing import List

def search_insert(nums:List[int], target:int) -> int:
  # write solution here
  return

# tests
assert search_insert([1,3,5,6], 5) == 2
assert search_insert([1,3,5,6], 2) == 1
```

## Solution A

When reading an algorithm prompt, pay attention if an input is a sorted list. Usually this means we can use some tricks so we don't have to check all the values of the list.

In this case, we only need to know where to insert our `target`. If we check a value in the middle of the list, we know whether `target` should be in the bottom half or the top half of the list. We do not need to check any other values, and can ignore the other half of the list entirely!

In this solution we store a `l_i` (left index) and `r_i` (right index). These represent the index range of a subsection of our `nums` list. At first, this is the entire list range. But as we continue to check the values between these indexes, we update either `l_i` or `r_i` to narrow in on the location of the list where we expect to find our `target`.

```python
from typing import List

def search_insert(nums:List[int], target:int) -> int:
  l_i = 0
  r_i = len(nums) - 1

  # first check if `target` is even in the range of `nums` values
  if target < nums[l_i]:
    return 0  # insert at start if target < minimum
  elif nums[r_i] < target:
    return len(nums)  # insert at end if target > maximum

  while True:
    # Check if we found our target at l_i
    if nums[l_i] == target:
      return l_i

    # Check if we found our target at r_i
    elif nums[r_i] == target:
      return r_i

    # If `l_i` and `r_i` are consecutive integers the `target` is not
    # at either position already (checked above), then we know
    # the `target` must go between these values. We use a Python
    # trick to add integer `l_i` to a boolean to figure out where.
    elif r_i - l_i == 1:
      return l_i + (target > nums[l_i])

    # If the above checks fail, we get the middle position between
    # `l_i` and `r_i`, and check whether our `target` should be less
    # than or greater than the middle value. Then we update either `l_i`
    # or `r_i` to narrow down the search, and we return to the top
    # of the `While` loop above.
    else:
      mid_i = (l_i + r_i) // 2
      if nums[mid_i] <= target:
        l_i = mid_i
      else:
        r_i = mid_i
```

## Solution B

Python actually includes a module, [`bisect`](https://docs.python.org/3.8/library/bisect.html), in the standand library that contains an algorithm for this solution. If you know about it, definitely mention that in an interview! The solution would be:

```python
import bisect.bisect_left

def search_insert(nums, target):
  return bisect.bisect_left(nums, target)
```

However, we still need to write the algorithm itself in an interview. Below is the [algorithm used by `bisect.bisect_left`](https://github.com/python/cpython/blob/3.8/Lib/bisect.py#L49), with minor modifications for our problem. This algorithm performs the same as Solution A.

```python
def search_insert(nums, target):
  lo = 0
  hi = len(nums)

  while lo < hi:
    mid = (lo + hi) // 2
    if nums[mid] < target:
      lo = mid+1
    else:
      hi = mid

  return lo
```
