# Last updated: 31/10/2026, 19:02:58
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        slow=fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        to_be_deleted=slow

        dummy=ListNode(0,head)
        curr=head
        prev=dummy
        
        while curr:
            if curr == to_be_deleted:
                prev.next=curr.next
                curr=curr.next
            else:
                curr=curr.next
                prev=prev.next    

        return dummy.next        
        