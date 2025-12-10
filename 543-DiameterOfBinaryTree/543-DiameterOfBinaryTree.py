# Last updated: 10/12/2025, 07:41:40
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0

            # Compute left and right subtree heights
            left = dfs(node.left)
            right = dfs(node.right)

            # Update diameter (longest path through current node)
            self.max_diameter = max(self.max_diameter, left + right)

            # Return height for parent call
            return 1 + max(left, right)

        dfs(root)
        return self.max_diameter
