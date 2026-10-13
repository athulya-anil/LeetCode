# Last updated: 12/10/2026, 22:54:58
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
9
10        if not root:
11            return TreeNode(val)
12        
13        if root.val<val:
14            root.right = self.insertIntoBST(root.right,val)
15        else:
16            root.left = self.insertIntoBST(root.left,val)    
17
18        return root
19        