# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashmap_number={}
        head=ListNode(0, head)
        first=head.next
        while first:
            if first.val in hashmap_number:
                hashmap_number[first.val].append(first)
            else:
                hashmap_number[first.val]=[first]
            first=first.next
        curr=head
        while curr.next:
            if len(hashmap_number[curr.next.val])!=1:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head.next
            