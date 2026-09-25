# Last updated: 24/09/2026, 23:27:53
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: TreeNode | None) -> int:
9        if not root:
10            return 0
11        left=self.maxDepth(root.left)
12        right=self.maxDepth(root.right)    
13
14        return (1+max(left,right))
15        