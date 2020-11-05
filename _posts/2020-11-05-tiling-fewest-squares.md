---
title: Tiling a Rectangle with the Fewest Squares
category:
link: https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/
author:
---

## Description

Given a rectangle of size `n` x `m` (both `<= 13`), find the minimum number of integer-sided squares that tile the rectangle.

```python
# Input
n = 2
m = 3

# Output
3

#  ____ ________
# |  1 |        |
# |____|   2    |
# |  1 |        |
# |____|________|
#
```

```python
# Input
n = 11
m = 13

# Output
6

#  ________________
# |  4 |  4 |      |
# |____|____|   5  |
# |       |_|______|
# |   7   |        |
# |       |    6   |
# |_______|________|
#
```

## Solution

```python
def tiling_rectangle(n, m):
  # Insert solution here

assert tiling_rectangle(2, 3) == 3
assert tiling_rectangle(11, 13) == 6
```
