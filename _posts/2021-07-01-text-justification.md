---
title: Text Justification
category: AlgoSIG 3
link: https://leetcode.com/problems/text-justification/
author:
gh_comments_issue_id: 96
tags:
  - arrays, strings
---

## Description

Given a list `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

* Each line must be exactly `maxWidth` characters
* Spaces must be evenly distributed from left to right
* Very last line of text should not be justified!

#### Example 1
```python
# Input
words = ["This", "is", "a", "justification", "of", "example", "text", "and", "words."]
maxWidth = 15

# Output
[ 
    "This    is    a",  # Most lines end with letters
    "justification  ",  # unless it's a single word
    "of example text",
    "and words.     "   # Also notice last line is normal and not justified
]
```

#### Example 2

```python
# Input
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

# Output
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```


## Solution

```python
def fullJustify(words, maxWidth):
  output = []
  return output

  ```
