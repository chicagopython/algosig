---
title: Count Orbits (Advent of Code 2019)
category: AlgoSIG 11
link: https://adventofcode.com/2019/day/6
author: Kevin Nasto
tags:

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

```python
class Tree:

    def __init__(self, file_lines):
        self.nodes_dict = {}
        for idx, line in enumerate(file_lines):
            parent, child = line.split(')')
            self.nodes_dict[child] = parent # Backwards

    def count_parents(self, node):
        if node not in self.nodes_dict:
            return 0
        return 1 + self.count_parents(self.nodes_dict[node])

    def get_parents(self, node):
        parents = []
        while node in self.nodes_dict:
            node = self.nodes_dict[node]
            parents.append(node)
        return parents


with open('input.txt') as fh:
    lines = fh.read().split()

tree = Tree(lines)

total = 0
for node in tree.nodes_dict:
    total += tree.count_parents(node)
print(total) # Part 1

you_nodes = tree.get_parents('YOU')
san_nodes = tree.get_parents('SAN')


def a_to_b(a_nodes, b_nodes):
    b_nodes_set = set(b_nodes)
    for idx, node in enumerate(a_nodes):
        if node in b_nodes_set:
            return idx


print(a_to_b(you_nodes, san_nodes) + a_to_b(san_nodes, you_nodes))
```
