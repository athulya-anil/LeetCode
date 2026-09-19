# Last updated: 19/09/2026, 14:25:40
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
8        slow=head
9        fast=head
10
11        while fast and fast.next:
12            slow=slow.next
13            fast=fast.next.next
14
15        to_be_deleted=slow  
16
17        dummy=ListNode(0,head)
18        prev=dummy
19        curr=head
20
21        while curr:
22            if curr == to_be_deleted:
23                prev.next=curr.next
24                curr=curr.next
25            else:
26                curr=curr.next
27                prev=prev.next    
28        return dummy.next        
29        
30
31        