---
title: Implement a Prefix Tree (Trie)
slug: implement-a-prefix-tree-trie
date: 2019-04-04 00:00:00 UTC-05:00
tags: trie, tree, autocomplete
category: "AlgoSIG 2"
link: 
description: 
type: text
author: "Kevin Nasto"
---

<img src="/assets/img/trie.png">

# Description

The problem can be found [here](https://leetcode.com/problems/implement-trie-prefix-tree/)

Implement a trie (prefix tree) with `insert`, `search`, and `startsWith` methods. Tries are used in many applications such as spell checking, autocompletion, and ip routing.

*Part 2* of this problem (not shown on LeetCode) is to implement an `autoComplete` method.

# Solution 1: Using Node Class and Storing Entire Word at Leaf

This solution uses a `Node` class which makes things easier to keep track of. Storing the entire word in the end of word seperator makes the implementation less tricky. However this unfortunetly causes the space complexity to be `O(n)` where `n` is the number of words.

```python
class Node:

    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node('root')

    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node(letter)
            node = node.children[letter]
        node.end = word
        
    def search(self, word):
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False
        if node.end:
            return True
        else:
            return False

    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False
        return True

    def autocomplete(self, word):
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return []
        words = []
        autocomplete_helper(node, words)
        return words


def autocomplete_helper(node, words):
    if node.end:
        words.append(node.end)
        return
    for child in node.children:
        autocomplete_helper(node, words)
```

# Solution 2: Using Just Dictionary and End of Word Marker $

Since this only stores the letters, and not the entire word, the space complexity is much less.

```python
class Trie:

    def __init__(self):
       self.root = {}
        
    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['$'] = {} # End of word
        
    def search(self, word):
        node = self.root
        for letter in word:
            if letter in node:
                node = node[letter]
            else:
                return False
        if '$' in node:
            return True
        else:
            return False
        
    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            if letter in node:
                node = node[letter]
            else:
                return False
        return True

    def autoComplete(self, prefix):
        node = self.root
        for letter in prefix:
            if letter in node:
                node = node[letter]
            else:
                return []
        words = []
        autocomplete_helper(prefix, words, node)
        return words


def autocomplete_helper(parent, words, node):
    if '$' in node:
        words.append(parent)
    for letter in node:
        print_tree(parent + letter, words, node[letter])
```

# Test Code and Benchmarking

```python
trie = Trie()
trie.insert('cat')
trie.insert('can')
trie.insert('and')
trie.insert('ant')
trie.insert('antenna')

print(trie.autocomplete('an'))
```

Using a list of 8000 most frequently searched words, here are some benchmarks.

```
77848 Bytes using python list
1184  Bytes using above trie

Input: p
Trie:  4.71 ms
List:  4.28 ms

Input: cat
Trie: 0.25 ms
List: 5.19 ms

Input: python
Trie:  0.05 ms
List:  7.81 ms
```


