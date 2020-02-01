---
title: Random Sample from Linked List
category: AlgoSIG 1
link:
author:
tags: Dynamic programming
---

# 1. Problem Link

The problem can be found [here](https://leetcode.com/problems/valid-anagram/)


# 2. Problem Description

Given two sequences, *x[1:m]* and *y[1:n]*,
find a longest sequence common to both. Uses memoization
to store intermediate results so comparisons between same
string indices are not duplicated

BASE CASE:
There are no letters in one string to compare

CASE 1:
The last letter of P and Q are the same

CASE 2:
The last letter of P and Q are different


# 3. Problem Solution


Other solutions can be found on the LeetCode link above.

```python
class ReservoirSampling(object):

    def __init__(self, max_size):
        self.reservoir = []
        self.max = max_size
        self.i = 0

    def add(self, element):
        size = len(self.reservoir)

        if size >= self.max:
            spot = random.randint(0, self.i - 1)
            if spot < size:
                self.reservoir[spot] = element

        else:
            self.reservoir.append(element)

        self.i += 1
```
