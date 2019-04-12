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

# 2. Problem Solution
## The naive approach
The straightforward but naive approach involves checking from the beginning version `1` to the end version `n`, until we find a ba
d version. However, when considering large inputs, or more specifically when `n` is an extremely large integer, this approach could possibly take a lot time to finish (think of cases where `n` is a billion and the first bad version is in the `nth` position).

## Using binary search
Binary search is a searching algorithm on sorted arrays where the search area is cut in half after each iteration. If `n = 8`, aft
er first search `n = 4`, after second search `n = 2`, and lastly after third search `n = 1`, where `n` represents the search area
(length of array, integer size, ...etc).

Binary search is cool and all, but why should we use it here? Going back to the problem, there is one important phrase that makes it the perfect candidate.
> Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

We can state this phrase as such **if version is bad then remaining versions are also bad**.
This single statement will be the foundation to build our logic on. Generally speaking, the statement will allow us to determine w
hich half to search next. This should start making more sense once we dive into the logic.

#### logic
Assume `n = 15` and first bad version is `3`
*recursive loop*
* find middle version i.e. (mid = 8 when n = 15)
* if middle version is a good version
  * Search the remaining half i.e. `(9..15)`. There's no need to worry about the first half because if we had a bad version prior
to current mid version, then by the statement above, the mid version should also be a bad version.
* if middle version is a bad version
  * Search the left half i.e. `(1..7)`. We care about the first bad version, and checking the remaining bad versions don't help to
 achieve that.

Eventually, we'll reach a point where we've exhausted the search to 1 version let's say `v` (in our case 2). We can at this point return the right boundary plus 1. This works because of how we search. If current middle version is bad, then we search the left half by resetting the right boundary to the current middle position minus 1, If the current middle version is good, then we search the right half by resetting the left boundary by current middle position plus 1.

Regardless of whether the last version is bad version or not, we've recorded the earliest bad version's position when we reevaluated the right boundary. We need to add 1 to the right boundary to offset the minus 1 during reevaluation of the right boundary.


```python
from math import floor

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n

        while (l <= r):
            mid = floor((r - l) / 2) + l

            if isBadVersion(mid):
                r = mid - 1
            else:
