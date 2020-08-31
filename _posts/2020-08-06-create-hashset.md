---
title: Create a hashset
category: AlgoSIG 2
link: https://leetcode.com/problems/design-hashset/
gh_comments_issue_id: 40
author:
tags:
  - Hash Table
  - Design
participants: 
---

## Description

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

1. add(value): Insert a value into the HashSet. 
2. contains(value) : Return whether the value exists in the HashSet or not.
3. remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Notes:
+ All values will be in the range of [0, 1000000].
+ The number of operations will be in the range of [1, 10000].
+ Please do not use the built-in HashSet library.

## Solution

``` python
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def add(self, key: int) -> None:
        

    def remove(self, key: int) -> None:
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

class MyHashSet:

    def __init__(self):
      """
      Initialize your data structure here.
      """
      self.capacity = 101
      self.my_list = [None for i in range(self.capacity)]    
      self.count = 0

    def add(self, key: int):
      index=self.my_hash(key)
      if self.my_list[index] is None:
        self.my_list[index] = [key]
      elif key not in self.my_list[index]:
            self.my_list[index].append(key)
      self.count += 1  

    def remove(self, key: int):
      index=self.my_hash(key)
      sub_list = self.my_list[index]
      if key in sub_list:
        sub_list.remove(key)
        return True
      else:
        return False

    def contains(self, key: int):
      # """
      # Returns true if this set contains the specified element
      # """
      index=self.my_hash(key)
      sub_list = self.my_list[index]
      if sub_list:        
        return key in sub_list
      else: 
        return False        


    def my_hash(self, key: int):
      index = key % self.capacity
      return index

# Your MyHashSet object will be instantiated and called as such:
obj2 = MyHashSet()
obj2.add(1)
print(obj2.my_list)
obj2.remove(1)
print(" ")
print(obj2.my_list)

obj2.add(3)
print("contains 3:", obj2.contains(3))  # should be True
print(" ") 
print("contains 2:", obj2.contains(2))  # should be False
```
