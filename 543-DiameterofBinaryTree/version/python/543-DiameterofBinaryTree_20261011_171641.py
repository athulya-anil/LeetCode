# Last updated: 11/10/2026, 17:16:41
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        largest_diameter=[0]
10
11        def height(root):
12            if not root:
13                return 0
14
15            left=height(root.left)    
16            right=height(root.right)   
17            diameter=left+right
18            largest_diameter[0] = max(diameter,largest_diameter[0])
19
20            curr_height = 1 + max(left,right)
21            return curr_height
22
23        height(root)
24
25        return (largest_diameter[0])    
26
27        