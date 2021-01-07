---
title: Seating System
category: AlgoSIG 3
link: https://adventofcode.com/2020/day/11
author:
gh_comments_issue_id: 82
tags:
  - Grid, Conway
---

## Description

You are given a grid representing seats on an airplane. You are trying to model which seats will be occupied or empty.

Each symbol represent an empty seat, occupied seat, or no seat which is the floor as shown below.

```
Empty seat    (L)
Occupied seat (#)
No seat       (.)
```

The grid looks like the following.

```
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
```

All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously.


- If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
- If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
- Otherwise, the seat's state does not change

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied? (Answer in the above example is 37).


### Part 2

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats.

```
.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
```

The following is the same grid as above except with the direction and first seat highlighted.

| ![]({{ '/assets/img/seats.png' | relative_url }}) | I am text to the right |



## Solution by your_name_here

```python
# Insert solution here
```
