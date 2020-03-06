---
title: Longest Common Prefix
link: https://leetcode.com/problems/longest-common-prefix/
author:
tags:
  - unsolved
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

## Javascript Solution
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
