# Last updated: 17/10/2026, 13:03:25
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
9        res=[]
10        def dfs(node):
11            if not node:
12                return
13
14            dfs(node.left)  
15            res.append(node.val)
16            dfs(node.right)  
17            
18        dfs(root)
19        return res    
20        