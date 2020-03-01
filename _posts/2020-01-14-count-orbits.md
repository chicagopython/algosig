---
title: Count Orbits (Advent of Code 2019)
category: AlgoSIG 11
link: https://adventofcode.com/2019/day/6
author:
tags:
  - unsolved
---

## Description

Given a list of nodes that represent the orbits of objects in space, find the total number of orbits in the system.

For example, `G` orbits `B`, and `B` orbits `COM`. The total orbits for `G` is 2. The total for `B` is 1. The total in the system is 42. (For part 2, find the number of orbits between the two objects that two ships are orbiting.)

You can get your own input for this challenge and test your solution on [this Advent of Code page]({{ page.link }}).

Example input:
```
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
```

Graph representation:
```
        G - H      J - K - L
   	   /       	/
COM - B - C - D - E - F
           	\
            	 I
```

## Solution

