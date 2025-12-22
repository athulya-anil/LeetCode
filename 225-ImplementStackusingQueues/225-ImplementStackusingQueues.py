# Last updated: 22/12/2025, 18:30:33
1class MyStack(object):
2
3    def __init__(self):
4        self.q1 = deque()
5        self.q2 = deque()
6        
7
8    def push(self, x):
9        """
10        :type x: int
11        :rtype: None
12        """
13        self.q2.append(x)
14
15        while self.q1:
16            self.q2.append(self.q1.popleft())
17
18        self.q1, self.q2 = self.q2, self.q1    
19        
20
21    def pop(self):
22        """
23        :rtype: int
24        """
25        return self.q1.popleft()
26        
27
28    def top(self):
29        """
30        :rtype: int
31        """
32        return self.q1[0]
33        
34
35    def empty(self):
36        """
37        :rtype: bool
38        """
39        return not self.q1
40        
41
42
43# Your MyStack object will be instantiated and called as such:
44# obj = MyStack()
45# obj.push(x)
46# param_2 = obj.pop()
47# param_3 = obj.top()
48# param_4 = obj.empty()