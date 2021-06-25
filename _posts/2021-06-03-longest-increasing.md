---
title: Longest Increasing Subsequence
category: AlgoSIG 2
link: https://leetcode.com/problems/longest-increasing-subsequence/
author:
gh_comments_issue_id: 95
tags:
  - arrays, sorting, dynamic, trees
---

## Description

Given an integer list `nums`, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, `[3,6,2,7]` is a subsequence of the array `[0,3,1,6,2,2,7]`. Note that a subsequence may have gaps and is not contiguous. 

Example 1:
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101]
```

Example 2:
```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```


## Solution 1: Patience Sort (Solitaire Method)

![]({{ '/assets/img/solitaire.jpg' | relative_url }})

In the game of Solitaire you make piles of cards. To add a card to a pile, the rule is that it's value must be smaller than the top card of the pile. If it's not smaller, then you make a new pile (see image above).

The total number of piles is the length of the longest increasing subsequence. It may not be intuitive but writing down a few examples, you can convince yourself this is true. 

This is still `O(n^2)` time complexity because you have to through each pile every time to figure out where to put the new card.

```python
def insert_to_pile(num, piles):
    for pile in piles:
        top_card = pile[-1]
        if num <= top_card: # Append to current pile
            pile.append(num)
            return
    piles.append([num]) # Create new pile
    
def lengthOfLIS(nums):
    piles = []
    for num in nums:
        insert_to_pile(num,piles)
    return len(piles)
 ```
 
## Solution 2: Patience Sort (Binary Search)

The `O(n*log(n))` solution is using a binary search to figure which pile the card goes in. This way, we don't have to check every pile each time. To make the implementation of the binary search easier, the rest of the cards in the pile are disregarded (only the top card is kept). This also decreases the space complexity.

```python
from bisect import bisect_left
    
def insert_to_pile(num, piles):
    idx = bisect_left(piles,num)
    if idx < len(piles):
        piles[idx] = num
    else:
        piles.append(num)
```

## Solution 3: Dynamic Programming (Table)

The conventional solution to this problem is the dynamic programing approach which is `O(n^2)`. We need to keep a table (just a list) that counts the longest increasing subsequence so far. When we get to a new element, we need to check every single previous count in the table. We need to add 1 to the maximum count, only if new element's value is greater (which means the sequence is increasing).

```python
def get_max(nums,array):
    cur_idx = len(array) # The new element's index we are checking
    try:
        array.append(1 + max([count for num,count in zip(nums,array) if num < nums[cur_idx]]))
    except ValueError: # If none of the previous elements are smaller
        array.append(1)
            
def lengthOfLIS(nums):
    array = []
    for num in nums:
        get_max(nums,array)
    return max(array)
```

## Solution 4: Dynamic Programming (Tree with Memoization)

We can also make a tree for this problem. The children at each node are the previous values, but only the ones smaller than the node (which is the current element). This solution is `O(n^2)` with memoization and `O(2^n)` without, which is the brute force solution.

```python
def recurse(nums,idx,table):
    
    if idx in table:
        return table[idx]
    
    counts = []
    for child_idx in range(idx+1, len(nums)):
        if nums[child_idx] > nums[idx]:
            counts.append(1 + recurse(nums,child_idx,table))
            
    if counts:    
        max_count = max(counts)
    else:
        max_count = 1
    table[idx] = max_count
    return max_count
    
    
def lengthOfLIS(self, nums):
    table = {}
    return max([recurse(nums,idx,table) for idx in range(len(nums))])
```
