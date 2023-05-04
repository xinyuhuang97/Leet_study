# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        min_heap = []
        node_stack = [root]
        
        while node_stack:
            current_node = node_stack.pop()
            if current_node:
                if (len(min_heap)<k):
                    heapq.heappush(min_heap, -current_node.val)
                else:
                    heapq.heappushpop(min_heap, -current_node.val)
                node_stack.append(current_node.right)
                node_stack.append(current_node.left)
                
        return -min_heap[0]