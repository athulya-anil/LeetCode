# Last updated: 11/10/2026, 01:15:13
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: TreeNode | None) -> bool:
9        if not root:
10            return True
11
12        def checker(left,right):
13            if not right and not left:
14                return True
15
16            if not right or not left:
17                return False  
18
19            if left.val != right.val:
20                return False
21
22            return (checker(left.left,right.right) and checker(left.right,right.left))
23        
24        return checker(root.left,root.right)