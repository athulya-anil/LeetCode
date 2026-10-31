# Last updated: 31/10/2026, 13:53:26
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6from math import gcd
7
8class Solution:
9    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:   
10        curr=head
11
12        while curr and curr.next:
13            gcd_val=gcd(curr.val,curr.next.val)    
14            gcd_node=ListNode(gcd_val)
15
16            nxt=curr.next
17            curr.next=gcd_node
18            gcd_node.next=nxt
19            curr=nxt
20        return head    
21
22        