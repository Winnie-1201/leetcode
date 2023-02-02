
from ast import List
from operator import add, sub, mul


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = int(tokens[0])
        
        for i in tokens:
            if i == "+":
                s = int(stack.pop()) + int(stack.pop())
                total = s
                stack.append(s)
            elif i == "*":
                s = int(stack.pop()) * int(stack.pop())
                total = s
                stack.append(s)
            elif i == "-":
                s1 = int(stack.pop())
                s2 =  int(stack.pop())
                s = s2 - s1
                total = s
                stack.append(s)
            elif i == "/":
                s1 = int(stack.pop())
                s2 =  int(stack.pop())
                s = s2 / s1 if s1 != 0 else s1 / s2
                total = s
                stack.append(s)
            else:
                stack.append(i)
                

        return int(total)

# other solution
def evalRPN(self, tokens: List[str]) -> int:
        hashMap = {"+":add, "-":sub, "*":mul, "/":lambda a,b: int(a/b)}
        stack = []
        for token in tokens:
            if token in hashMap:
                b = stack.pop()
                a = stack.pop()
                c = hashMap[token](a, b)
            else:
                c = int(token)
            stack.append(c)
        return stack[-1]
                