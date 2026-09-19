# Last updated: 19/09/2026, 12:59:15
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
18        back=slow.next  
19        slow.next=None
20        prev=None
21
22        while back:
23            nxt=back.next
24            back.next=prev
25            prev=back
26            back=nxt
27        head2 = prev    
28        front=head
29        #interchange
30        while head2:
31            temp1=front.next
32            temp2=head2.next
33            front.next=head2
34            head2.next=temp1
35            front=temp1
36            head2=temp2
37
38        return head
39
40