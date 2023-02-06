from ast import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:

            if i == "+":
                stack.append(int(stack[len(stack)-1]) +
                             int(stack[len(stack)-2]))

            elif i == "C":
                stack.pop()

            elif i == "D":
                stack.append(int(stack[len(stack) - 1]) * 2)
            else:
                stack.append(int(i))

        return sum(stack)
