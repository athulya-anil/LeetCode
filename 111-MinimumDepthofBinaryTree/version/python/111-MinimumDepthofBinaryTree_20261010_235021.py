# Last updated: 10/10/2026, 23:50:21
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
12        left=self.minDepth(root.left)    
13        right=self.minDepth(root.right)  
14
15        if not root.left:
16            return 1 + right
17        if not root.right:
18            return 1 + left    
19
20        return 1 + min(left,right)
21        