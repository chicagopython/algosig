---
title: Water Bottles
category:
link: https://leetcode.com/problems/water-bottles/
author:
tags:
  - unsolved
---

## Description

Given `numBottles` of full water bottles, you can exchange `numExchange` empty water bottles for one full water bottle.
The operation of drinking a full water bottle turns it into an empty bottle.
Return the maximum number of water bottles you can drink.

For example:
If you are given `numBottles=9` full bottles and `numExchange=3`, the maximum number of water bottles you can drink
is **13**.

1. Drink 9 full bottles (9 drank)
2. Exchange 9 empty bottles for 3 full bottles (9 drank)
3. Drink 3 full bottles (12 drank)
4. Exchange 3 empty bottles for 1 full bottle
5. Drink 1 full bottle (13 drank)

Since there aren't enough bottles left to exchange, the maximum number of bottles that can be drank here is **13**.

## Solution

```python
def maxDrinkable(self, numBottles: int, numExchange: int) -> int:

```
