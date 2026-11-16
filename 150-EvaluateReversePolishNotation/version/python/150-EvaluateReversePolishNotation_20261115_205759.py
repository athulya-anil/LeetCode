# Last updated: 15/11/2026, 20:57:59
1class Solution:
2    def evalRPN(self, tokens: list[str]) -> int:
3        stack=[]
4        for char in tokens:
5            if char == "+":
6                stack.append(stack.pop()+stack.pop())
7            elif char == "*":
8                stack.append(stack.pop()*stack.pop())
9            elif char == "-":
10                a=stack.pop()
11                b=stack.pop()
12                stack.append(b-a)
13            elif char == "/":
14                a=stack.pop()
15                b=stack.pop()
16                stack.append(int(b/a))
17            else:
18                stack.append(int(char))     
19        return stack[0]               
20
21        