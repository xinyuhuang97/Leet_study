# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head==None or head.next==None:
            return head
        cpt=0
        head=ListNode(0, head)
        curr=head
        hash_list={}
        while curr.next:
            hash_list[cpt]=curr.next
            curr=curr.next
            cpt+=1
        hash_list[cpt]=head.next
        print(cpt)
        curr.next=head.next
        hash_list[cpt-k%cpt-1].next=None
        head=hash_list[cpt-k%cpt]
        return head
            
        
            