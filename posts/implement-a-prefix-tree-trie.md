<!--
.. title: Implement a Prefix Tree (Trie)
.. slug: implement-a-prefix-tree-trie
.. date: 2019-04-15 21:10:03 UTC-05:00
.. tags: trie, tree, autocomplete
.. category: 
.. link: 
.. description: 
.. type: text
-->

<img src="/assets/img/trie.png">

# 1. Problem Link

The problem can be found [here](https://leetcode.com/problems/implement-trie-prefix-tree/)

# 2. Problem Description

Implement a trie (prefix tree) with `insert`, `search`, and `startsWith` methods. Tries are used in many applications such as spell checking, autocompletion, and ip routing.

*Part 2* of this problem (not shown on LeetCode) is to implement an `autoComplete` method.

# 3. Solution Using Node Class and Storing Entire Word at Leaf

This solution uses a `Node` class which makes things easier to keep track of. Storing the entire word in the end of word seperator makes the implementation less tricky. However this unfortunetly causes the space complexity to be `O(n)` where `n` is the number of words.

{{% listing trie1.py python %}}

# 4. Solution Using Just Dictionary and End of Word Marker $

Since this only stores the letters, and not the entire word, the space complexity is much less.

{{% listing trie2.py python %}}

# 5. Test Code and Benchmarking

```
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


