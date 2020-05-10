---
title: Keys and Rooms
category: AlgoSIG 2
link: https://leetcode.com/problems/keys-and-rooms/
gh_comments_issue_id: 40
author:
tags:
  - Depth First Search
  - Graph
  - unsolved
participants: Adam Bain, Sree Prasad, Michael Shoemaker
---

## Description

There are N rooms and you start in room 0. Each room has a distinct number in `0, 1, 2, ..., N-1`, and each room may have some keys to access the next room.

Formally, each room *i* has a list of keys `rooms[i]`, and each key `rooms[i][j]` is an integer in `[0, 1, ..., N-1]` where `N = rooms.length`. A key `rooms[i][j] = v` opens the room with number *v*.

Initially, all the rooms start locked (except for room 0). You can walk back and forth between rooms freely.

Return `true` if and only if you can enter every room.

## Solution

``` python
class Solution:
    def canVisitAllRooms(self, rooms):
        if len(rooms) <= 1: #guard for short or empty list
            return True
        key_inventory = set([0]) # append only
        rooms_visited = set() #append

        while key_inventory - rooms_visited: # We have keys to rooms we have not seen
            chosen_room = (key_inventory - rooms_visited).pop()  #choose the room
            keys = set(rooms[chosen_room])  # visit chosen room, get keys
            key_inventory |= keys  # add keys found in  room to inventory
            rooms_visited.add(chosen_room)  # room has been visited
            if key_inventory >= set(range(len(rooms))):  # Stop once we have a key for each room
                return True 
        
        return False # We have no keys to rooms we have not seen, and we didnt have a key for each room
```

## Solution: Recursive
```python
class Solution:
    
    def __init__(self):
      self.visited = set()
      self.number_of_rooms = 0
    
    def dfs(self, rms, rm):
        if rm not in self.visited:
            print(rm)
            self.visited.add(rm)
            
            for room_key in rms[rm]:
              if room_key < self.number_of_rooms:
                self.dfs(rms, room_key)
    
    def canVisitAllRooms(self, rooms) -> bool:
        
        if rooms:
          self.number_of_rooms = len(rooms)
          self.dfs(rooms, 0)

          if len(self.visited) != self.number_of_rooms:
            return False
          
          else:
            return True

        else:
          print("No Rooms to Enter")
          return False
```
