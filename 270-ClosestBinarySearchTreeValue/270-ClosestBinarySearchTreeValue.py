# Last updated: 30/12/2025, 23:10:12
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
14        closest = root.val    
15        while root:
16            if abs(root.val-target) < abs(target-closest) or (abs(root.val-target) == abs(target-closest) and root.val<closest):
17                closest=root.val
18            if target<root.val:
19                root=root.left
20            else:
21                root=root.right    
22        return closest  
23        