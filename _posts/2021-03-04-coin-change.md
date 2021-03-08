---
title: Coin Change
category: AlgoSIG 2
link: https://leetcode.com/problems/coin-change/solution/
author:
tags:
  - Dynamic
---

## Description
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

```python
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

```python
Input: coins = [2], amount = 3
Output: -1
```

```python
Input: coins = [1], amount = 0
Output: 0
```

```python
Input: coins = [1], amount = 1
Output: 1
```

```python
Input: coins = [1], amount = 2
Output: 2
```

## Solution your_name_here


```python
from functools import lru_cache
from typing import List
class Solution:
    def coinChange(self,coins: List[int], amount: int) -> int:
        
        @lru_cache
        def recurse(amount:int)->int:
            ans=amount+1
            if amount==0:
                return 0
            for c in coins:
                if amount>=c:
                    left=recurse(amount-c)
                    if left!=-1:
                        ans=min(ans,left+1)

            if ans==amount+1: ans=-1
            return ans

        return recurse(amount)

```
