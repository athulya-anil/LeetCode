# Last updated: 16/10/2026, 23:15:58
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
9        if not root:
10            return
11
12        if root.val == val:
13            return root
14
15        if root.val > val:
16            return self.searchBST(root.left,val) 
17        else:
18            return self.searchBST(root.right,val) 
19