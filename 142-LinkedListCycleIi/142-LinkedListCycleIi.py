# Last updated: 10/07/2026, 11:59:59
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                slow=head    
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow    





        