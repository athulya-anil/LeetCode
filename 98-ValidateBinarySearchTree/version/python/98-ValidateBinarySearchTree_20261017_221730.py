# Last updated: 17/10/2026, 22:17:30
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: TreeNode | None) -> bool:
9
10        def check(node,minn,maxx):
11
12            if not node:
13                return True
14
15            if node.val <= minn or node.val >= maxx:
16                return False
17
18            return (check(node.left,minn,node.val) and check(node.right,node.val,maxx))        
19            
20        return check(root, float('-inf'), float('inf'))    
21        
22        