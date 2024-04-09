# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:
            return list2
        if list2==None:
            return list1
        if list1.val>list2.val:
            head=list2
            tmp=list1
            list1=list2
            list2=tmp
        else:
            head=list1
        while list1!=None and list2!=None:
            if list1.val<=list2.val:
                if list1.next==None or list2.val<=list1.next.val:
                    tmp=list2.next
                    list2.next=list1.next
                    list1.next=list2
                    list1=list1.next
                    list2=tmp
                else:
                    list1=list1.next
            else:
                list1=list1.next
        return head