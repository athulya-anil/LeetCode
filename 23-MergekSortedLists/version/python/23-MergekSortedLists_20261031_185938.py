# Last updated: 31/10/2026, 18:59:38
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6import heapq
7
8class Solution:
9    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
10        dummy=ListNode()
11        curr=dummy
12        heap=[]
13        for i, node in enumerate(lists):
14            if node:
15                heapq.heappush(heap,(node.val,i,node))
16        while heap:
17            val,i,node = heapq.heappop(heap)       
18            curr.next=node
19            curr=node
20            node=node.next
21            if node:
22                heapq.heappush(heap,(node.val,i,node))
23
24        return dummy.next     
25        