---
title: Eating Cookies
date: 2020-03-05 14:40:46
link:
author:
tags:
  - recursive
  - iterative
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

## Solution 1: Iterative

```python
def eating_cookies(n):
  ways = {0:1,
          1:1,
          2:2,
          3:4}
  for i in range(4, n+1):
    ways[i] = ways[i-1] + ways[i-2] + ways[i-3]
  return ways[n]
```
## Solution 2: Recursive

```python
class Memoize(object):
  def __init__(self, func):
    self.func = func
    self.cache = {}
  def __call__(self, *args):
    if args in self.cache:
      return self.cache[args]
    ret = self.func(*args)
    self.cache[args] = ret
    return ret

@Memoize
def eatingCookies(n):
  if n < 0:
    print('Incorrect Input')
  elif n == 0:
    return 1
  elif n == 1:
    return 1
  elif n == 2:
    return 2
  else:
    return eatingCookies(n-1) + eatingCookies(n-2) + eatingCookies(n-3)
```

## Tests

```python
# tests
assert eating_cookies(50) == 10562230626642
assert eating_cookies(100) == 180396380815100901214157639
assert eating_cookies(500) == 1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527
```
