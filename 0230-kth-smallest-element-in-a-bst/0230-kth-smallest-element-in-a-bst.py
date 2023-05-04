# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import numpy as np
null=0
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        print(root)
        node_rest=[root]
        list_node=[]
        while node_rest!=[]:
            current_node = node_rest.pop()
            if current_node!=None:
                list_node.append(current_node.val)
                print(current_node,"here")
                node_rest.append(current_node.left)
                node_rest.append(current_node.right)

        print(list_node)
        list_node=np.sort(list_node)
        print(list_node)
        return list_node[k-1]