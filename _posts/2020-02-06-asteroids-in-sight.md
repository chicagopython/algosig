---
title: Asteroids In Sight
link: https://adventofcode.com/2019/day/10
author: Kevin Nasto
tags:
  - grid
  - math
---

## Description

Find the asteroid (denoted by `#`) that has the maximum number of other asteroids in its “line of sight”. The input file looks like the following:
```
Input File:
.#..#
.....
#####
....#
...##
```

Below, the highlighted asteroid (denoted by `0`) is the answer with *eight* in sight. The top left one `L` is blocked (by the asteroid denoted by `X`), but all others are in its sight. Notice the top right asteroid is in sight. Hint: Find the slope or angle.

```
.L..#
.....
##X##
....#
...0#
```

The following denotes how many asteroids are visible at each location.

```
.7..7
.....
67775
....7
...87
```

![image tooltip here](/assets/img/trie.png)

For more information on the problem check out the problem source on advent of code linked above or the problem slide [here.](https://docs.google.com/presentation/d/1FhnQGN0AzcDZL7ZaSnnj-PCvJYLDAOhQ-v7GphZzZnc/edit#slide=id.g61f898af63_0_0)

## Solution

For the solution we need to find the slope given by ```slope = y_diff/x_diff = (y2-y1)/(x2-x1)```. Unfortunately because the slope does not tell us which direction the asteroid is coming from, need to look at the sign of *y_diff* and *x_diff* to tell us which quadrant it's pointing from.

```python
def print_grid(selection=(-1,-1)):
    '''For debugging'''
    for y, line in enumerate(GRID):
        for x, char in enumerate(line):
            point = (y,x)
            if selection == point:
                print('@', end='')
            else:
                print(char, end='')
        print()


def get_char(point):
    y, x = point
    return GRID[y][x]


def get_asteroids():
    asteroids = []
    for y in range(y_max):
        for x in range(x_max):
            point = (y,x)
            if get_char(point) == '#':
                asteroids.append(point)
    return asteroids


def calculate_slope(y_diff, x_diff):
    if x_diff >= 0:
        if y_diff >= 0:
            quadrant = 1
        else:
            quadrant = 0
    else: # negative x
        if y_diff < 0:
            quadrant = 3
        else: # positive y
            quadrant = 2
    try:
        return y_diff / x_diff, quadrant
    except ZeroDivisionError:
        return -float('inf'), quadrant


def get_slope_and_direction(station, asteroid):
    y1, x1 = station
    y2, x2 = asteroid
    y_diff = y2 - y1
    x_diff = x2 - x1
    return calculate_slope(y_diff, x_diff)


with open('input.txt') as fh:
    text = fh.read().strip()

GRID = text.splitlines()
y_max = len(GRID)
x_max = len(GRID[0])

asteroids = set(get_asteroids())

asteroids_per_station = []

for station in asteroids:
    station_slopes = set()
    for asteroid in asteroids:
        if station == asteroid:
            continue
        slope_and_direction = get_slope_and_direction(station, asteroid)
        station_slopes.add(slope_and_direction)
    #print(station_slopes)
    asteroids_per_station.append((len(station_slopes), station))

print(max(asteroids_per_station))
```

### Solution using Angle

From the formula ```tan(theta) = slope = y_diff/x_diff``` we can get ```theta = atan(y_diff/x_diff)```. However there is the `atan2()` in python which avoids the divide by zero argument and keeps track of the sign for you ```theta = atan2(y_diff, x_diff)```

```python
def calculate_slope(y_diff, x_diff):
    from math import atan2
    return atan2(y_diff, x_diff)
```

### Time and Space Complexity
```O(n^2)``` where `n` is the number of asteroids, since for each asteroid we are looking at all the other asteroids. For space it's ```O(n)``` since we are only keeping how many can we see for each asteroid.
