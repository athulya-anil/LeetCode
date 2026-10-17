# Last updated: 17/10/2026, 01:39:28
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
10        res=[]
11
12        def dfs(node):
13            if not node:
14                return
15
16            dfs(node.left)   
17            dfs(node.right) 
18            res.append(node.val) 
19
20        dfs(root) 
21        return res   
22        
23        