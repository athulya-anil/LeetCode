# Last updated: 31/10/2026, 18:43:47
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
8        dummy1=ListNode()
9        dummy=dummy1
10
11        while list1 and list2:
12            if list1.val<list2.val:
13                dummy.next=list1
14                list1=list1.next
15            else:
16                dummy.next=list2   
17                list2=list2.next
18
19            dummy=dummy.next    
20
21        while list1:
22            dummy.next=list1
23            list1=list1.next
24            dummy=dummy.next
25        while list2:
26            dummy.next=list2     
27            list2=list2.next
28            dummy=dummy.next
29
30        return dummy1.next    
31        