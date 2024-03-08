# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        b1=(p!=None)
        b2=(q!=None)
        if b1 != b2:
            return False
        if b1 and b2:
            if p.val!=q.val:
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)   
        return True