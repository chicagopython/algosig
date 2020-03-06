---
title: Eating Cookies
link:
author:
tags:
  - unsolved
---

## Description

![]({{ '/assets/img/cookie-monster.jpeg' | relative_url }})

Cookie Monster can eat either 0, 1, 2, or 3 cookies at a time. If he were given a jar of cookies with `n` cookies inside of it, how many ways could he eat all `n` cookies in the cookie jar? Implement a function `eating_cookies` that counts the number of possible ways Cookie Monster can eat all of the cookies in the jar.

For example, for a jar of cookies with `n = 3` (the jar has 3 cookies inside it), there are 4 possible ways for Cookie Monster to eat all the cookies inside it:

 1. He can eat 1 cookie at a time 3 times
 2. He can eat 1 cookie, then 2 cookies
 3. He can eat 2 cookies, then 1 cookie
 4. He can eat 3 cookies all at once.

Thus, `eating_cookies(3)` should return an answer of 4.

Note: there is 1 way to eat 0 cookies.

## Solution

```python
# tests
assert eating_cookies(50) = 10562230626642
assert eating_cookies(100) = 180396380815100901214157639
assert eating_cookies(500) = 1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527
```
