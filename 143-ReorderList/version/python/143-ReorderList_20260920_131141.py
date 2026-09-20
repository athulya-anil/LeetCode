# Last updated: 20/09/2026, 13:11:41
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
11        #Find middle
12        slow=head
13        fast=head
14        while fast and fast.next:
15            slow=slow.next
16            fast=fast.next.next
17
18        curr=slow.next        
19        slow.next=None
20        prev=None
21
22        while curr:
23            nxt=curr.next
24            curr.next=prev
25            prev=curr
26            curr=nxt
27
28        h2=prev
29        h1=head
30
31        while h2:
32            temp2=h2.next
33            temp1=h1.next
34            
35            h1.next=h2
36            h2.next=temp1
37
38            h1=temp1
39            h2=temp2
40
41        return head    