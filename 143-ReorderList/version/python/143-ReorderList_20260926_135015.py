# Last updated: 26/09/2026, 13:50:15
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
12
13        while fast and fast.next:
14            slow=slow.next
15            fast=fast.next.next
16
17        curr=slow.next
18        slow.next=None
19        prev=None
20
21        while curr:
22            nxt=curr.next
23            curr.next=prev
24            prev=curr
25            curr=nxt
26
27        h2 = prev  
28        h1 = head
29
30        while h1 and h2:
31            temp1=h1.next
32            temp2=h2.next
33
34            h1.next=h2
35            h2.next=temp1
36
37            h1=temp1
38            h2=temp2
39            
40        return head    
41