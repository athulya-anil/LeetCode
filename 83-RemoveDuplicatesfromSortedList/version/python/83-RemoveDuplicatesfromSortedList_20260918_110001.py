# Last updated: 18/09/2026, 11:00:01
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def deleteDuplicates(self, head):
8        """
9        :type head: Optional[ListNode]
10        :rtype: Optional[ListNode]
11        """
12        curr=head
13
14        while curr and curr.next:
15            if curr.val==curr.next.val:
16                curr.next=curr.next.next
17            else:
18                curr=curr.next           
19        return head        