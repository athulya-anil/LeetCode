# Last updated: 16/12/2025, 19:19:39
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def middleNode(self, head):
8        fast=head
9        slow=head
10        while fast and fast.next:
11            fast=fast.next.next
12            slow=slow.next
13        return slow    
14
15        
16        