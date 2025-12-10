# Last updated: 10/12/2025, 07:42:48
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k==0:
            return head
        temp=head
        count=1
        while temp.next:
            temp=temp.next
            count+=1
        temp.next=head    

        k=k%count
        if k==0:
            temp.next=None
            return head

        new_tail=head
        steps = count-k-1

        for _ in range(steps):
            new_tail=new_tail.next

        new_head=new_tail.next
        new_tail.next=None

        return new_head 
        
        
        