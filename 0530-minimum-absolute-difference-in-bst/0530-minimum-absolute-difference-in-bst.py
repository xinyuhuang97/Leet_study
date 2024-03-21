import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        dif_dic={}
        deque=collections.deque([root])
        while deque:
            node=deque.pop()
            if node==None:
                continue
            if node.val not in dif_dic.keys():
                dif_dic[node.val]=inf
            deque.append(node.left)
            deque.append(node.right)
        deque=collections.deque([root])
        min_dif=inf
        while deque:
            node=deque.pop()
            if node!=None:
                for key in dif_dic.keys():
                    if key!=node.val and abs(key-node.val)<min_dif:
                        min_dif=abs(key-node.val)
                deque.append(node.left)
                deque.append(node.right)
        return min_dif
                    