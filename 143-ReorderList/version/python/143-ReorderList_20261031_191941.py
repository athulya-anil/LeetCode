# Last updated: 31/10/2026, 19:19:41
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: ListNode | None) -> None:
8        """
9        Do not return anything, modify head in-place instead.
10        """
11        slow=fast=head
12        while fast and fast.next:
13            slow=slow.next
14            fast=fast.next.next
15
16        curr=slow.next
17        prev=None
18        slow.next=None   
19
20        while curr:
21            nxt=curr.next
22            curr.next=prev
23            prev=curr
24            curr=nxt
25
26        h2=prev
27        h1=head
28
29        while h1 and h2:
30            temp1=h1.next
31            temp2=h2.next
32
33            h1.next=h2
34            h2.next=temp1
35
36            h1=temp1
37            h2=temp2
38 