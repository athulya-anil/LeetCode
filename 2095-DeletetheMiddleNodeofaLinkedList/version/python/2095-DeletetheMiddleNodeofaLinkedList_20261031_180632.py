# Last updated: 31/10/2026, 18:06:32
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
8        slow=fast=head
9
10        while fast and fast.next:
11            slow=slow.next
12            fast=fast.next.next
13
14        to_be_deleted=slow
15
16        dummy=ListNode(0,head)
17        curr=head
18        prev=dummy
19        
20        while curr:
21            if curr == to_be_deleted:
22                prev.next=curr.next
23                curr=curr.next
24            else:
25                curr=curr.next
26                prev=prev.next    
27
28        return dummy.next        
29        