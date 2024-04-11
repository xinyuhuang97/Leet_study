# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        less_list=ListNode(0,None)
        head_less_list=less_list
        ge_list=ListNode(0,None)
        head_ge_list=ge_list
        curr=head
        while curr:
            #print("here",curr.val)
            if curr.val<x:
                less_list.next=curr
                less_list=less_list.next
                curr=curr.next
                less_list.next=None
            else:
                ge_list.next=curr
                ge_list=ge_list.next
                curr=curr.next
                ge_list.next=None
        head_less_list=head_less_list.next
        if head_less_list==None:
            return head_ge_list.next
        less_list.next=head_ge_list.next
        return head_less_list
                