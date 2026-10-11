# Last updated: 11/10/2026, 15:51:08
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: TreeNode | None) -> bool:
9        def match(left,right):
10            if not left and not right:
11                return True
12            if not left or not right:
13                return False
14                
15            if left.val != right.val:
16                return False
17
18            return match(left.right,right.left) and match(right.right,left.left)
19
20        return match(root.left,root.right) 
21
22
23        