# Last updated: 16/10/2026, 22:48:07
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: TreeNode | None) -> bool:
9        if not root:
10            return False
11
12        def checker(p,q):
13            if not p and not q:
14                return True
15            if not p or not q:
16                return False
17                    
18            if p.val != q.val:
19                return False
20
21            return checker(p.left,q.right) and checker(p.right,q.left)
22
23        return (checker(root.left,root.right))
24       