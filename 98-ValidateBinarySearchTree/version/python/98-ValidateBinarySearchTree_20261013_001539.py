# Last updated: 13/10/2026, 00:15:39
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: TreeNode | None) -> bool:
9
10        def check(root,minn,maxx):
11            if not root:
12                return True
13
14            if maxx <= root.val or minn >= root.val:
15                return False       
16
17            return check(root.left,minn,root.val) and check(root.right,root.val,maxx)   
18 
19        return check((root),float('-inf'),float('inf')) 