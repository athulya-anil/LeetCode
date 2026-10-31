# Last updated: 31/10/2026, 13:36:09
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def middleNode(self, head: ListNode | None) -> ListNode | None:
8        slow=fast=head
9
10        while fast and fast.next:
11            slow=slow.next
12            fast=fast.next.next
13
14        return slow    
15        