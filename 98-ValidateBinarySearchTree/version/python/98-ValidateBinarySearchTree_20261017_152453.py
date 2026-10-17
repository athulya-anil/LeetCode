# Last updated: 17/10/2026, 15:24:53
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: TreeNode | None) -> bool:
9        
10        def dfs(node,maxx,minn):
11            if not node:
12                return True
13            if node.val >= maxx or node.val <= minn:
14                return False
15
16            return (dfs(node.left,node.val,minn) and dfs(node.right,maxx,node.val))
17
18        return dfs(root,float('inf'),float('-inf'))
19                
20        
21            
22
23