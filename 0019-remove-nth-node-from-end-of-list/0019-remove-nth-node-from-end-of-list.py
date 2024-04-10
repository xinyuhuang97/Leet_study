# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cpt = 1
        hashmap_list={}
        curr=head
        while curr:
            hashmap_list[cpt]=curr
            cpt+=1
            curr=curr.next
        if cpt==2:
            return None
        n_start = cpt-n
        if n_start==1:
            return head.next
        hashmap_list[n_start-1].next=hashmap_list[n_start].next
        return head