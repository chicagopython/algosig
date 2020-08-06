---
title: Base-10 to Binary
category:
link: https://runestone.academy/runestone/books/published/pythonds/BasicDS/ConvertingDecimalNumberstoBinaryNumbers.html
author:
gh_comments_issue_id: 52
tags:
  - stack
  - loop
  - recursion
---

## Description

Write a function to convert any base-10 number to a base-2 (binary) number.
The algorithm should follow these steps:

1. If the input number is even, prepend our output string with `0`. Else prepend with `1`.
2. Use floor or integer division (no remainder) to divide the input number by `2`.
3. Repeat steps 1 & 2 until our input is reduced to `0`.

For example, given an input `5`:
1. `5` is odd, so our binary representation will start with `1`.
2. `5 / 2` (integer division) is `2`.
3. `2` is even, so our binary representation becomes `01`.
4. `2 / 2` (integer division) is `1`.
5. `1` is odd, so our binary representation becomes `101`.
6. `1 / 2` (integer division) is `0`. Output `101`.

**Stretch Goal:** Modify your function to convert a base-10 number to any base 2 through 9.
Hint: simply checking whether the input is odd or even is insufficient.
What operator can we use in Python to return a `0` or `1` depending on whether the input is even or odd?
How would we modify this to support other bases?

## Solution

```python
def base10_to_binary(n:int) -> str:
    """enter solution here"""

    return

# tests
assert base10_to_binary(1) == '1'
assert base10_to_binary(2) == '10'
assert base10_to_binary(3) == '11'
assert base10_to_binary(int(10e10)) == '1011101001000011101101110100000000000'
```
