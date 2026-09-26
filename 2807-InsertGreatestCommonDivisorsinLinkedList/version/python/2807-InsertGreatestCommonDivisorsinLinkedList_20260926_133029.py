# Last updated: 26/09/2026, 13:30:29
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6from math import gcd
7class Solution:
8    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        curr=head
10        while curr and curr.next:
11            gcd_val=gcd(curr.val,curr.next.val)
12            gcd_node=ListNode(gcd_val)
13
14            nxt=curr.next
15            curr.next=gcd_node
16            gcd_node.next=nxt
17
18            curr=nxt
19        return head    
20        