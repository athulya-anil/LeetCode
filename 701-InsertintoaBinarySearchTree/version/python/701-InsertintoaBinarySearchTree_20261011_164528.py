# Last updated: 11/10/2026, 16:45:28
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
9        if not root: 
10            return TreeNode(val)
11
12        if root.val < val:
13            root.right=self.insertIntoBST(root.right,val)
14            
15        else:
16            root.left=self.insertIntoBST(root.left,val)
17
18        return root         