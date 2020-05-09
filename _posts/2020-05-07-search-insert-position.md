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

#Solution from Joanna Raygoza
from typing import List


def search_insert(nums:List[int], target:int) -> int:
	count = 0
	while count <= len(nums)-1 and nums[count] < target:
		count += 1
	return count

# tests
assert search_insert([1,3,5,6], 5) == 2
assert search_insert([1,3,5,6], 2) == 1
