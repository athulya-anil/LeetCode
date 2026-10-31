# Last updated: 31/10/2026, 19:08:33
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return (TreeNode(val))

        if root.val < val:
            root.right=self.insertIntoBST(root.right,val)   
        else:
            root.left=self.insertIntoBST(root.left,val)       

        return root     

