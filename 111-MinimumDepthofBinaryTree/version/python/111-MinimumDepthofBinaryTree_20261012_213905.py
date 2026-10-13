# Last updated: 12/10/2026, 21:39:05
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
11   
12
13        left=self.minDepth(root.left)
14        right=self.minDepth(root.right)
15
16        if not root.left:
17            return 1 + right
18        if not root.right:
19            return 1+ left    
20
21        return 1 + min(left,right)    
22        