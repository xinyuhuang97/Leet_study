# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        return 1+self.depth(root)
    def depth(self, root: Optional[TreeNode]) -> int:
        left_length=0
        right_length=0
        if root.left!=None:
            left_length=1+self.depth(root.left)
        if root.right!=None:
            right_length=1+self.depth(root.right)
        return max(left_length, right_length)