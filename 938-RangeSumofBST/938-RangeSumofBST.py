# Last updated: 01/01/2026, 22:37:53
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def rangeSumBST(self, root, low, high):
9        """
10        :type root: Optional[TreeNode]
11        :type low: int
12        :type high: int
13        :rtype: int
14        """
15        if not root:
16            return 0
17        
18        total = 0
19        if low <= root.val <= high:
20            total += root.val   
21
22
23        leftsum = self.rangeSumBST(root.left,low,high)   
24        rightsum = self.rangeSumBST(root.right,low,high)   
25
26        total += rightsum+leftsum
27        return(total)    