---
title: Longest Common Prefix
link: https://leetcode.com/problems/longest-common-prefix/
author:
tags:
  - unsolved
---

## Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

Example 1:
```
Input: ["flower","flow","flight"]
Output: "fl"
```

Example 2:
```
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

Note: all given inputs are in lowercase letters `a-z`.

## Solution

```python
def lcp(input):
    out = ''
    for tuple in zip(*input):
        char = tuple[0]
        if all(map(lambda x: x == char, tuple)):
            out += char
        else:
            break
```
    return out
