---
title: Carpooling
category: AlgoSIG 2
link: https://leetcode.com/problems/car-pooling/
author: Sand Ip, Yuliana Sari (SolutionOne), Emily Ekdahl (SolutionTwo)
tags:
  - Greedy
---

## Description

You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

Example 1:
```python
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
```

Example 2:
```python
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
```

Example 3:
```python
Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
```

Example 4:
```python
Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
```

## Solution

Other solutions can be found on the problem source link at the top of the post.

```python
class SolutionOne:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pool = defaultdict(int)
        for val, start, end in trips:
            pool[start] += val
            pool[end] -= val
        
        current = 0
        for location in sorted(pool.keys()):
            current += pool[location]
            if current > capacity:
                return False
        return True

class SolutionTwo:
   def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
      milesDict = {}

      for trip in trips:
        passengers = trip[0]
        start = trip[1]
        end = trip[2]

        mile = start

        while mile < end:
          if mile in milesDict:
            milesDict[mile] = milesDict[mile] + passengers
          else:
            milesDict[mile] = passengers

          mile = mile + 1

      if max(milesDict.values()) <= capacity:
        return True
      else:
        return False
  ```
