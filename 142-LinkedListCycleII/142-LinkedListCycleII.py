# Last updated: 16/12/2025, 09:08:28
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution(object):
8    def detectCycle(self, head):
9        fast=head
10        slow=head
11        while fast and fast.next:
12            slow=slow.next
13            fast=fast.next.next
14            if fast==slow:
15                slow=head    
16                while slow!=fast:
17                    slow=slow.next
18                    fast=fast.next
19                return slow    
20
21
22
23
24
25        