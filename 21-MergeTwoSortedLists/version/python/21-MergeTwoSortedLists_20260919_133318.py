# Last updated: 19/09/2026, 13:33:18
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
8        dummy=ListNode()
9        tail=dummy
10
11        while list1 and list2:
12            if list1.val<=list2.val:
13                tail.next=list1
14                list1=list1.next
15            else:
16                tail.next=list2
17                list2=list2.next
18
19            tail=tail.next    
20
21        if list1:      
22            tail.next=list1  
23        if list2:      
24            tail.next=list2    
25
26        return dummy.next      
27           