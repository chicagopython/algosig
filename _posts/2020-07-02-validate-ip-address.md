---
title: Validate IP Address
category: AlgoSIG 2
link: https://leetcode.com/problems/validate-ip-address/
author: Kevin Nasto
gh_comments_issue_id: 48
tags:
  - strings
---

## Description

Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither. An IPv4 address is for example `172.16.254.1`. The numbers can be from *0* to *255* and there must be no leading zeros (e.g. *01*).

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address `2001:0db8:85a3:0000:0000:8a2e:0370:7334` is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so `2001:db8:85a3:0:0:8A2E:0370:7334`.

```
Input: IP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".
```

```
Input: IP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.
```

## Solution

```python
def valid_ip_address(IP):
    pass
```
