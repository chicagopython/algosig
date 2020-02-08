---
title: Merge Two Sorted Linked Lists
link: https://leetcode.com/problems/merge-two-sorted-lists/
author:
tags:
  - sorting
  - linked list
---

## Description

Merge two sorted linked lists and return the first node of the merged list. The new list should be made by splicing together the nodes of the first two lists (don't define any new data structures like python dictionaries or python lists).

```python
# Definition for singly-linked list node
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Function Inputs
# * first node of list 1
# * first node of list 2
```

## Solution

In order to tackle this problem, we need a basic understanding of singly linked lists. A (singly) linked list is composed of nodes that are connected in a **single** direction.

<a href="https://en.wikipedia.org/wiki/Linked_list"><img class="post-img" src="{{ '/assets/img/singly-linked-list.svg' | relative_url }}" title="Wikipedia"></a>

Linked lists are very simple data structures. We can't use python list features like index slicing (`list[0:4]`) to access the values of our list. To know all the values of a linked list, we have to start at the very first node and read forward. Check out [Dan Bader's article](https://dbader.org/blog/python-linked-list) for a more thorough explanation.

The barebones linked list implementation was provided:

```python
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
```

We can make our own linked list composed of `ListNode`s:
```python
my_list = ListNode(x=1)
my_list.next = ListNode(x=3)
my_list.next.next = ListNode(x=7)
```

We can walk through each node and print its value:
```python
node = my_list
while node:
    print(node.val)
    node = node.next

>>> 1 3 7
```

And now we can approach our solution:

```python
def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    # create a blank node to start our merged list. We will add nodes to this list
    #   in increasing order.
    merged_list_node_1 = ListNode(None)

    # make a "head" that will point to the blank node_1 to start. We'll move it
    #   forward so it's always pointing to the last value of our merged list.
    head = merged_list_node_1

    while l1 and l2:
        if l1.val <= l2.val:
            # add the smaller node to our merged list
            head.next = l1
            # update l1 to refer to the next item of its list
            l1 = l1.next

        elif l2.val < l1.val:
            head.next = l2
            l2 = l2.next

        # move our head pointer forward
        head = head.next

    # finally we need to add the last node from whichever list
    #   was not empty when we broke out of the while loop above
    if l1:
        head.next = l1
    elif l2:
        head.next = l2

    # since the first item of our list is None, we return the next value
    return merged_list_node_1.next
```
