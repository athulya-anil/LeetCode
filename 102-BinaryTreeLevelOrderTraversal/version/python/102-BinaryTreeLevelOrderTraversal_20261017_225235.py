# Last updated: 17/10/2026, 22:52:35
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
10        q=deque()
11        q.append(root)
12        res=[]
13
14        if not root:
15            return []
16
17        while q:
18            level=[]
19            n=len(q)
20
21            for i in range(n):
22                node=q.popleft()
23                level.append(node.val)
24
25                if node.left:
26                    q.append(node.left)
27
28                if node.right:
29                    q.append(node.right)  
30
31            res.append(level)
32            
33        return res              
34
35
36
37        