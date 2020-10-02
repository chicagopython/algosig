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
def diagonal_sum(A):
  N = len(A)
  res = 0
  for i in range(N):
      res += A[i][i] + A[i][N - 1 - i]
  if N & 1:
      res -= A[N // 2][N // 2]        
  return res

# Tests
assert diagonal_sum([[1,2,3],[4,5,6],[7,8,9]]) == 25
```
