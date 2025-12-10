# Last updated: 10/12/2025, 07:39:57
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        #find middle
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next   
        #reverse middle
        prev=None
        curr=slow

        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt   
        #sum max

        left=head
        right=prev
        ans=0

        while left and right:
            ans=max(ans,left.val+right.val)
            left=left.next
            right=right.next
            
        return ans    