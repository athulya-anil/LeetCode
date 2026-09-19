# Last updated: 19/09/2026, 14:06:12
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
8        nums=set(nums)
9        curr=head
10        dummy=ListNode(0,head)
11        prev=dummy
12
13        while curr:
14            if curr.val in nums:
15                prev.next=curr.next
16                curr=curr.next  
17            else:
18                prev=prev.next
19                curr=curr.next   
20
21        return dummy.next        
22        