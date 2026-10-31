# Last updated: 31/10/2026, 19:02:02
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:   
        curr=head

        while curr and curr.next:
            gcd_val=gcd(curr.val,curr.next.val)    
            gcd_node=ListNode(gcd_val)

            nxt=curr.next
            curr.next=gcd_node
            gcd_node.next=nxt
            curr=nxt
        return head    

        