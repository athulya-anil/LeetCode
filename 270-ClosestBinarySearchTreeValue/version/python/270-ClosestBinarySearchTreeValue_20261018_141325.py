# Last updated: 18/10/2026, 14:13:25
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def closestValue(self, root: TreeNode | None, target: float) -> int:
9
10        closest = root.val
11
12        while root:
13            if not root:
14                return
15
16            if abs(root.val-target) < abs(closest - target) or abs(root.val-target) == abs(closest - target) and root.val < closest:
17                closest=root.val
18
19            if target < root.val:
20                root=root.left
21            elif target > root.val:
22                root=root.right
23            else:
24                return root.val    
25
26        return closest        
27
28
29
30  
31