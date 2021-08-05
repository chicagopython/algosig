---
title: My Calendar
category: AlgoSIG 1
link: https://leetcode.com/problems/my-calendar-i/
author: 
gh_comments_issue_id: 98
tags:
  - intervals
---

## Description

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a *double booking*.

A *double booking* happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers `start` and `end` that represents a booking on the half-open interval `[start, end)`, the range of real numbers `x` such that `start <= x < end`.

Implement the `MyCalendar` class:

   * `MyCalendar()` Initializes the calendar object.
   * `boolean book(int start, int end)` Returns `true` if the event can be added to the calendar successfully without causing a *double booking*. Otherwise, return `false` and do not add the event to the calendar.

## Example

```python
cal = MyCalendar()
cal.book(10, 20) # return True
cal.book(15, 25) # return False, It can not be booked because time 15 is already booked by another event.
cal.book(20, 30) # return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
```


## Solution

```python
class MyCalendar:

    def __init__(self):
        pass

    def book(self, start: int, end: int) -> bool:
        pass


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

  ```
