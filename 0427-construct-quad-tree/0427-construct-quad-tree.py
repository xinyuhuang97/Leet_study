"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        size = len(grid)
        if size == 1:
            return Node(grid[0][0], True, None, None, None, None)
        same_val = all(grid[i][j] == grid[0][0] for i in range(size) for j in range(size))
        if same_val:
            return Node(grid[0][0], True, None, None, None, None)
        left_size = size//2
        print(grid[:left_size][:left_size])
        topleft = self.construct([row[:left_size] for row in grid[:left_size]])
        topright = self.construct([row[left_size:] for row in grid[:left_size]])
        bottomleft = self.construct([row[:left_size] for row in grid[left_size:]])
        bottomright = self.construct([row[left_size:] for row in grid[left_size:]])
        return Node(1, False, topleft, topright, bottomleft, bottomright)