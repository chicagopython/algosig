---
title: Complete the Max Heap
category: AlgoSIG 7
link:
author: Chris Luedtke
tags:
---

# Description

Given a partial object representation of a **Max Heap** (below), complete the `insert` and `delete` methods.

**Max Heap** are binary tree data structures implemented as an array.

1. each node is greater than each of its children
1. the tree is balanced
1. all leaves are in the leftmost position available

The storage of heaps are implemented as arrays. This allows us to take advantage of constant-time access to any element in the heap. Given a parent node's index value, `i`, the parent's left child index is `2i + 1`, and its right child index is `2i + 2`. Conversely, a node's parent is located at index `floor((i - 1) / 2)`.

To get a better understanding of heaps and how they work, study the images below and experiment with this [Min Heap annimation](https://www.cs.usfca.edu/~galles/JavascriptVisual/Heap.html).

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Max-Heap.svg/1280px-Max-Heap.svg.png)


```python
class MaxHeap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        if not self.storage:
            return None
        elif len(self.storage) == 1:
            return self.storage.pop()
        else:
            top = self.storage[0]
            self.storage[0] = self.storage.pop()
            self._sift_down(0)
            return top

    def _bubble_up(self, index):
        # TODO

    def _sift_down(self, index):
        # TODO
```

# Solution

```python
class MaxHeap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        if not self.storage:
            return None
        elif len(self.storage) == 1:
            return self.storage.pop()
        else:
            top = self.storage[0]  # store top heap value so we can return it
            self.storage[0] = self.storage.pop()
            self._sift_down(0)
            return top

    def get_max(self):
        if self.storage:
            return self.storage[0]
        else:
            return None

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while index > 0:
            # compare to parent
            parent_i = (index - 1) // 2  # floor division

            if parent_i < 0:
                break

            if self.storage[parent_i] < self.storage[index]:
                self.storage[index], self.storage[parent_i] = \
                    self.storage[parent_i], self.storage[index]  # swap

                index = parent_i
            else:
                break

    def _sift_down(self, index):
        end_i = len(self.storage) - 1
        l_i = 2 * index + 1

        while l_i <= end_i:
            r_i = l_i + 1

            if (r_i <= end_i and self.storage[l_i] < self.storage[r_i]):
                swap_i = r_i
            else:
                swap_i = l_i

            if self.storage[index] < self.storage[swap_i]:
                self.storage[index], self.storage[swap_i] = \
                    self.storage[swap_i], self.storage[index]  # swap

                index = swap_i
                l_i = 2 * index + 1
            else:
                break
```
