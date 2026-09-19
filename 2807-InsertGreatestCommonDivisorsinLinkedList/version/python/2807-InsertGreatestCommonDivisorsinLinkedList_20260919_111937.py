# Last updated: 19/09/2026, 11:19:37
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
13            gcd_val=gcd(curr.val,nxt.val)
14            gcd_node=ListNode(gcd_val)
15
16            curr.next=gcd_node
17            gcd_node.next=nxt
18
19            curr=nxt
20
21        return head