---
title: Earliest Ancestor in Family Tree
category:
author:
gh_comments_issue_id: 62
---

## Problem

Suppose we have input data describing a graph of relationships between parents and children over multiple generations.

Given an individual's ID, `i`, and a list of (parent, child) pairs, `edges`, write a function that returns the individual's earliest known ancestor (the one at the farthest distance from the input individual). If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return `-1`.

For example, in this diagram and the example input below, `3` is a child of `1` and `2`, and `5` is a child of `4`:

```
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
```


```
Example input
  6

  [( 1, 3),
   ( 2, 3),
   ( 3, 6),
   ( 5, 6),
   ( 5, 7),
   ( 4, 5),
   ( 4, 8),
   ( 8, 9),
   (11, 8),
   (10, 1)]

Example output
  10
```

Clarifications:
* The input will not be empty.
* There are no cycles in the input.
* There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
* IDs will always be positive integers.
* A parent may have any number of children.

## Solution

```python
def earliest_ancestor(i, edges):
  return

assert earliest_ancestor(
  6,
  [
    (1, 3),
    (2, 3),
    (3, 6),
    (5, 6),
    (5, 7),
    (4, 5),
    (4, 8),
    (8, 9),
    (11, 8),
    (10, 1)
  ]
) == 10
```
