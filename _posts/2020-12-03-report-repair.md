---
title: Report Repair
category: AlgoSIG 1
link: https://adventofcode.com/2020/day/1
gh_comments_issue_id: 76
author:
tags:
  - dictionary
  - binary-search
  - brute-force
---

## Description

You are given an expense report by the Elves that looks similar to the following:

```
1721
979
366
299
675
1456
```


#### Part 1
You are told there is an error in the report and you need to **find the two entries** that sum to `2020`. In this example above, the two entries that sum to `2020` are `1721` and `299`. Then to submit the final answer to the website, you need to **multiply** the two entries together. 

#### Part 2
The Elves are grateful but now they ask you to **find three entries** that sum to `2020`. Then to submit the final answer to the website, you need to **multiply** the three entries together. 

## Solution

There are a few different solutions, each with different complexities.

```python
# Part 1 - O(n) complexity
nums = set([int(x) for x in report.splitlines()])
for num in nums:
    if (2020-num) in nums:
        print((2020-num)*num)

# Part 2 - O(n^2) complexity
for a in nums:
    for b in nums:
        if a != b:
            c = 2020-b-a
            if c in nums:
                print(a*b*c)
              
# Part 2 - O(n^3) complexity  
for a in nums:
    for b in nums:
        for c in nums:
            if a+b+c == 2020:
                print(a*b*c)
```
