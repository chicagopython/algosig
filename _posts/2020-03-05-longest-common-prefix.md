---
title: Longest Common Prefix
link: https://leetcode.com/problems/longest-common-prefix/
date: 2020-03-05 14:40:47
author: Kevin Nasto
tags:
---

## Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

Example 1:
```
Input: ["flower","flow","flight"]
Output: "fl"
```

Example 2:
```
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

Note: all given inputs are in lowercase letters `a-z`.

## Solution

#### Space and Time Complexity

Since we aren't storing anything the space complexity is _O(1)_. The time complexity is _O(mn)_ where _m_ is the number of letters in the common prefix and _n_ is the number of strings. We are checking letter by letter (only if it matches) for every string.

```python
def check_letter(idx, letter, min_len, strs):
    for string in strs:
        if idx >= min_len:
            return False
        if letter != string[idx]:
            return False
    return True

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        min_len = min([len(x) for x in strs])
        prefix = []
        first_string = strs[0]
        for idx, letter in enumerate(first_string):
            if check_letter(idx, letter, min_len, strs):
                prefix.append(letter)
            else:
                break
        return ''.join(prefix)
```

## Javascript Solution by Akira957
```javascript
var longestCommonPrefix = function(strs) {
     if(!strs.length){
        return ''
    }
    let firstStr=strs.shift()
    if(!strs.length){
        return firstStr
    }
    
    let isFound=false
    let str=firstStr
    
        for(var j=firstStr.length;j>0;j--){
            str=firstStr.slice(0,j)
            isFound=strs.every((item)=>{
                return item.indexOf(str)==0
            })
            if(isFound){
                return str
            }
        }
    return ''
};
```
