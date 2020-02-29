---
title: Best Time to Buy and Sell Stock
category: AlgoSIG 11
link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
author:
tags:
  - Greedy
---

## Description

Say you have an array for which the ith element is the price of a given stock on day `i`.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
```
Input:  [7,1,5,3,6,4]
Output: 5
```
Explanation:
* Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
* Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
```
Input:  [7,6,4,3,1]
Output: 0
```
Explanation:
* In this case, no transaction is done, i.e. max profit = 0.

## Solution

Other solutions can be found on the LeetCode link above.

```python
def get_max_profit(stock_prices):
  if len(stock_prices) < 2:
    raise ValueError('Getting a profit requires at least 2 prices')

  min_price = stock_prices[0]
  max_profit = stock_prices[1] - stock_prices[0]

  print(f'ITERATION 0: \n MIN_PRICE: {min_price} \n MAX_PROFIT: {max_profit}')

  iteration = 1

  for current_time in range(1, len(stock_prices)):

    print(f'ITERATION {iteration} ' + '-' * 43)
    current_price = stock_prices[current_time]
    potential_profit = current_price - min_price

    print(f'CURRENT_PRICE: {current_price} \n POTENTIAL_PROFIT: {potential_profit}')
    max_profit = max(max_profit, potential_profit)
    min_price = min(min_price, current_price)

    print(f'MIN_PRICE: {min_price} \n MAX_PROFIT: {max_profit}')
    iteration += 1

  return max_profit

prices = [10, 7, 5, 8, 11, 9]

maximum = get_max_profit(prices)

print(maximum)
```

