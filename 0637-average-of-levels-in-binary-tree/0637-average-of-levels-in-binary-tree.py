import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result=[]
        q=collections.deque([root])
        while q:
            n=len(q)
            sumVal=0
            cpt=0
            for i in range(n):
                node=q.popleft()
                if node:
                    cpt+=1
                    sumVal+=node.val
                    q.append(node.left)
                    q.append(node.right)
            if cpt>0:
                result.append(sumVal/cpt)
        return result