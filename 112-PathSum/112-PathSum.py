# Last updated: 24/12/2025, 20:21:30
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def hasPathSum(self, root, targetSum):
9        """
10        :type root: Optional[TreeNode]
11        :type targetSum: int
12        :rtype: bool
13        """
14        def dfs(node,currSum):
15            if not node:
16                return False
17
18            currSum += node.val    
19            
20            if not node.left and not node.right:   
21                return currSum == targetSum
22
23            return dfs(node.left, currSum) or dfs(node.right, currSum)  
24
25        return dfs(root,0)        