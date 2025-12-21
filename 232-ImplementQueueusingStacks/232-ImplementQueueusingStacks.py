# Last updated: 21/12/2025, 20:30:40
1class MyQueue(object):
2
3    def __init__(self):
4        self.in_stack = []
5        self.out_stack = []
6
7    def push(self, x):
8        """
9        :type x: int
10        :rtype: None
11        """
12        self.in_stack.append(x)
13        
14
15    def pop(self):
16        """
17        :rtype: int
18        """
19        self.peek()
20        return self.out_stack.pop()
21        
22
23    def peek(self):
24        """
25        :rtype: int
26        """
27        if not self.out_stack:
28            while self.in_stack:
29                self.out_stack.append(self.in_stack.pop())
30        return self.out_stack[-1]
31        
32
33    def empty(self):
34        """
35        :rtype: bool
36        """
37        return not self.in_stack and not self.out_stack
38        
39
40
41# Your MyQueue object will be instantiated and called as such:
42# obj = MyQueue()
43# obj.push(x)
44# param_2 = obj.pop()
45# param_3 = obj.peek()
46# param_4 = obj.empty()