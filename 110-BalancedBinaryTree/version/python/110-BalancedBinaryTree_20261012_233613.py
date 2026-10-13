# Last updated: 12/10/2026, 23:36:13
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: TreeNode | None) -> bool:
9        balanced=[True]
10        def check(root):
11            if not root:
12                return 0
13
14            left=check(root.left)    
15            right=check(root.right)  
16
17            if abs(left-right)>1:
18                balanced[0]=False
19                return 0
20
21            return 1 + max(left,right)     
22
23        check(root)
24        return balanced[0]        
25
26
27        