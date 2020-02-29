---
title: Game of Life
category:
link: https://leetcode.com/problems/game-of-life/
author:
---

## Description

Given a board with `m` by `n` cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules. Determine the next state.

1. Live cell with fewer than two live neighbors dies, as if caused by under-population.
1. Live cell with two or three live neighbors lives on to the next generation.
1. Live cell with more than three live neighbors dies, as if by over-population..
1. Dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.


## Solution

```python
class Board:
	def __init__(self, board):
    import copy
    self.board = copy.deepcopy(board)
    self.rows = len(board)
    self.cols = len(board[0])
    self.board = []
    for y in range(self.rows):
      self.board.append([board[y][x] for x in range(self.cols)])

	def value(self, y, x):
    if x < 0 or y < 0:
      return 0
    if y >= self.rows:
      return 0
    if x >= self.cols:
      return 0
    if not self.board[y][x]:
      return 0
    return 1

	def num_live_neighbors(self, y, x):
    neighbors = []
    for offset_y, offset_x in [(0,1),(1,0),(-1,1),(1,1)]:
      neighbors.append(self.value(y+offset_y, x+offset_x))
      neighbors.append(self.value(y-offset_y, x-offset_x))
    return sum(neighbors)

	def print(self):
    for y in range(self.rows):
      for x in range(self.cols):
        if self.value(y,x):
          print('*', end='')
        else:
          print('-', end='')
        print()


def gameOfLife(board):
	"""
	Do not return anything, modify board in-place instead.
	"""
	board_obj = Board(board)
	board_obj.print()
	for y in range(board_obj.rows):
    for x in range(board_obj.cols):
      num_live_neighbors = board_obj.num_live_neighbors(y,x)
      if board_obj.value(y,x): # Alive
        if num_live_neighbors == 2 or num_live_neighbors == 3:
          new_value = 1
        else:
          new_value = 0
      else: # Dead
        if num_live_neighbors == 3:
          new_value = 1
        else:
          new_value = 0
      board[y][x] = new_value
	Board(board).print()


from pprint import pprint
board = [
  [0,0,0,0,0,0,1,0],
  [0,0,0,0,1,0,1,1],
  [0,0,0,0,1,0,1,0],
  [0,0,0,0,1,0,0,0],
  [0,0,1,0,0,0,0,0],
  [1,0,1,0,0,0,0,0],
]

while True:
	gameOfLife(board)
	input()
```
