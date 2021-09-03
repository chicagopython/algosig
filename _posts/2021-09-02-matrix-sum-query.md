---
title: Matrix Sum Query
category: AlgoSIG 2
link: https://leetcode.com/problems/range-sum-query-2d-immutable/
author: 
gh_comments_issue_id: 100
tags:
  - matrix
---

## Description

Given a 2D matrix `matrix`, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its **upper left corner** `(row1, col1)` and **lower right corner** `(row2, col2)`.

![]({{ '/assets/img/sum-grid.jpg' | relative_url }})


## Solution (by @librohew)

```python
def sumRegion(row1, col1, row2, col2):
  # Insert code here
  runerSum = 0
  for x in range(row1, row2+1):
    runerSum += addWithinRows(x, col1, row2, col2)
    print('runerSum',runerSum)
  return runerSum

def addWithinRows(row1, col1, row2, col2):
  # add matrix[row1][col1] and the next (col2 - row2)^{th} elts to the right
  sumr = 0
  # do col2 - row1 - 1 additions
  for x in range(abs(col2 - col1) + 1):
    print("row:" + str(row1) + "\n" + "col:" + str(col1 + x) +  "\nVAL:" +str(matrix[row1][col1 + x]))
    sumr += matrix[row1][col1 + x]
  return sumr
```
