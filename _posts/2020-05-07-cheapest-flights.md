---
title: Cheapest Flights With K Stops
category: AlgoSIG 2
link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
author: Kevin Nasto
gh_comments_issue_id: 39
tags:
  - Graph
---

## Description

There are *n* cities connected by *m* flights. Each flight starts from city *u* and arrives at *v* with a price *w*.

Now given all the cities and flights, together with starting city *src* and the destination *dst*, your task is to find the cheapest price from *src* to *dst* with up to *K* stops. If there is no such route, output `-1.`

```
Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
```

```
Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
```

## Solution 1 Recursive With Memoization

```python
from collections import defaultdict


def get_node(name, value):
    return {'id':name, 'cost':value}


def recurse(node_id, tree, k, dest, visited):

    key = (node_id,k)
    if key in visited:
        return visited[key]

    if node_id == dest:
        return 0

    if k < 0:
        return float('inf')

    children = tree[node_id]

    if not children:
        return float('inf')

    results = []
    for child in tree[node_id]:
        results.append(child['cost'] + recurse(child['id'], tree, k-1, dest, visited))

    visited[key] = min(results)
    return visited[key]


def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    tree = defaultdict(list)
    for edge in flights:
        node_id = edge[0]
        child = get_node(edge[1], edge[2])
        tree[node_id].append(child)

    visited = {}
    result = recurse(src,tree, K, dst, visited)
    if result == float('inf'):
        return -1
    else:
        return result
```
