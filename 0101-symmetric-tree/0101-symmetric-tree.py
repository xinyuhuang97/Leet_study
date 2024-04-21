import collections
import copy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_subtree_left(self, node):
        if node==None:
            return [None]
        else:
            return [node.val] + self.get_subtree_left(node.left) + self.get_subtree_left(node.right)
    def get_subtree_right(self, node):
        if node==None:
            return [None]
        else:
            return [node.val] + self.get_subtree_right(node.right) + self.get_subtree_right(node.left)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root ==None or root.left==root.right==None:
            return True
        left = self.get_subtree_left(root.left)
        right = self.get_subtree_right(root.right)
        #print(left)
        #print(right)
        lg_l = len(left)
        if lg_l!= len(right):
            return False
        for i in range(lg_l):
            if left[i]!=right[i]:
                return False
        return True
        

        
        
        
                
                