# Last updated: 31/10/2026, 17:56:20
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
8        dummy=ListNode()
9        dummy.next=head
10        slow=fast=dummy
11
12        for _ in range(n+1):
13            fast=fast.next
14
15        while fast:
16            slow=slow.next
17            fast=fast.next
18        slow.next=slow.next.next        
19
20        return dummy.next
21        
22        