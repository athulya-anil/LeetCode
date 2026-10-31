# Last updated: 31/10/2026, 17:29:06
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        slow=fast=head
10        while fast and fast.next:
11            slow=slow.next
12            fast=fast.next.next
13
14            if slow == fast:
15                slow=head
16
17                while slow != fast:
18                    slow=slow.next
19                    fast=fast.next
20                    
21                return slow
22        return None        
23     
24
25