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



## Solution

```python
grid = []
for line in grid_text.splitlines():
    if not line:
        continue
    grid.append(list(line))


def get_adj_seats(point):
    occupied = 0
    print(point)
    (y,x) = point
    for dy in (-1,0,1):
        for dx in (-1,0,1):
            if not dy and not dx: # Skip (0,0)
                continue
            y_adj = y + dy
            x_adj = x + dx
            if y_adj >= len(grid):
                continue
            if x_adj >= len(grid[0]):
                continue
            if y_adj < 0:
                continue
            if x_adj < 0:
                continue
            if grid[y_adj][x_adj] == '#':
                occupied += 1
    return occupied

def next_state():
    changes = {}
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            point = (y,x)
            seat = grid[y][x]
            num_occupied = get_adj_seats(point)
            print(num_occupied)
            if seat == 'L':
                if num_occupied == 0:
                    changes[point] = '#'
            if seat == '#':
                if num_occupied >= 4:
                    changes[point] = 'L'
    if not changes:
        return False
    for point in changes:
        (y,x) = point
        grid[y][x] = changes[point]
    return True

while next_state():
    pass

num_seats = 0
for row in grid:
    print(''.join(row))
    for seat in row:
        if seat == '#':
            num_seats+=1
print(num_seats)
```
