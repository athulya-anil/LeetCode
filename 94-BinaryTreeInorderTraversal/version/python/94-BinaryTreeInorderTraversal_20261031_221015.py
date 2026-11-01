# Last updated: 31/10/2026, 22:10:15
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
9        res=[]
10        if not root:
11            return []
12
13        def dfs(node):
14            if not node:
15                return []  
16
17            dfs(node.left)
18            res.append(node.val) 
19            dfs(node.right)
20
21        dfs(root)
22        return res
23        