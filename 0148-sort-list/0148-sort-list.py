# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        t = head
        while t:
            size += 1
            t = t.next
        if size < 2:
            return head
        
        def merge(node, size):
            if size == 1:
                return ListNode(node.val)
            left_size = size//2
            right_size = size - left_size
            
            left_list = merge(node, left_size)
            for i in range(left_size):
                node=node.next
            right_list = merge(node, right_size)
            
            root = ListNode(-1)
            node = root
            while left_list or right_list:
                if left_list and right_list:
                    if left_list.val < right_list.val:
                        node.next = left_list
                        left_list = left_list.next
                        node = node.next
                    else:
                        node.next = right_list
                        right_list = right_list.next
                        node = node.next
                elif left_list:
                    node.next = left_list
                    left_list = left_list.next
                    node = node.next
                elif right_list:
                    node.next = right_list
                    right_list = right_list.next
                    node = node.next
            return root.next
        return merge(head, size)