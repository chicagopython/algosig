---
title: Escape a Large Maze
category:
link: https://leetcode.com/problems/escape-a-large-maze/
author:
gh_comments_issue_id: 61
---

## Description

We start at the `source` (denoted as `S` below) square and want to reach the `target` square (denoted as `T`). Each move, we can walk to a 4-directionally adjacent square in the grid that isn't in the given list of `blocked` squares (denoted as `#`).

```
############
#....#....S#
#.....#....#
#......#...#
#.......#..#
#........#.#
#T........##
############
```

The grid size is **1 million by 1 million** and the maximum number of blocked squares is **200**. (You cannot go past the edge of the grid or where the coordinates are negative numbers.)

Return `True` if and only if there is a path otherwise return `False`

```python
# Input
blocked = [[0,1],[1,0]]
source = [0,0]
target = [0,2]

# Output is False
```

## Solution by your_name_here

```python
def get_children(point):
    children = []
    y, x = point
    size_y, size_x = (1000000, 1000000)
    
    if y-1 >= 0:
        children.append((y-1, x))
    
    if x-1 >= 0:
        children.append((y,x-1))
        
    if y+1 <= size_y:
        children.append((y+1,x))
        
    if x+1 <= size_x:
        children.append((y,x+1))
        
    return children


def bfs(source, target, is_blocked):
    queue = []
    marked = set()

    queue.append((source,1))
    marked.add(source)

    while queue:

        node_id, depth = queue.pop(0)
        
        if depth > 200:
            return True

        for child_id in get_children(node_id):

            if child_id in is_blocked:
                continue

            if child_id == target:
                return True

            if child_id not in marked:
                queue.append((child_id,depth+1))
                marked.add(child_id)

    return False
    


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        is_blocked = set()
        for item in blocked:
            is_blocked.add(tuple(item))
            
        target = tuple(target)
        source = tuple(source)
        
        if bfs(source, target, is_blocked) and bfs(target,source,is_blocked):
            return True
        
        return False```
