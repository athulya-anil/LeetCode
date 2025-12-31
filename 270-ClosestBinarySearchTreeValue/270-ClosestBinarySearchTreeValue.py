# Last updated: 31/12/2025, 21:54:41
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def closestValue(self, root, target):
9        """
10        :type root: Optional[TreeNode]
11        :type target: float
12        :rtype: int
13        """
14        closest=root.val
15
16        while root:
17            if abs(root.val-target) < abs(closest-target) or abs(root.val-target) == abs(closest-target) and root.val<closest:
18                closest = root.val
19            if target < root.val:
20                root=root.left
21            else:
22                root=root.right  
23        return closest              
24
25
26       