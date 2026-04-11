# Last updated: 11/04/2026, 13:37:27
1from collections import deque
2# Definition for a binary tree node.
3# class TreeNode(object):
4#     def __init__(self, val=0, left=None, right=None):
5#         self.val = val
6#         self.left = left
7#         self.right = right
8class Solution(object):
9    def levelOrder(self, root):
10        """
11        :type root: Optional[TreeNode]
12        :rtype: List[List[int]]
13        """
14        if not root:
15            return ([])
16        ans=[]
17        q=deque()
18        q.append(root)
19
20        while q:
21            level=[]
22            n=len(q)
23            for neigh in range (n):
24                node=q.popleft()
25                level.append(node.val)
26
27                if node.left:
28                    q.append(node.left)
29                if node.right:
30                    q.append(node.right)    
31
32            ans.append(level)  
33        return ans          
34