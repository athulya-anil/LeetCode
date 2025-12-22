# Last updated: 22/12/2025, 19:47:49
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def isSameTree(self, p, q):
9        """
10        :type p: Optional[TreeNode]
11        :type q: Optional[TreeNode]
12        :rtype: bool
13        """
14        if not p and not q:
15            return True
16        if not p or not q or p.val != q.val:
17            return False
18        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
19      
20        