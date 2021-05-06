---
title: Reverse String In Place
category: AlgoSIG 1
link: https://leetcode.com/problems/reverse-string/
gh_comments_issue_id: 85
tags:
  - strings, arrays
---

## Description

Write a function that reverses a string. The input string is given as list of letters.

Do not create a new list, you must do this by modifying the input list in-place with O(1) extra memory. 

Can you do it using a loop? Can you do it recursively?

```
Input: ['H','e','l','l','o']
Output: ['o','l','l','e','H']
```


## Iterative Solution

```python
# Insert solution here
length = len(s)-1

for i in range(0,length-1):
  s[i], s[length-i] = s[length-i], s[i]
```

## Recursive Solution

```python
def helper(s, left_idx, right_idx):
    if left_idx >= right_idx:
        return
    temp = s[left_idx]
    s[left_idx] = s[right_idx]
    s[right_idx] = temp
    helper(s, left_idx + 1, right_idx - 1)
```
