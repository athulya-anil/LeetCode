# Last updated: 18/09/2026, 11:20:54
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6from math import gcd
7class Solution:
8    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        curr=head
10
11        while curr and curr.next:
12            nxt=curr.next
13            
14            gcd_val=gcd(curr.val,nxt.val)
15            gcd_node=ListNode(gcd_val)
16           
17            curr.next=gcd_node
18            gcd_node.next=nxt
19
20            curr=nxt
21
22        return head    
23        
24        