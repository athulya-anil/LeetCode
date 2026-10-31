# Last updated: 31/10/2026, 19:11:27
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        balanced=[True]
        
        def check(root):
            if not root:
                return 0

            left = check(root.left)    
            right = check(root.right)  

            if abs(left-right) > 1:
                balanced[0]=False 

            return 1 + max(left,right)

        check(root)   
        return balanced[0] 
