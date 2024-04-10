# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head
        head=ListNode(0, head)
        curr=head
        for i in range(left-1):
            curr=curr.next
        prev_node=curr
        curr=curr.next
        for i in range(left, right):
            next_node=curr.next
            next_node.next,curr.next,prev_node.next = prev_node.next, next_node.next,next_node
        return head.next


            
            
            
            
        
        