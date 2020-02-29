---
title: Largest Area Between Points (Advent of Code 2018)
category: "AlgoSIG 3"
link: https://adventofcode.com/2018/day/6
author:
tags:
  - unsolved
---

## Description

Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y locations that are closest to that coordinate (and aren't tied in distance to any other coordinate). Your goal is to find the size of the largest area that isn't infinite.

You'll need to get your own input for this challenge from [this Advent of Code problem]({{ post.link }}).

```
# Sample input:
  1, 1
  1, 6
  8, 3
  3, 4
  5, 5
  8, 9
```

```
Point Map:  |  Point Areas:
            |
 .......... |  aaaaa.cccc
 .A........ |  aAaaa.cccc
 .......... |  aaaddecccc
 ........C. |  aadddeccCc
 ...D...... |  ..dDdeeccc
 .....E.... |  bb.deEeecc
 .B........ |  bBb.eeee..
 .......... |  bbb.eeefff
 .......... |  bbb.eeffff
 ........F. |  bbb.ffffFf
```

## Solution
