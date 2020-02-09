---
title: Merge Sort
category: AlgoSIG 6
link:
author: Chris Luedtke
tags:
---

## Description

Implement merge sort, an efficient "divide and conquer" approach to sorting.
1. split the array in half
1. merge-sort each half
1. combine each sorted half

Sample input:

```python
merge_sort([ 5, 4, 6, 2, 1,])

>>> [1, 2, 4, 5, 6]
```

## Solution

```python
def merge(arr_a, arr_b):  # helper function
    merged_arr = []
    while len(arr_a) > 0 and len(arr_b) > 0:
        if arr_a[0] <= arr_b[0]:
            merged_arr.append(arr_a.pop(0)) # O(k)
        else:
            merged_arr.append(arr_b.pop(0))

    return merged_arr + arr_a + arr_b


def merge_sort(arr):  # O(n * log(n))
    if len(arr) < 2:
        return arr

    mid_i = len(arr) // 2
    left, right = merge_sort(arr[:mid_i]), merge_sort(arr[mid_i:])

    return merge(left, right)
```
