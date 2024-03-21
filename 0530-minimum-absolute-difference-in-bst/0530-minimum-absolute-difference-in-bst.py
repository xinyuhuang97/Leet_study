import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def InOrderTraversal(val):
            if val==None:
                return []
            inorder_list=InOrderTraversal(val.left)
            inorder_list.append(val.val)
            inorder_list+=InOrderTraversal(val.right)
            return inorder_list
        
        def FindMinDifference(inorder_list):
            lg=len(inorder_list)
            min_val=inf
            for i in range(lg-1):
                if abs(inorder_list[i]-inorder_list[i+1])<min_val:
                    min_val=inorder_list[i+1]-inorder_list[i]
            return min_val
        
        inorder_list=InOrderTraversal(root)
        return FindMinDifference(inorder_list)
        