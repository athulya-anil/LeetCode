# Last updated: 18/10/2026, 10:14:43
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        def search(root):
11            if not root:
12                return
13
14            if p.val < root.val and q.val < root.val:
15                return search(root.left)    
16            if p.val > root.val and q.val > root.val:
17                return search(root.right)  
18
19            return root        
20
21        return search(root)     