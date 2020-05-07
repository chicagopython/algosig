---
title: Cheapest Flights With K Stops
category: AlgoSIG 2
link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
author: Kevin Nasto
gh_comments_issue_id: 39
tags:
  - Graph
  - unsolved
---

## Description

There are *n* cities connected by *m* flights. Each flight starts from city *u* and arrives at *v* with a price *w*.

Now given all the cities and flights, together with starting city *src* and the destination *dst*, your task is to find the cheapest price from *src* to *dst* with up to *K* stops. If there is no such route, output `-1.`

```Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200```

```Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500```
