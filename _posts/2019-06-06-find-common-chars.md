---
title: Find Common Characters
category: AlgoSIG 4
link: https://leetcode.com/problems/find-common-characters/
author: Sree Prasad
tags:
  - array
---

## Description

Given an array `arr` of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates). For example, if a character occurs two times in all strings but not three times, you need to include that character two times in the final answer.

##### Example:

```python
>>> arr = ["bella","label","roller"]
>>> find_common_chars(arr)
["e","l","l"]
```

## Solution

{::options parse_block_html="true" /}

<details>
<summary markdown="span">Expand</summary>

We can use the *[Counter](https://docs.python.org/3/library/collections.html#collections.Counter)* data structure to solve this problem. A *Counter* is essentially a dictionary where the *key* corresponds to an element in the collection and the *value* corresponds to the number of times that element appears in the collection. We initialize `char_count` with the first element in `arr` then iterate through all the elements and intersect them (denoted by the `&`) with the current `char_count`.


```python
from collections import Counter

def find_common_chars(arr):
  char_count = Counter(arr[0])
  for a in arr:
    char_count = char_count & Counter(a)
  return list(char_count.elements())
```

The runtime is *O(nm)* where *n* is the number of words in the `arr` and *m* is the number of characters in a word. If you look into the implementation of *Counter* or implement something similar, you'll find that the intersection iterates through all the items in the *Counter* object (the number of character-to-count entries).

</details>

{::options parse_block_html="false" /}
