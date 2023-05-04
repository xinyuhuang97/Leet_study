# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node_rest=[root]
        list_node=[]
        while node_rest!=[]:
            current_node = node_rest.pop()
            if current_node!=None:
                list_node.append(current_node.val)
                node_rest.append(current_node.left)
                node_rest.append(current_node.right)
        list_node=sorted(list_node)
        return list_node[k-1]