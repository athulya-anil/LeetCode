# Last updated: 18/12/2025, 06:21:58
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def mergeTwoLists(self, list1, list2):
8        """
9        :type list1: Optional[ListNode]
10        :type list2: Optional[ListNode]
11        :rtype: Optional[ListNode]
12        """
13        dummy=ListNode()
14        tail=dummy
15        while list1 and list2:
16            if list1.val<list2.val:
17                tail.next=list1
18                list1=list1.next
19            else:
20                tail.next=list2
21                list2=list2.next
22            tail=tail.next
23
24        if list1:
25            tail.next=list1
26        else:
27            tail.next=list2
28
29        return(dummy.next)    
30
31          
32