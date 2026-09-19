# Last updated: 19/09/2026, 12:09:17
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
11        #find middle
12        slow=head
13        fast=head
14        while fast and fast.next:
15            slow=slow.next
16            fast=fast.next.next
17        #reverse 2nd half
18        prev=None
19        curr=slow.next
20        slow.next=None  
21
22        while curr:
23            nxt=curr.next
24            curr.next=prev
25            prev=curr
26            curr=nxt
27        back = prev    
28        front = head
29        #3 
30        while back:
31            back_temp=back.next
32            front_temp=front.next
33            front.next=back
34            back.next=front_temp
35            front=front_temp
36            back=back_temp
37            
38        return head    
39            
40