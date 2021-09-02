---
title: Course Schedule
category: AlgoSIG 2
link: https://leetcode.com/problems/course-schedule/
author: 
gh_comments_issue_id: 99
tags:
  - graphs
  - cycles
---

## Description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array prerequisites where `prerequisites[i] = [ai, bi]` indicates that you *must* take course `bi` first if you want to take course `ai`.

For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `True` if you can finish all courses. Otherwise, return `False`.

## Example

```python
# Input
numCourses = 2
prerequisites = [[1,0],[0,1]]

# Output
False

# Explanation 
# There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, 
# and to take course 0 you should also have finished course 1.
# So it is impossible.
```


## Solution

```python
def canFinish(numCourses, prerequisites):
  # Insert code here
  return False
```
