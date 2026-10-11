# Last updated: 11/10/2026, 15:21:56
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def minDepth(self, root: TreeNode | None) -> int:
9        if not root:
10            return 0
11        if not root.left and not root.right:
12            return 1            
13
14        left = self.minDepth(root.left)  
15        right = self.minDepth(root.right)  
16          
17        if not root.left:
18            return 1+ right   
19        if not root.right:
20            return 1+left 
21
22        return 1+min(left,right)
23          
24        