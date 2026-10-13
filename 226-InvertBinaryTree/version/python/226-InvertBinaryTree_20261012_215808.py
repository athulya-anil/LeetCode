# Last updated: 12/10/2026, 21:58:08
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
9        if not root:
10            return 
11
12        left = self.invertTree(root.left)
13        right = self.invertTree(root.right)    
14        
15        root.right = left
16        root.left = right
17
18        return root