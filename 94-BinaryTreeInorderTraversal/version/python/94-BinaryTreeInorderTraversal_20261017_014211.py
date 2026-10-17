# Last updated: 17/10/2026, 01:42:11
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
9        res=[]
10
11        def dfs(node):
12            if not node:
13                return 
14
15            dfs(node.left)
16            res.append(node.val)
17            dfs(node.right)
18
19        dfs(root)
20        return res       
21        