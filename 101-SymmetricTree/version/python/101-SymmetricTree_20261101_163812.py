# Last updated: 01/11/2026, 16:38:12
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
12        def balanced(p,q):
13            if not p and not q:
14                return True
15            if not p or not q:
16                return False
17            if p.val != q.val:
18                return False
19            return(balanced(p.left,q.right) and balanced(p.right,q.left))            
20
21        return balanced(root.left,root.right)    
22        