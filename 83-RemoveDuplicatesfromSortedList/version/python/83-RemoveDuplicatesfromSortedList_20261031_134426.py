# Last updated: 31/10/2026, 13:44:26
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
11            if curr.val == curr.next.val:       
12                curr.next=curr.next.next
13            else:    
14                curr=curr.next    
15        return head        
16        