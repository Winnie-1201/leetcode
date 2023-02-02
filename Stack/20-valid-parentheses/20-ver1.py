class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if stack and self.same(stack[len(stack)-1], i):
                stack.pop()
            else:
                stack.append(i)

        return True if len(stack) == 0 else False

    def same(self, s1, s2):
        if (s1 == "{" and s2 == "}") or (s1 == "(" and s2 == ")") or (s1 == "[" and s2 == "]"):
            return True

        else:
            return False
