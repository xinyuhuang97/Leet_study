# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        plusone=False
        sum_listnode=ListNode()
        head=sum_listnode
        val1, val2 = 0, 0
        while l1!=None or l2!=None:            
            if plusone==True:
                sum_listnode.val=1
                plusone=False
            
            if l1==None:
                val1=0
            else:
                val1=l1.val
            if l2==None:
                val2=0
            else:
                val2=l2.val
            sum_twoList=val1 + val2
            if sum_listnode.val+sum_twoList>=10:
                plusone=True
                sum_listnode.val+=sum_twoList-10
            else:
                sum_listnode.val+=sum_twoList
            if l1!=None:
                l1=l1.next
            if l2!=None:
                l2=l2.next
            if plusone==True and l1==None and l2==None:
                sum_listnode.next=ListNode()
                sum_listnode.next.val=1
            if l1!=None or l2!=None:
                sum_listnode.next=ListNode()
            sum_listnode=sum_listnode.next
        return head
        