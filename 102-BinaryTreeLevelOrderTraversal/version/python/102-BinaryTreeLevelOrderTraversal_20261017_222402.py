# Last updated: 17/10/2026, 22:24:02
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
12        ans=[]
13
14        if not root:
15            return []
16
17        while q:
18            level=[]
19            n = len(q)
20            for i in range(n):
21                node = q.popleft()
22                level.append(node.val)
23
24                if node.left:
25                    q.append(node.left)
26                if node.right:
27                    q.append(node.right)
28
29            ans.append(level)
30
31        return ans    
32
33
34
35
36
37        