# Last updated: 12/10/2026, 22:22:26
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
11        if root.val == val:
12            return root    
13
14        if root.val < val:
15            return(self.searchBST(root.right,val))   
16        else:
17            return(self.searchBST(root.left,val))    
18
19   
20
21       