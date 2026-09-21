# Last updated: 21/09/2026, 13:20:09
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
8        curr=head
9
10        while curr and curr.next:
11            nxt=curr.next
12            if curr.val==curr.next.val:
13                curr.next=curr.next.next
14            else:
15                curr=nxt    
16
17        return head            
18
19        