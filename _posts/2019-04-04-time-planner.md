---
title: Time Planner
category: AlgoSIG 2
link:
author: Chris Luedtke
tags: array, python-101
---

# Description

Implement a time planner that receives the availability of two people, a and b, and a duration, dur. Return the earliest time slot in which both people can meet. If no satisfactory time exists, return None.

You may assume availabilities are sorted.

Example:
```python
a = [(10, 50), (60, 120), (140, 210)]
b = [(0, 15), (60, 70)]
dur = 8

>>> (60, 68)
```

# Solution 1: `O(n^2)`

```python
def time_planner(a, b, dur):
  for avail_a in a:
    for avail_b in b:
      overlap = set(range(*avail_a)) & set(range(*avail_b))

      if len(overlap) >= dur:
        overlap = sorted(list(overlap))

        return (overlap[0], overlap[0] + dur)

  return None
```

# Solution 2: `O(n)`

```python
def time_planner(a, b, dur):
  i_a, i_b = 0, 0

  while i_a < len(a) and i_b < len(b):
    start = max(a[i_a][0], b[i_b][0])
    end = min(a[i_a][1], b[i_b][1])

    if start + dur <= end:
      return start, start + dur

    if a[i_a][1] < b[i_b][1]:
      i_a += 1
    else:
      i_b += 1

  return None
```
