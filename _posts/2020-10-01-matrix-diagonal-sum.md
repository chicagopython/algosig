---
title: Matrix Diagonal Sum
category:
link: https://leetcode.com/problems/matrix-diagonal-sum/
gh_comments_issue_id:
tags:
  - solved
---

## Problem

Given a square matrix `mat`, return the sum of the matrix diagonals.

```python
# Example Input
mat = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

# Example Output
25

# Explanation (note that 5 is not repeated)
1 + 5 + 9 + 3 + 7 == 25
```

## Solution

```python
def diagonal_sum(mat):
  n = len(mat)
  res = 0

  for i in range(n):
    res += mat[i][i] + mat[i][n - 1 - i]

  if n & 1:  # this "bitwise and" operation determines whether n is odd
    res -= mat[n // 2][n // 2]        

  return res

# Tests
assert diagonal_sum([[1,2,3],[4,5,6],[7,8,9]]) == 25
```
