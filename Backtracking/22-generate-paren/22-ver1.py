from ast import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = []

        def helper(left, right):
            if left == n and right == n:
                res.append("".join(temp))
                return

            if left < n:
                temp.append("(")
                helper(left + 1, right)
                temp.pop()

            if right < left:
                temp.append(")")
                helper(left, right + 1)
                temp.pop()

        helper(0, 0)
        return res
