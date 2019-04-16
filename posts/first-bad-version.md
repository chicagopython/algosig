<!--
.. title: First Bad Version
.. slug: first-bad-version
.. date: 2019-03-31 00:00:00 UTC-05:00
.. tags: array, binary-search
.. category: 
.. link: 
.. description:
.. type: text
-->

# 1. Problem Link

The problem can be found [here](https://leetcode.com/problems/first-bad-version/)


# 2. Problem Description

You have *n* versions *1,2,3,...,n* and you want to find the first one that broke the code.

You are given a function `isBadVersion(version)` which will return `True` if the version is greater or equal to first broken version. Otherwise it return `False`.

**Part 2** of this problem (not shown on LeetCode) is to solve without knowing in advance how many versions *n* you have to check. 

# 3. Problem Solution

This solution is for **Part 2**, solved without knowing the total number of versions *n*. Instead of finding the midpoint between the current value and the last, the index of the current is multiplied by 2.

Other solutions can be found on the LeetCode link above.

{{% listing part2_without_n.py python linenumbers=True %}}
