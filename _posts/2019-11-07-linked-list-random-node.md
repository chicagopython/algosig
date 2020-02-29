---
title: Random Sample from Linked List
category:
link:
author:
tags:
  - Dynamic programming
---

## Description

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

**Follow up:** What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

## Solution

Other solutions can be found on the problem source link at the top of the post.

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
