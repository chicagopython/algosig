---
title: Crossed Wires
category: AlgoSIG 10
link:
author: Kevin Nasto
tags:
  - Dynamic programming
---

# 1. Problem Link

The problem can be found [here](https://adventofcode.com/2019/day/3)


# 2. Problem Description

Given a list of wires that _cross_ (intersect), find the closest intersection point to start of the wire. All wires start at the same point. A wire CANNOT intersect with itself. A wire is defined by a string in a file representing steps. See link for description of PART 2.

```
...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
```

```
...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
```

Input File:
```
R8,U5,L5,D3
U7,R6,D4,L4
```

# 3. Problem Solution


Other solutions can be found on the LeetCode link above.

```python
def get_char(point, wires):

    if point == ORIGIN:
        return 'o'

    intersections = 0

    for wire in wires:
        if point in wire:
            intersections += 1
            continue
        if intersections == 2:
            return 'X'

    if not intersections:
        return '.'
    else:
        return '*'


def print_grid(wires):
    y,x = ORIGIN
    x -= SIZE
    y -= SIZE
    for i in range(SIZE*2):
        for j in range(SIZE*2):
            point = (y+i,x+j)
            print(get_char(point, wires), end='')
        print()


def get_distance(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def get_wire_points(moves):

    y, x = ORIGIN
    points = []

    for move in moves:
        way = move[0]
        steps = int(move[1:])

        for i in range(steps):

            if way == 'R':
                x += 1
            elif way == 'U':
                y -= 1
            elif way == 'D':
                y += 1
            elif way == 'L':
                x -= 1
            else:
                raise Exception(way)

            points.append((y,x))

    return points


def get_wires(file_lines):
    wires = []
    for moves in file_lines:
        moves = moves.split(',')
        wire = get_wire_points(moves)
        wires.append(wire)
    return wires


def get_exes(wires):
    exes = []
    seen = set()
    for wire in wires:
        for point in set(wire): # Making sure it doesnt intersect with itself
            if point in seen:
                exes.append(point)
            else:
                seen.add(point)
    return exes

def find_step(ex, wire):
    for num, point in enumerate(wire, start=1):
        if ex == point:
            return num
    return 0


def find_steps(ex, wires):
    steps = 0
    for wire in wires:
        if ex in wire: # Ineffecient, should use set here
            steps += find_step(ex, wire)
    return steps


ORIGIN = (0,0)
SIZE = 15


with open('input.txt') as fh:
    lines = fh.read().splitlines()


wires = get_wires(lines)
exes = get_exes(wires)

print('Part 1')
print(min([get_distance(ex, ORIGIN) for ex in exes]))

print('\nPart 2')
print(min([find_steps(ex, wires) for ex in exes]))

```
