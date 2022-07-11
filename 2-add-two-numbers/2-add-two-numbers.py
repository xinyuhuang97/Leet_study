# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        lg1,lg2 = 0,0
        c1,c2=l1,l2
        while c1!=None:
            c1=c1.next
            lg1+=1
        while c2!=None:
            c2=c2.next
            lg2+=1
        minlg=min(lg1, lg2)
        maxlg=max(lg1,lg2)
        
        new_list=l2
        unchosen_list=l1
        
        if lg1>lg2:
            new_list=l1 
            unchosen_list=l2
            
        head=new_list

        for i in range(maxlg):
            if i <minlg:
                s=new_list.val+unchosen_list.val
                if s>=10:
                    new_list.val=s-10
                    if i!=maxlg-1:
                        new_list.next.val+=1
                    else:
                        new_list.next=ListNode(1,None)
                else:
                    new_list.val=s
                unchosen_list=unchosen_list.next
            else:
                print(i,new_list.val,maxlg)
                if new_list.val>=10 :
                    new_list.val-=10
                    if i!=maxlg-1:
                        new_list.next.val+=1
                    else:
                        new_list.next=ListNode(1,None)
                
            new_list=new_list.next
            
        return head