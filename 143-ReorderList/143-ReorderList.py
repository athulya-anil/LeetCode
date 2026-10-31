# Last updated: 31/10/2026, 19:11:05
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        curr=slow.next
        slow.next=None
        prev=None

        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        h2 = prev  
        h1 = head

        while h1 and h2:
            temp1=h1.next
            temp2=h2.next

            h1.next=h2
            h2.next=temp1

            h1=temp1
            h2=temp2
            
        return head    
