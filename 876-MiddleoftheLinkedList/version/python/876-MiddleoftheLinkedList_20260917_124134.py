# Last updated: 17/09/2026, 12:41:34
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def middleNode(self, head):
8        fast=head
9        slow=head
10
11        while fast and fast.next:
12            slow=slow.next
13            fast=fast.next.next
14    
15        return slow    
16        