# Last updated: 10/12/2025, 07:39:42
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        remove_set = set(nums)  # O(m)
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        # Traverse and remove nodes
        while current.next:
            if current.next.val in remove_set:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next
        