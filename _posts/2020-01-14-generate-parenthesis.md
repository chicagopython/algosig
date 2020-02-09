---
title: Generate Parentheses
category: AlgoSIG 11
link: https://leetcode.com/problems/generate-parentheses/
author: Chris Luedtke
tags:
---

## Description

Given **`n`** pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given **`n = 3`**, a solution set is:
```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```


## Solution

```python
ANS = []
def recurse(s = '', n_open = 0, n_clsd = 0, n = 3) -> None:
    if len(s) == 2 * n:
        ANS.append(s)
        return
    if n_open < n:
        recurse(s + '(', n_open + 1, n_clsd)
    if n_clsd < n_open:
        recurse(s + ')', n_open, n_clsd + 1)

recurse()
print(ANS)
```
